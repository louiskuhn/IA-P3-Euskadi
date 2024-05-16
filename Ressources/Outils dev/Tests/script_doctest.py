"""
>>> from math import sqrt
>>> res = sqrt(9)
>>> res
3.0
>>> a = 12
>>> a == ma_fonction(3,4)
True
"""

def ma_fonction(a, x):
    """
    returns the product of a and x
    parameters : a, x: numeric
    >>> ma_fonction(3,4)
    12
    """
    return a*x

print(f"{ma_fonction(3,4)=}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
