def bubble_sort(number, array):
    for i in range(number - 1):
        for j in range(0, number-i-1):
            var1 = array[j] + array[j+1]
            var2 = array[j + 1] + array[j]
            # print(var1, var2)
            if int(var1) < int(var2):
                array[j], array[j+1] = array[j+1], array[j]
                print(array)

    print("".join(array))


if __name__ == '__main__':
    number = 6
    source_array = ['9', '10', '1', '1', '1', '6']
    bubble_sort(number, source_array)
