### Task 4.7
'''Implement a function `foo(List[int]) -> List[int]` which, given a list of
integers, return a new list such that each element at index `i` of the new list
is the product of all the numbers in the original array except the one at `i`.
Example:
```python
>>> foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]

>>> foo([3, 2, 1])
[2, 3, 6]'''

def foo(numbers: list[int]) -> list[int]:
    '''
    Returns a list with the product of all the numbers in the array except the one at count
    :param numbers: List with multiple int
    :return: a list with the product of the numbers in the original array except the one at count
    '''
    result = []
    for count in range(len(numbers)):
        current_num = 1
        for num in numbers:
            if numbers[count] == num:
                num = 1
            else:
                current_num = current_num * num
        result.append(current_num)
    return result


if __name__ == '__main__':
    assert foo([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert foo([3, 2, 1]) == [2, 3, 6]
