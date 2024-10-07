def Twosum(ar,target):
    a={}
    for i,num1 in enumerate(ar):
        num2=target-num1
        if num2 in a:
            return a[num2],i
        a[num1]=i           
    return None    
ar=list(map(int,input().split()))
target=int(input())
result = Twosum(ar,target)
if result:
    print(result[0],result[1])
    