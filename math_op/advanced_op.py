import math

def average(nums):
    return sum(nums) / len(nums)

def power(base, exponent):
    return base ** exponent

def sqrt(num):
    if num < 0:
        raise ValueError("Cannot compute square root of negative number")
    return num ** 0.5

def log(num, base = 10):
    if num <= 0 or base <= 0:
        raise ValueError("Cannot compute logarithm of non-positive number")
    
    return math.log(num, base)