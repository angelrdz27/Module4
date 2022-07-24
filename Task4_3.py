### Task 4.3
'''Implement a function which works the same as `str.split` method
(without using `str.split` itself, ofcourse).'''

def split_func(var, string):
    new_string = []
    old_string = ""
    for x in string:
        if x == var or x == string[-1]:
            if x == string[-1]: old_string += x
            new_string.append(old_string)
            old_string = ""
        else:
            old_string += x
    return new_string
string = str(input('Introduce the string with the char for splitting'))
var = str(input('Introduce the split char that you want to use'))
if __name__ == "__main__":
    print(split_func(var, string))
