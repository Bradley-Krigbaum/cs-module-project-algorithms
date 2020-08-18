'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    mute_arr = []
    negative_arr = []
    zero_arr = []

    for i in arr:
        if i == 0:
            zero_arr.append(i)
            # print("ZERO: ", zero_arr)
        elif i < 0:
            negative_arr.append(i)
            # print("NEGATIVE: ", negative_arr)
        else:
            mute_arr.append(i)
            # print("MUTE: ", mute_arr)
    
    mute_arr.extend(negative_arr)
    mute_arr.extend(zero_arr)

    print(mute_arr)

    return mute_arr
    # [0], mute_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")