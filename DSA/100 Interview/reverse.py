def reverseString(s):
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        for i in range(n//2):
              s[i],s[n-i-1]=s[n-i-1],s[i]
        return s

s=["h","e","l","l","o"]
print(reverseString(s))
        