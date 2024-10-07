def palindrome (a):
    for i in a:
        if i.isalnum():
            b.append(i)
    result="".join(b).lower()


    return result==result[::-1]


b=[]
a="0p"
print(palindrome(a))