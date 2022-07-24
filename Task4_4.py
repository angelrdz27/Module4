### Task 4.4
'''Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
which splits the `s` string by indexes specified in `indexes`. Wrong indexes
must be ignored.
Examples:
python
split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

split_by_index("no luck", [42])
["no luck"]'''
def split_by_index(string :str, indexes: list[int]) -> list[str]:
   all_indexes = [0] + [index for index in indexes if 0 <= index < len(string)] + [len(string)]
   all_indexes.sort()
   return [string[all_indexes[i]:all_indexes[i+1]] for  i in range(len(all_indexes)- 1)]

if __name__ == '__main__':
    print(split_by_index("pythoniscool,isn'tit?", [-10, 200, 100]))
    assert split_by_index("pythoniscool,isn'tit?", []) == ["pythoniscool,isn'tit?"]
    assert split_by_index("pythoniscool,isn'tit?", [-10, 200, 100]) == ["pythoniscool,isn'tit?"]
    assert split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]) == ["python", "is", "cool", ",", "isn't", "it?"]
    assert split_by_index("pythoniscool,isn'tit?", [6, -20, 12, 13, 8, 18, 45]) == ["python", "is", "cool", ",", "isn't", "it?"]

