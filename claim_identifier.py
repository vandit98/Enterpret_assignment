import os
import json
import pandas as pd
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")
model = "mistral-large-latest"

client = MistralClient(api_key=api_key)

class ClaimIdentifier:
    def __init__(self):
        self.client = client
        self.model = model
        self.template = (
            "You are an intelligent AI assistant that identifies claims from a conversation. "
            "For each message in the conversation, return 1 if it is a claim and 0 if it is not. "
            "Conversation: {Conversation} "
            "Response format: {{1:0, 2:1, ...}}"
        )

    def create_message_content(self, conversation: str) -> str:
        return self.template.format(Conversation=conversation)

    def split_conversation(self, conversation: str) -> dict:
        messages = conversation.split("\n")
        return {i + 1: msg.strip() for i, msg in enumerate(messages)}

    async def process_message(self, message: str):
        conversation = self.create_message_content(message)
        messages = [ChatMessage(role="user", content=conversation)]
        
        chat_response = self.client.chat(
            model=self.model,
            response_format={"type": "json_object"},
            messages=messages,
        )
        
        response_text = chat_response.choices[0].message.content
        try:
            return json.loads(response_text)
        except json.JSONDecodeError:
            raise ValueError("Mistral response is not valid JSON: " + response_text)

    async def identify_claims(self, conversation: str):
        indexed_messages = self.split_conversation(conversation)
        indexed_messages_str = json.dumps(indexed_messages)
        
        claims_result = await self.process_message(indexed_messages_str)
        return [index for index, is_claim in claims_result.items() if is_claim == 1]

    async def process_csv(self, input_csv: str, output_json: str):
        df = pd.read_csv(input_csv)
        
        # Create or load existing JSON file
        if os.path.exists(output_json):
            with open(output_json, 'r') as f:
                results = json.load(f)
        else:
            results = []

        for _, row in tqdm(df.iterrows(), total=len(df), desc="Processing Records"):
            record_id = row['ID']
            conversation = row['Conversation']
            metadata = row["Metadata"]
            claim_indices = await self.identify_claims(conversation)
            
            result = {
                "record_id": record_id,
                "claim_indices": claim_indices,
                "metadata": metadata
            }
            results.append(result)
            
            # Save the result instantly
            with open(output_json, 'w') as f:
                json.dump(results, f, indent=4)
