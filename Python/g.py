a = list(map(int, input("Enter credits: ").split()))  # List of credits
b = list(map(str, input("Enter grades: ").split()))   # List of grades
n = len(b)  # Number of subjects

# Grade to point mapping
grade_dict = {"S": 10, "A": 9, "B": 8, "C": 7, "D": 6, "E": 5 , "P":0}

total_points = 0  # To accumulate the sum of grade points * credits
total_credits = 0  # To accumulate the sum of credits

# Iterate over the subjects
for i in range(n):
    grade = b[i]
    credit = a[i]
    total_points += grade_dict[grade] * credit  # Calculate weighted grade points
    total_credits += credit  # Sum up credits

# Calculate CGPA
cgpa = total_points / total_credits if total_credits != 0 else 0

print(f"Your CGPA is: {cgpa:.2f}")
