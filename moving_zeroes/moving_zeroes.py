'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # loop thru the array, and while the value on the current
    # value's RIGHT is zero, swap
    for i in range(len(arr)):
        # make sure we are not at the start of the array--
        # can't swap at this point
        if i is not 0:
            # while the previous item is zero, swap
            prev = arr[i-1]
            while prev is 0 and arr[i] is not 0:
                arr[i], arr[i-1] = arr[i-1], arr[i]
    return arr
            

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    # [0, 3, 1, 0, -2]
    # [3, 1, 0, -2, 0]

    print('is it an infinate loop?')
    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
    print("No, you're all good!")