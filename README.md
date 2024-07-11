# JSON to CSV Converter
## Description
This script converts a JSON file into a CSV file using Python. It reads a JSON file containing a list of dictionaries, transforms the data into a pandas DataFrame, and optionally saves it as a CSV file.
## Features
- Reads a JSON file and converts it to a pandas DataFrame.
- Optionally saves the DataFrame as a CSV file.
- Includes error handling for file reading and JSON decoding.
- Provides logging to track the progress and any errors.
- Accepts command-line arguments for input and output file paths.
## Requirements
- Python 3.x
- pandas
- argparse
## Installation
1. Clone the repository or download the script file.
2. Install the required Python packages using pip:
```console
pip install -r requirements
```
## Usage
To use the script, run it from the command line with the path to the JSON file as an argument. Optionally, you can also provide a path for the output CSV file.

### Command-Line Arguments
- `json_file`: Path to the input JSON file.
- `output_csv` (optional): Path to save the output CSV file.
### Example
1. Save the following JSON content into a file named `example.json`:
```json
[
    {
        "id": 1,
        "name": "Alice",
        "age": 30,
        "city": "New York"
    },
    {
        "id": 2,
        "name": "Bob",
        "age": 25,
        "city": "Los Angeles"
    },
    {
        "id": 3,
        "name": "Charlie",
        "age": 35,
        "city": "Chicago"
    },
    {
        "id": 4,
        "name": "David",
        "age": 28,
        "city": "Houston"
    }
]
```
2. Run the script with the JSON file as input and specify an output CSV file name:
```console
python script_name.py example.json output.csv
```
3. The script will read the JSON file, convert it to a DataFrame, and save it as `output.csv`:
```console
id,name,age,city
1,Alice,30,New York
2,Bob,25,Los Angeles
3,Charlie,35,Chicago
4,David,28,Houston
```
## Logging
The script uses the `logging` module to provide feedback on the process:
- INFO: General information about the progress.
- ERROR: Details about any errors encountered.
## Error Handling
The script includes error handling for:
- File not found errors.
- JSON decoding errors.
- Unexpected exceptions.
