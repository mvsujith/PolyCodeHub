# Read the input
N = int(input().strip()) # Number of students and eggs in each tray
random_numbers = list(map(int, input().strip().split()))

# Create a dictionary to count occurrences of each random number
group_count = {}
for num in random_numbers:

if num in group_count:

group_count[num] += 1
else:
group_count [num] = 1


 # Calculate the number of eggs left for each student
eggs_left = []

for num in random_numbers:

group_size = group_count[num] eggs_left.append(N group_size)
# Print the result as a single line with spaces
print(''.join(map(str, eggs_left)))