class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed = 0
        temp = x

        while temp != 0: #121!=0
            digit = temp % 10  
            reversed= reversed* 10 + digit
            temp //= 10   #121//10=1

        return reversed== x