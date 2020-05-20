'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # outer loop
    for i in range(len(arr)):
        # declare variable for if a number is found twice
        found_twice = False
        # loop thru array for every item in array
        for j in range(len(arr)):
            # if we aren't looking at the same index (same item)
            # and the value is the same, the item was found
            if i != j and arr[i] == arr[j]:
                found_twice = True
        # if the value was not found twice, return that value
        if not found_twice:
            return arr[i]
    
    return -1


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")