### Task 4.5
'''Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple
of a given integer's digits.
Example:
```python
>>> get_digits(87178291199)
(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)'''

class NumberError(Exception):
    '''
    Exception used by this module.
    '''

def get_digits(num: int) -> tuple[int]:
    '''
    Returns a tuple of a given integer's digit:
    :param num: the input int number.
    :return: the int number's in a tuple
    '''
    if num < 0:
        raise NumberError('Input must be a zero or positive number')
    return tuple(int(digit) for digit in str(num))

if __name__ == '__main__':
    assert get_digits(87178291199) == (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
    assert get_digits(0) == (0,)
    try:
        assert get_digits(-1) == (1,)
    except NumberError:
        assert True
    else:
        assert False