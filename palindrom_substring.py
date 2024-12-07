#find all substring palindroms. 
def find_all_palindromic_substring(s):
    result = []
    
    def expand_around_corner(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            result.append(s[left: right + 1])
            left -= 1
            right += 1
    
    for i in range(len(s)):
        #odd length palindromes
        expand_around_corner(i, i)

        #event lenth palindroms
        expand_around_corner(i, i + 1)


def  find_all_palindrom(s):
    result = []

    def outward(left, right):
        while left >= 0 and right <= len(s) and s[left] == s[right]:
            result.append(s[left:right+1])
            left -= 1
            right += 1
    
    for i in range(len(s)):
        outward(i, i)
        outward(i, i + 1)
