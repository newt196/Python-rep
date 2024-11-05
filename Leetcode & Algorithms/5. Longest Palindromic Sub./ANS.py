class Solution:
    def longestPalindrome(self, s: str) -> str:
        print(s)
        rev = s[::-1]
        n=len(s)
        print(n)
        longest_palindrome = ""


        for i in range(n):
            for j in range(i,n):
                substring_s = s[i:j+1]
                substring_rev = rev[n-j-1:n-1]

                if substring_s == substring_rev and len(substring_s) > len(longest_palindrome):
                    longest_palindrome = substring_s
        return longest_palindrome
sol = Solution()


