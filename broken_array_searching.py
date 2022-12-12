from typing import List


def broken_search(nums: List[int], target: int) -> int:
    """Поиск в смещенном сортированном массиве.
    Возвращает индекс элемента.
    Если элемента нет в массиве, возвращает -1."""
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if target == nums[middle]:
            return middle

        if nums[left] <= nums[middle]:
            if nums[left] <= target <= nums[middle]:
                right = middle - 1
            else:
                left = middle + 1

        else:
            if nums[middle] <= target <= nums[right]:
                left = middle + 1
            else:
                right = middle - 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


if __name__ == '__main__':
    test()
