### Task 4.10
'''Implement a function that takes a number N as an argument and returns a dictionary, where the key is a n (n ∈ [1, N]) and the value is the square of n (n**2).
```python
print(generate_squares(5))
>>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''

def generate_squares(n_values : int) -> dict[int, int]:
    '''
    Take a number N as an argument and return a dictionary, the key
    is a n (n ∈ [1, N]) and the value is the square of n (n**2)
    :param n_values: N argument.
    :return: Where the key is a n (n ∈ [1, N]) and the value is the square of n (n**2)
    '''
    return {n :n**2 for n in range(1, n_values + 1)}

if __name__ == '__main__':
    assert generate_squares(0) == {}
    assert generate_squares(1) == {1: 1}
    assert generate_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}