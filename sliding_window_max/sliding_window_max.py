'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # start by looping through nums (i for nums)
    # next, loop from i to i+k to get window
    # next, find the largest item in that range
    # append to an array
    max_nums = []
    for i in range(len(nums)):
        # set the maximum number to negative infinity
        # so that it will always be overwritten, even
        # if there are negative numbers in the array
        max_num = float("-inf")
        for j in range(i, i+k):
            # ensure we are not at the end of the array
            if j < len(nums):
                # find the max num in this set
                if nums[j] > max_num:
                    max_num = nums[j]
            else:
                # we are at the end of the array
                break
        # max_num will now be the largest item. Append
        max_nums.append(max_num)
        if j == len(nums)-1: 
            # while the outer loop (i) has not finished,
            # j has successfully counted up to the end of
            # the array, and therefore we need to break out
            # of the i loop
            break  

    return max_nums


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
