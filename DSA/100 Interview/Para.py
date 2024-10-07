a=[1,2,1,4,4]
h=[]
for i in a:
    if i in h:
        h.remove(i)
    else:
        h.append(i)
print(h)        
