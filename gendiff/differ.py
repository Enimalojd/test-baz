from gendiff.build_diff import build_diff
from gendiff.formatters.json import format_json
from gendiff.data.get_data import get_sisyphus_data, get_p10_data
from gendiff.parser import get_data


def generate_diff(format_name='json'):
    if format_name == 'json':
        path_sisyphus = get_sisyphus_data()
        path_p10 = get_p10_data()
        data1 = get_data(path_sisyphus)
        data2 = get_data(path_p10)
        diff = build_diff(data1, data2)
        return format_json(diff)
    else:
        raise ValueError('format must be json')
