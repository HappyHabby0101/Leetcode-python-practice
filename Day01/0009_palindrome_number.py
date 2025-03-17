class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

# 測試
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))  # Output: True
