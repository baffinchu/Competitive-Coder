# {'time': 'O(n)', 'space': 'O(n)'}
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.


def plusMinus(arr):
    n = len(arr)
    positiveCount = len([num for num in arr if num > 0])
    negativeCount = len([num for num in arr if num < 0])
    zeroCount = len([num for num in arr if num == 0])

    print(f"{positiveCount/n:.6}")
    print(f"{negativeCount/n:.6}")
    print(f"{zeroCount/n:.6}")


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
