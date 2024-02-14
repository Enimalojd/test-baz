import os.path
import requests
import json
from gendiff.config import DATA_PATH1, DATA_PATH2


def main_dir():
    return os.path.dirname(os.path.abspath(__file__))


def clear_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.truncate(0)


def get_sisyphus_data():
    data = requests.get(DATA_PATH1).json()
    dir = main_dir()
    res_path = os.path.join(dir, 'json/sisyphus.json')
    clear_file(res_path)
    with open(res_path, 'w') as file:
        names = {package["name"]: package["version"]
                 for package in data['packages']}
        json.dump(names, file)
    return res_path


def get_p10_data():
    data = requests.get(DATA_PATH2).json()
    dir = main_dir()
    res_path = os.path.join(dir, 'json/p10.json')
    clear_file(res_path)
    with open(res_path, 'w') as file:
        names = {package["name"]: package["version"]
                 for package in data['packages']}
        json.dump(names, file)
    return res_path


def save_data(data):
    dir = main_dir()
    res_path = os.path.join(dir, 'json/result.json')
    clear_file(res_path)
    with open(res_path, 'w') as file:
        file.write(data)
    print(res_path)
    return None
