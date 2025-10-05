import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    csv_to_json('sample.csv', 'output.json')
    print("CSV converted to JSON successfully.")
