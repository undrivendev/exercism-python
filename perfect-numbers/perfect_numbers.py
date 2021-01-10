import math


def classify(number):
    if number < 1:
        raise ValueError("input argument must be a positive integer")

    factors_sum = sum(
        [i for i in range(1, math.ceil(number / 2) + 1) if not number % i]) if number > 1 else 0
    if factors_sum == number:
        return "perfect"
    elif factors_sum < number:
        return "deficient"
    else:
        return "abundant"
