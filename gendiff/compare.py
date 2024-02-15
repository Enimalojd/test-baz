def compare_versions(version1, version2):
    try:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
    except ValueError:
        return False
    for i in range(min(len(v1), len(v2))):
        if v1[i] > v2[i]:
            return True
    if len(v1) > len(v2):
        return True
    return False
