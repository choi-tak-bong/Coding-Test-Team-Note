"""
최대공약수 알고리즘
"""

def gcd(a: int, b: int):
    if a % b == 0:
        return b
    return gcd(b, a % b)
