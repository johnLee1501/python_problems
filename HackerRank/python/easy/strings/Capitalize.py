#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    a_string = s.split(' ')
    return ' '.join((word.capitalize() for word in a_string))


if __name__ == '__main__':
    print(solve(input()))
