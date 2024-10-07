def missing(a):
    a.sort()

    for i in range(0,len(a)):
        if a[i]+1==a[i+1]:
            pass
        else:
            return a[i]+1
a=[3,0,1]        
print(missing(a))
