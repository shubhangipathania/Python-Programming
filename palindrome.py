def palindrome(s):
    def solve(left,right):

        if left >= right:
            return True
        
        if s[left] != s[right]:
            return False
        return solve(left +1, right-1)
    return solve(0, len(s) -1)

print(palindrome("madam"))




