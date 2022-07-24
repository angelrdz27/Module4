### Task 4.2
'''Write a function that check whether a string is a palindrome or not. Usage of
any reversing functions is prohibited. To check your implementation you can use
strings from [here](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).'''

def palindrome():
    i = str(input('Introduce the word you want to check '))
    string = list(i)
    size_str = len(string)
    rev = [None]*size_str
    for x, y in zip(string, range(size_str)):
        rev[y - size_str] = x
    if string == rev:
        print('This string is a Palindrome')
    else:
        print('This string is not a Palindrome')

print('Welcome to the palindrome function checker')
palindrome()