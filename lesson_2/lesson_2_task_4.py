n = int(input("Введите число:"))


def check_divisibility(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            print(f"{i} -Fizz")
        elif i % 5 == 0:
            print(f"{i} -Bizz")
        else:
            print(i)


check_divisibility(n)
