class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False

        y = 0
        while y < x:
            y = 10 * y + x % 10
            x //= 10

        if y > x:
            y //= 10

        return x == y

# Time: O(log_10(x))
# Space: O(1)
