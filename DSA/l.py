def product(num):
    arr=[]
    for i in num:
        a=1
        for j in num:
            if i==0 and j!=0:
                a=j*a
                break
            a=j*a    
        if i!=0:    
           k=a/i
        arr.append(k) 
    return arr
num=list(map(int,input().split()))
result=product(num)
print(result)

        


