"""
If there are 23 students in your class, what are the chances that two of them have the same birthday? You can estimate
this probability by generating random samples of 23 birthdays and checking for matches.
en.wikipedia.org/wiki/Birthday_paradox
Hint: you can generate random birthdays with the randint function in the random module.
"""
import random
from math import prod


def has_duplicates(lst):
    return len(lst) != len(set(lst))


def birthday_probability(n_simulations=1000, n_students=23):
    # create students and assign them random birthdays
    count_duplicates = 0
    for _ in range(n_simulations):
        students = [random.randint(1, 365) for _ in range(n_students)]

        # how to determine the probability there are two students with the same birthday?
        # can use the concept of complementary probability, which states that the probability of an event occurring is
        # 1 minus the probability of it not occurring
        # P(at least one repeats) = 1 - P(no repeats)
        if has_duplicates(students):
            count_duplicates += 1
    return count_duplicates / n_simulations


if __name__ == '__main__':
    print(birthday_probability(10000, 23))
