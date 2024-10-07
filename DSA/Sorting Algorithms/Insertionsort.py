n = list(map(int,input().split()))
a = len(n)

def insertionsort(n,a):

    for i in range(a):
        
        minposition=i
        for j in range(i,a):
            if n[j]<n[i]:
                
