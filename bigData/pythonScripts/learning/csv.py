import csv, itertools, json

def cluster(rows):
    result = []
    for key, group in itertools.groupby(rows, key=lambda r: r[0]):
        group_rows = [row[1:] for row in group]
        if len(group_rows[0]) == 2:
            cost = group_rows[0][0]
            result.append({key: cost})
        else:
            result.append({key: cluster(group_rows)})
    return result

if __name__ == '__main__':
    s = '''\
Gondwanaland,Bobs Bits,Operations,nuts,332
Gondwanaland,Bobs Bits,Operations,bolts,254
Gondwanaland,Maureens Melons,Operations,nuts,123
'''
    rows = list(csv.reader(s.splitlines()))
    r = cluster(rows)
    print json.dumps(r, indent=4)
