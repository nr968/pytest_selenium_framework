import json

def get_config():
    with open("config/config.json", "r") as config:
        return json.load(config)