def hello(n):
    added = n  
    while True:  
        reversed_number = reverse(added)  
        added = added + reversed_number  
        if str(added) == str(added)[::-1]:  
            print(added)
            break

def reverse(n):
    return int(str(n)[::-1])  

n = int(input("Enter a number: "))
hello(n)
