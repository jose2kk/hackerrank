#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return ' '.join([
        word.title() if word.isalpha()
        else word 
        for word in s.split(' ')
    ])
    
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)