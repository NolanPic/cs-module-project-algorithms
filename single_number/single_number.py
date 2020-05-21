'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# O(n^2)
def single_number_array(arr):
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


# O(n)
def single_number(nums):
    # store each single number found (there should only be one)
    single_counts = {}
    
    for x in nums: # O(n)
        if x in single_counts: # O(1)
            # if x is already in single_counts, that means
            # it is not actually a single num--thus delete it
            del single_counts[x]
        else:
            # this num has only been found once so far
            single_counts[x] = 1
            
    # single_counts will only contain one key, but we still have
    # to loop through it to get to it. The loop will be O(1)
    # because there will always only ever be 1 key
    for number in single_counts:
        return number
        


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")