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
