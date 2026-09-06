import json

def load_test_data(test_file: str):
    with open(f"test_data/{test_file}", "r") as data:
        return json.load(data)