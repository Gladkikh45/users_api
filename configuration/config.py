import json
from pprint import pprint


def get_config() -> dict:
    json_file = 'config.json'
    with open(json_file, 'r') as json_dict:
        data = json.loads(json_dict.read())
        # pprint(data)
        return data

# get_config()