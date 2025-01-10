'''
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "hello", needle = "a"
Output: -1

Example 3:
Input: haystack = "hello", needle = ""
Output: 0

Constraints:
0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.
'''


def strStr(s, x):
    if x == "":
        return 0
    if x in s:
        return s.index(x)
    else:
        return -1
    
def strStr2(s, x):
    n = len(s)
    for i in range(n):
        if x == '':
            return 0
        if s[i:i+len(x)] == x:
            return i
    return -1


print(strStr('hello', 'll'))
print(strStr2('hello', 'll'))


print(strStr('hello', ''))
print(strStr2('hello', ''))


print(strStr('hello', 'l'))
print(strStr2('hello', 'l'))

print(strStr('hello', 'o'))
print(strStr2('hello', 'o'))

print(strStr('hello', 'a'))
print(strStr2('hello', 'a'))

print(strStr('hello', 'hello'))
print(strStr2('hello', 'hello'))

print(strStr('hello', 'helloo'))
print(strStr2('hello', 'helloo'))

print(strStr('hello', 'hellooo'))
print(strStr2('hello', 'hellooo'))
