# https://contest.yandex.ru/contest/28412/problems/A/

n = int(input())
containers = list(map(int, input().split()))
answer = 0
largest_volume = containers[0]
for i in range(len(containers)):
    largest_volume = max(containers[i], largest_volume)
    if containers[i] < largest_volume:
        answer = -1
        break
print(max(containers) - min(containers) if answer == 0 else answer)
