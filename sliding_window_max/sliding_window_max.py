'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers


    1. Create an array max_upto and a stack to store indices. Push 0 in the stack.
    2. Run a loop from index 1 to index n-1.
    3. Pop all the indices from the stack, which elements (array[s.top()]) is less than the current element and update max_upto[s.top()] = i – 1 and then insert i in the stack.
    4. Pop all the indices from the stack and assign max_upto[s.top()] = n – 1.
    5. Create a variable j = 0
    6. Run a loop from 0 to n – k, loop counter is i
    7. Run a nested loop until j < i or max_upto[j] < i + k – 1, increment j in every iteration.
    8. Print the jth array element.


'''

def sliding_window_max(nums, k):

# Variables
    result = []
    # Stores index up to the max element
    max_upto = [0] * len(nums)
    # Update array as if your finding the next greater element
    s = [0]
    j = 0


# Loops
    for i in range(1, len(nums)):
        while (len(s) > 0 and nums[s[-1]] < nums[i]):
            max_upto[s[-1]] = i - 1
            del s[-1]
        
        s.append(i)
    
    # print("S: ", s)
    
    while (len(s) > 0):
        max_upto[s[-1]] = len(nums) - 1
        del s[-1]
    
    # Check to see if next element (j) in inside the window
    for i in range(len(nums) - k + 1):
        while (j < i or max_upto[j] < i + k - 1):
            j += 1
        
        result.append(nums[j])
    
    # print("Result: ", result)
    
    return result

    

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
