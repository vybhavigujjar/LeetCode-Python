class Solution:
    def isPalindrome(self,x):
        word = str(x)
        reverse_word = word[::-1]
        return word == reverse_word
        