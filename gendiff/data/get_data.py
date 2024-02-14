import requests
import json
import os
from ...config import DATA_PATH1, DATA_PATH2


def main_dir():
    return os.path.dirname(os.path.abspath(__file__))


def clear_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.truncate(0)


def get_sisyphus_data():
    data = requests.get(DATA_PATH1).json()
    res_path = main_dir() + '/json/sisyphus.json'
    with open(res_path, 'w') as file:
        clear_file(res_path)
        names = {package["name"]: package["version"] for package in data['packages']}
        json.dump(names, file)
    return None

def get_p10_data():
    data = requests.get(DATA_PATH2).json()
    res_path = main_dir() + '/json/p10.json'
    with open(res_path, 'w') as file:
        clear_file(res_path)
        names = {package["name"]: package["version"] for package in data['packages']}
        json.dump(names, file)
    return None


def save_data(data):
    res_path = main_dir() + '/json/result.json'
    with open(res_path, 'w') as file:
        file.write(data)
    return None