def build_diff(data1, data2):
    diff = {}
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    for key in keys:
        status = {'name': key}
        if key not in data2:
            status['operation'] = 'only sisyphus'
            status['version'] = data1[key]
        elif key not in data1:
            status['operation'] = 'only p10'
            status['version'] = data2[key]
        elif data1[key] != data2[key]:
            status['operation'] = 'different versions'
            status['old'] = data1[key]
            status['new'] = data2[key]
        else:
            status['operation'] = 'unchanged'
            status['version'] = data2[key]
        diff[key] = status
    return diff
