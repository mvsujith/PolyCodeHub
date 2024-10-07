class UserMainCode(object):
    @classmethod
    def removeOccurrence(cls, input1, input2):
        # Dictionary to count occurrences of each character in the string
        char_count = {}
        for char in input2:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # Get the counts of characters sorted in descending order
        char_counts = sorted(char_count.values(), reverse=True)

        # Perform up to 3 operations to remove the most frequent characters
        operations = min(3, len(char_counts))
        for i in range(operations):
            input1 -= char_counts[i]

        # Return the minimum possible length of the string
        return input1

# Taking user input directly without prompts
input_values = input().split()  # Takes input in one line, split into a list
input1 = int(input_values[0])  # First input as integer (length of the string)
input2 = input_values[1]       # Second input as the string

# Calling the method and printing the result
result = UserMainCode.removeOccurrence(input1, input2)
print(result)
