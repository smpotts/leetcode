def collatzSteps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2

        elif n % 2 == 1:
            n = 3 * n + 1

        steps += 1
    return steps


if __name__ == '__main__':
    print(collatzSteps(3))