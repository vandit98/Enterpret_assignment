import pandas as pd

class PATH:
    data_path = "./enterpret.csv"

roi_column = "Content"
req_columns = ['ID', 'URL', 'Source', 'Type', 'CreatedAt', 'Language', 'Record Sentiment', 'Tracked Keywords', 'Reasons', 'Content']

def preprocess_csv(input_csv: str, output_csv: str):
    # Load data
    data = pd.read_csv(input_csv)[req_columns]
    
    # Filter out rows with "<AUDIO_CONTENT>" and nulls in the Content column
    filtered_data = data[(data[roi_column] != "<AUDIO_CONTENT>") & (data[roi_column].notnull())]
    
    # Select 'ID' and 'Content', rename 'Content' to 'Conversation'
    df_filtered = filtered_data[['ID', 'Content']].rename(columns={'Content': 'Conversation'})
    
    # Create 'Metadata' column containing all other columns as JSON strings
    df_filtered['Metadata'] = filtered_data.drop(columns=['ID', 'Content']).to_dict(orient='records')
    
    # Save the result to a new CSV file
    df_filtered.to_csv(output_csv, index=False)


preprocess_csv(PATH.data_path, 'filtered_output.csv')
