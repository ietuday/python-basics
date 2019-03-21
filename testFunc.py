def mul(a, b):
    """
    it is useful for multiplication
    >>> mul(2,3)
    6
    >>> mul(3,5)
    16
    >>> mul(6,2)
    12
    """
    return a*b
if __name__ == "__main__": 
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)

