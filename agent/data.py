import json

def load_swahili_dictionary(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        swahili_dict = json.load(file)
    return swahili_dict
