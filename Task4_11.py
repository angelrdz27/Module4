### Task 4.11
'''Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers) and combines them into one dictionary.
Dict values ​​should be summarized in case of identical keys

```python
def combine_dicts(*args):
    ...

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2)
>>> {'a': 300, 'b': 200, 'c': 300}


print(combine_dicts(dict_1, dict_2, dict_3)
>>> {'a': 600, 'b': 200, 'c': 300, 'd': 100}'''
import collections

def combine_dicts(*args) -> dict[str, int]:
    '''
    Recives changeable number of dictionaries (keys - letters, values - numbers) and combines them into one dictionary.
    :param args: Recives changeable number of dictionaries (keys - letters, values - numbers) and combines them into one dictionary.
    :return: Dictionary where values wull be summarized in case of identical keys.
    '''
    combine_dict= collections.defaultdict(lambda: 0)
    for one_dict in args:
        for key in one_dict:
            combine_dict[key] += one_dict[key]
    return combine_dict

if __name__ == '__main__':
     dict_1 = {'a': 100, 'b': 200}
     dict_2 = {'a': 200, 'c': 300}
     dict_3 = {'a': 300, 'd': 100}

     assert not combine_dicts()
     assert not combine_dicts({})
     assert not combine_dicts({}, {})
     assert combine_dicts(dict_1, dict_2) == {'a': 300, 'b': 200, 'c': 300}
     assert  combine_dicts(dict_1, dict_2, dict_3) == {'a': 600, 'b': 200, 'c': 300, 'd': 100}