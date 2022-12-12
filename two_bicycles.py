def binarySearch(money, price, left, right):
    if right <= left and left != 0:
        return -1
    middle = (left + right) // 2
    if money[middle] >= price and (money[middle - 1] < price or middle == 0):
        return middle + 1
    elif price <= money[middle]:
        return binarySearch(money, price, left, middle)
    else:
        return binarySearch(money, price, middle + 1, right)


days = int(input())
money = [int(num) for num in input().split(' ')]
price = int(input())

print(binarySearch(money, price, left=0, right=len(money)), end=' ')
print(binarySearch(money, price * 2, left=0, right=len(money)), end=' ')
