### Task 4.8
'''Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
of tuples containing pairs of elements. Pairs should be formed as in the
example. If there is only one element in the list return `None` instead.
Example:
```python
>>> get_pairs([1, 2, 3, 8, 9])
[(1, 2), (2, 3), (3, 8), (8, 9)]

>>> get_pairs(['need', 'to', 'sleep', 'more'])
[('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]

>>> get_pairs([1])
None'''

def get_pairs(values: list) -> list[tuple]:
    '''
    Returns a list of tuples containing pairs of elements
    Pairs will be created from item list as (index, index+1)
    If there is only one element in the list return 'None' instead.
    :param values: list of values
    :return: list of pairs
    '''
    if len(values) > 1:
        return [(values[index], values[index + 1]) for index in range(len(values)- 1)]
    return None

if __name__ == '__main__':
    assert get_pairs([]) is None
    assert get_pairs([1, ]) is None
    assert get_pairs([1, 2, 3, 8, 9]) == [(1, 2), (2, 3), (3, 8), (8, 9)]
    assert get_pairs(['need', 'to', 'sleep', 'more']) == [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]