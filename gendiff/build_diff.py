from gendiff.compare import compare_versions


def build_diff(data1, data2):
    diff = {}
    sisyphus_packages = []
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    for key in keys:
        status = {'name': key}
        if key not in data2:
            status['branch'] = 'sisyphus'
            status['version'] = data1[key]
        elif key not in data1:
            status['branch'] = 'p10'
            status['version'] = data2[key]
        elif data1[key] != data2[key]:
            status['branch'] = 'different versions'
            status['sisyphus'] = data1[key]
            status['p10'] = data2[key]
            if compare_versions(data1[key], data2[key]):
                sisyphus_packages.append(key)
        else:
            status['branch'] = 'coincidence'
            status['version'] = data2[key]
        diff[key] = status
    diff['sisyphus_over'] = sisyphus_packages
    return diff
