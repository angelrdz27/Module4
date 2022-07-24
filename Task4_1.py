### Task 4.1
"""Implement a function which receives a string and replaces all `"` symbols
with `'` and vise versa."""

def string_replace( ):
    i = input('Please introduce the string ')
    temp = list(i)
    index = 0
    for symbol in temp:
        if symbol == "'":
            temp[index] = '"'
        elif symbol == '"':
            temp[index] = "'"
        index += 1
        string = "".join(temp)
    return string
print(string_replace( ))