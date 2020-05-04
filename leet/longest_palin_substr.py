class Solution:
    def longestPalindrome(self, s: str) -> str:
        all_substrs = [s[i:j] for i in range(0, len(s)) for j in range(i + 1, len(s) + 1)]
        longest = ''
        length = 0
        for substr in all_substrs:
            sub_len = len(substr)
            if sub_len > length and self.is_palin(substr):
                longest = substr
                length = sub_len

        return longest

    def is_palin(self, st):
        if (st[::-1] == st):
            return True
        return False


a = Solution()

print(a.longestPalindrome("aaabbbaaaabsdfaabbaaaacccccdddccc"))
