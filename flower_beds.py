def segmentsUnion(data):
    data.sort()
    newData = []
    start = data[0][0]
    end = data[0][1]
    for i in range(n-1):
        if end < data[i+1][0]:
            newData.append('{} {}'.format(start, end))
            start = data[i+1][0]
            end = data[i+1][1]
        elif data[i+1][1] > end:
            end = data[i+1][1]
    newData.append('{} {}'.format(start, end))
    return newData


n = 3
if n >= 1:
    data = [(9, 10), (1, 3), (3, 4)]
    for i in range(n):
        data.append(tuple([int(x) for x in input().split()]))
    print('\n'.join(segmentsUnion(data)), end='')
