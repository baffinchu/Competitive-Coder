# {'time': 'O(1)', 'space': 'O(1)'}
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.


def staircase(n):
    for num in range(1, n+1):
        print(' ' * (n - num), end='')
        print('#' * num)


if __name__ == '__main__':
    n = int(input())

    staircase(n)
