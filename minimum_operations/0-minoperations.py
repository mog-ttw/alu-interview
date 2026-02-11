#!/usr/bin/python3
def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:

        while n % factor == 0:
            n //= factor
            operations += factor

        factor += 1

    return operations