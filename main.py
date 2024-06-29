import asyncio
import os
import json
from claim_identifier import ClaimIdentifier
from preprocess import preprocess_csv

async def main():
    input_csv = "./data//enterpret.csv"
    preprocessed_csv = "./data/filtered_output.csv"
    output_json = "./data/claims_output.json"

    try:
        # Preprocess the CSV
        preprocess_csv(input_csv, preprocessed_csv)

        # Initialize ClaimIdentifier
        claim_identifier = ClaimIdentifier()

        # Process CSV and save claims to JSON
        await claim_identifier.process_csv(preprocessed_csv, output_json)

    except Exception as e:
        print(f"An error occurred: {e}")

    # Handling progress JSON
    try:
        if os.path.exists(output_json):
            with open(output_json, 'r') as f:
                progress = json.load(f)
                print("Progress saved so far:", json.dumps(progress, indent=4))
        else:
            progress = {"status": "No progress saved yet."}
            with open(output_json, 'w') as f:
                json.dump(progress, f, indent=4)
            print(progress)
    except json.JSONDecodeError as json_err:
        print(f"Error loading JSON: {json_err}")
    except Exception as file_err:
        print(f"File handling error: {file_err}")

if __name__ == "__main__":
    asyncio.run(main())
