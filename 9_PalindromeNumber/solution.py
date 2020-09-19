class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        digits = 0
        y = x
        while y:
            digits += 1
            y //= 10

        while digits > 1:
            if x // (10**(digits-1)) != (x % 10):
                return False

            x = (x % 10**(digits-1)) // 10
            digits -= 2
            
        return True

# Time: O(log_10(x))
# Space: O(1)
