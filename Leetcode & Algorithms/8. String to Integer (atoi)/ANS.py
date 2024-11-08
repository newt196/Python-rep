class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  
        
        
        sub = 1  
        if s and s[0] == '-':
            sub = -1
            s = s[1:]
        elif s and s[0] == '+':
            s = s[1:]

        tran = ''
        for char in s:
            if char.isdigit():
                tran += char
            else:
                break  #

        if tran:
            result = sub * int(tran)
        else:
            result = 0  

        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result
