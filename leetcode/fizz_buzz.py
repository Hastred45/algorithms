import time

start = time.time()


def fizzBuzz(n):
    fizzbuzz_list = list(range(1, n + 1))
    for i in range(n):
        if not fizzbuzz_list[i] % 15:
            fizzbuzz_list[i] = 'FizzBuzz'

        elif not fizzbuzz_list[i] % 3:
            fizzbuzz_list[i] = 'Fizz'

        elif not fizzbuzz_list[i] % 5:
            fizzbuzz_list[i] = 'Buzz'

        else:
            fizzbuzz_list[i] = str(fizzbuzz_list[i])
    print(fizzbuzz_list)


fizzBuzz(15)

end = time.time()
# print("The time of execution of above program is :",
#       (end-start) * 10**3, "ms")
