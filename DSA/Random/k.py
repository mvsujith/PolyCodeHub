from collections import deque

def max_sliding_window(nums, k):
    if not nums or k == 0:
        return []
    
    window = deque()
    result = []

    for i, num in enumerate(nums):
        # Remove indices that are out of the current window
        if window and window[0] <= i - k:
            window.popleft()
        
        # Remove elements that are smaller than the current element
        while window and nums[window[-1]] <= num:
            window.pop()
        
        # Add the current element at the end of the deque
        window.append(i)
        
        # Append the current maximum to the result (starts when we have a full window)
        if i >= k - 1:
            result.append(nums[window[0]])
    
    return result

# Input: Take inputs from the user
n = int(input())  # Number of elements in the array
nums = list(map(int, input().split()))  # Array of integers
k = int(input())  # Window size

# Output: Print the max sliding window values as space-separated integers
print(" ".join(map(str, max_sliding_window(nums, k))))
