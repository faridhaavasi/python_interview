'''
task:
    Write a function that takes a list of integers and returns True if the list is a palindrome and False otherwise.
    A list is considered a palindrome if it reads the same forwards and backwards.
    For example, [1, 2, 3, 2, 1] is a palindrome, but [1, 2, 3, 4, 5] is not.
    You may not use the reverse() method for lists.
    You may not use the == operator to compare lists.
    You may not use the slicing operator to reverse the list.
    You may not use the list() constructor to create a reversed copy of the list.
    You may not use the list() constructor to create a list from a string.
    You may not use the join() method for strings.
    You may not use the reversed() function.
    You may not use the copy() method for lists.
    You may not use the copy() method for strings.
    You may not use the copy() method for dictionaries.
    You may not use the copy() method for sets.
    You may not use the copy() method for tuples.

Example:

    print(polindron([1, 2, 3, 2, 1]))  # True
    print(polindron([1, 2, 3, 4, 5]))  # False
    print(polindron([1, 2, 3, 3, 2, 1]))  # True
    print(polindron([1, 2, 3, 4, 3, 2, 1]))  # True

'''





def polindron(l: list) -> bool:
    i_left = 0
    i_right = len(l) - 1
    while i_left < i_right:
        if l[i_left] != l[i_right]:
            return False
        i_left += 1
        i_right -= 1
    return True



print(polindron([1, 2, 3, 2, 1]))  # True
print(polindron([1, 2, 3, 4, 5]))  # False
print(polindron([1, 2, 3, 3, 2, 1]))  # True
print(polindron([1, 2, 3, 4, 3, 2, 1]))  # True
print(polindron([1, 2, 3, 4, 5, 6]))  # False
print(polindron([1, 2, 3, 4, 5, 6, 7]))  # False