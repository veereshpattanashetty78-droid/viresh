def palindrome(s):
    s = ''.join(s.split()).lower()
    return s == s[::-1]
print(palindrome("No lemon, no melon"))    



