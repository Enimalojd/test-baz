import os
import json


def get_data(file_path):
    root, ext = os.path.splitext(file_path)
    with open(file_path, 'r', encoding="utf-8") as f:
        return parse(f.read(), ext)


def parse(data, format):
    if format in ['.json']:
        return json.loads(data)
    else:
        raise ValueError(f'Unsupported file extension: {format}')
