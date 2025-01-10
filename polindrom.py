"""
Write a function that takes a string as input and returns True if it's a palindrome and False otherwise.

Example 1:
palindrome("racecar") ➞ True

Example 2:
palindrome("not a palindrome") ➞ False

Example 3:
palindrome("taco cat") ➞ True


Notes:
You should ignore spaces, special characters and case.
A palindrome is a word that reads the same forwards and backwards.

"""



def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

print(is_palindrome("racecar"))
print(is_palindrome("not a palindrome"))
print(is_palindrome("taco cat"))
print(is_palindrome("radar"))
