# Function to check if Chef will finish watching the episode before the exam starts
def can_finish_episode(x):
    if x >= 24:
        return "YES"
    else:
        return "NO"

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the time until the exam starts
    x = int(input())
    
    # Check if Chef will finish watching the episode
    result = can_finish_episode(x)
    
    # Print the result
    print(result)
