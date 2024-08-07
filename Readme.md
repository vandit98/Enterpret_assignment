# Ml Intern Assignment: Extracting Claims from Records Using Large Language Models (LLMs)

## Overview
This project aims to develop a system using Large Language Models (LLMs) to accurately extract claims from textual records such as user feedback, interaction logs, and other conversational data. The system will preprocess the data, identify relevant claims, and provide structured outputs indicating where these claims are discussed within the records.

## Demo


https://github.com/vandit98/Enterpret_assignment/assets/91458535/d83d202b-aaf2-48e6-b1de-08e048fa6a5f


## Project Structure
![Screenshot from 2024-06-29 20-38-54](https://github.com/vandit98/Enterpret_assignment/assets/91458535/ebc40fa7-0c3a-448f-b594-518854216cf6)

### Files Included
- `main.py`: Entry point for running the claim extraction process.
- `preprocess.py`: Python module for preprocessing the input CSV file.
- `claim_identifier.py`: Python module encapsulating claim identification logic using LLMs.
- `requirements.txt`: List of Python packages required for the project.

### Setup Instructions

1. **Create a Virtual Environment:**
   ```bash
   conda create -n env_name python==3.12
   conda activate env_name
   ```
2. **Installing Dependencies:**
  ```bash
  pip install -r ./requirements.txt
  ```

3. **Run the Extraction Process::**
  ```bash
  python3 ./main.py
  ```
### Files Explanation
**main.py**: Initiates the claim extraction process by calling functions from preprocess.py and claim_identifier.py.

**preprocess.py**: Handles data preprocessing tasks such as cleaning, normalizing, and structuring the input data from a CSV file (enterpret.csv).

**claim_identifier.py**: Implements claim identification using Mistral's large language models. It splits the text into manageable units, processes them through the LLM, and identifies indices where claims are discussed.

**.env** - Mistral API keys; I have exposed them so that one can test my code. Since they are free trials which expire on 5th July.
### Output Format

     {
        "record_id": "e0e5cedb-2da1-5476-bfef-366eebc71656",
        "claim_indices": ["1"],
        "metadata": "{'URL': 'https://dashboard.enterpret.com/enterpretinc/record/e0e5cedb-2da1-5476-bfef-366eebc71656', 'Source': 'Slack,' 'Type': 'RecordTypeConversation', 'CreatedAt': '2024-01-12T22:28:45Z', 'Language': 'eng', 'Record Sentiment': 'NEGATIVE', 'Tracked Keywords': nan, 'Reasons': 'Issue With Decreased Feedback Volume From Sources'}",
        "indexed_messages_str": "{\"1\": \"Agent: Mike McNasby jil It looks like the volume of feedback coming from Discord has dropped to zero. The channel for issues and bugs was the primary driver, just wanted to confirm if this was intentional?\", \"2\": \"\", \"3\": \"\"}"
    }

Note -  It is a bit different from the expected format. Because I wanted to return the index content where claims are being made.


## Approach

### Using Quantized Models from Hugging Face
- **Model Choice:** I tried the quantized model from [Hugging Face](https://huggingface.co/TheBloke/Llama-2-7B-GGML/tree/main), aiming for a balance between size and performance.
- **JSON Output Needs:** Since my project requires JSON output, I found the Mistral large model, which naturally outputs in JSON, to be promising.

### Experimenting with llama.cpp and Ollama Models
- **Model Size:** I tested various models like the 2B H2O-Danube2-1.8B, but even after reducing their size, they still needed over 3GB.
- **Hardware Limits:** My laptop isn't powerful enough for heavy GPU tasks, making it hard to use large models.
- **Fine-tuning:** I tried fine-tuning these models with my data, but the results weren't great.

## Challenges

### Model Size and Efficiency
- Even the optimized models were too large, making it hard to run them on my limited hardware.
- Models like the 2B H2O-Danube2-1.8B still used too much memory, even after shrinking them.

### Fine-tuning and Output Format
- Fine-tuning took a lot of effort and resources, and the results didn’t improve much.
- Not all models could easily produce JSON output, which I need for my project.

### Hardware Limitations
- My laptop’s limited GPU power was a big obstacle, forcing me to compromise on model size and performance.

### Project Requirements
- Finding a model that fits my hardware, outputs JSON, and performs well was tough. The Mistral model seemed good but still required a lot of resources.
