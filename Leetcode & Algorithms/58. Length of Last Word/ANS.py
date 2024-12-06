class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        help = ""
        length = len(s)
        for i in range(length - 1, -1, -1):  
            if s[i] == " ":
                if help:  
                    break
            else:
                help += s[i]
        return len(help)
