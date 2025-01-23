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