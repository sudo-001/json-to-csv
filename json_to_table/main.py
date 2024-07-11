import pandas as pd
import json
import os
import argparse
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to read a JSON file and convert it to a DataFrame
def json_to_table(json_file, output_csv=None):
    # Check if the file exists
    if not os.path.exists(json_file):
        logging.error(f"The file {json_file} does not exist.")
        return None

    try:
        # Read the JSON file
        with open(json_file, 'r') as file:
            data = json.load(file)
        
        # Convert JSON data to DataFrame
        df = pd.DataFrame(data)
        
        # Write DataFrame to CSV if output path is provided
        if output_csv:
            df.to_csv(output_csv, index=False)
            logging.info(f"CSV file saved to {output_csv}")
        
        return df
    
    except json.JSONDecodeError as e:
        logging.error(f"Error reading JSON file: {e}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Convert JSON file to CSV")
    parser.add_argument("json_file", help="Path to the input JSON file")
    parser.add_argument("output_csv", help="Path to save the output CSV file", nargs='?', default=None)
    args = parser.parse_args()
    
    # Convert JSON to table
    table = json_to_table(args.json_file, args.output_csv)
    
    # Print the resulting DataFrame
    if table is not None:
        print(table)
