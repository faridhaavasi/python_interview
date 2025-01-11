'''
Given two strings s and t, write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: True

Example 2:
Input: s = "rat", t = "car"
Output: False

Note: You may assume the string contains only lowercase alphabets.

'''



def is_anagtam(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)