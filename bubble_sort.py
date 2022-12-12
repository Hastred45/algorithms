
def bubble_sort(lenght, array):
    flag = 1
    for j in range(lenght - 1):
        for num in range(lenght - j - 1):
            if array[num] > array[num + 1]:
                array[num], array[num + 1] = array[num + 1], array[num]
                flag = 1
        if flag == 1:
            print(' '.join(array))
            flag = 0


if __name__ == '__main__':
    long = 5
    numbers = ['9', '4', '3', '2', '1']
    bubble_sort(long, numbers)
