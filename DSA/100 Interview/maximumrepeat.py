def maximumrepeat(a):
    b=[]
    c={}
    for i in range(0,len(a)):
        if a[i] in c:
            c[a[i]]=c[a[i]]+1
        else:
            c.setdefault(a[i],1)
    d=max(c.values())
    for i,j in c.items():
        if j==d:
            return i      

a=[1,2,1,3,2,2,3]
print(maximumrepeat(a))           


"""counter"""