def insert_it(array):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and item_to_insert < array[j-1]:
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert
        print(f"step {i}, sorted {i+1} elements: {array}")


insert_it([11, 101, 2, 9, 7, 1, 88])
