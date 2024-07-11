import pandas as pd
import json

# Fonction pour lire un fichier JSON et le transformer en DataFrame
def json_to_table(json_file, output_csv=None):
    # Lire le fichier JSON
    with open(json_file, 'r') as file:
        data = json.load(file)
        
    # Transformer les donnees JSON en DataFrame
    df = pd.DataFrame(data)
        
    if output_csv:
        df.to_csv(output_csv, index=False)
            
    return df
    

if __name__ == "__main__":
    json_file = "/home/sudo_dev/Desktop/Challenges/LLMs4OL/model/Train dataset/A.1(FS)_WordNet_Test.json"
    output_csv = "./outputs/A.1(FS)_WordNet_Test.csv"
    
    table = json_to_table(json_file, output_csv)
    
    print(table)