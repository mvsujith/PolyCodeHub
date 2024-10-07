from collections import deque
def dict(a):

    b={"}":"{",")":"(","]":"["}

    stack=deque()
    for i in a:
        if stack and stack[-1]==b.get(i):
            stack.pop()
        
        else:
            stack.append(i)

    if stack:
        return "false"
    else:
        return "true"    



a="(]"
print(dict(a))

"""class Solution:
    def isValid(self, s: str) -> bool:
        b={"}":"{",")":"(","]":"["}
        st=[]
        for i in s:
            if len(st)>0 and st[-1]==b.get(i):
                st.pop()
        
            else:
                st.append(i)

        if st:
            return False
        else:
            return True   """