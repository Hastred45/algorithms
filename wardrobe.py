def counting_sort(array, k):
    counted_values = [0] * k
    for n in array:
        counted_values[n] += 1
        
    for color in range(k):
        print((str(color) + ' ') * counted_values[color], end='')

if __name__ == '__main__':
    n = input()
    k = 3
    arr = [1, 0, 0, 2, 2, 1, 1, 0, 1, 2]
    counting_sort(arr, k)