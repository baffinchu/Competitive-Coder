# {'time': 'O(1)', 'space': 'O(1)'}
#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#


def timeConversion(s):
    #
    # Write your code here.
    #
    hour = int(s[:2])
    if s[8:] == 'PM' and not hour == 12:
        hour = str((hour + 12) % 24)
        return hour + s[2:8]
    elif s[8:] == 'AM' and hour == 12:
        return '00' + s[2:8]
    else:
        return s[:8]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
