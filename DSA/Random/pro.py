def answer(n, m, array, target):
    for i in range(n):
        for j in range(m):
            if array[i][j] == target:
                return True
    return False

n = int(input())
m = int(input())
array = []

for i in range(n):
    numbers = list(map(int, input().split()))
    array.append(numbers)

target = int(input())

if answer(n, m, array, target):
    print("true")
else:
    print("false")
