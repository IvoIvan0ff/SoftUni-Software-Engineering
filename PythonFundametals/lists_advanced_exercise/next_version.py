version = input().split('.')
version_as_int = [int(i) for i in version]
if version_as_int[-1] <= 9:
    version_as_int[-1] += 1
    if version_as_int[-1] == 10:
        version_as_int[-1] = 0
        version_as_int[-2] += 1
        if version_as_int[-2] == 10:
            version_as_int[-2] = 0
            version_as_int[-3] += 1
version_as_string = [str(i) for i in version_as_int]
print('.'.join(version_as_string))
