'''
Input: a List of integers
Returns: a List of integers
'''
# runs in O(n)
def moving_zeroes(arr):
    # the beginning of the array
    left = 0
    # the end of the array
    right = len(arr) -1
    # while the left and right sides have not met,
    while left <= right:
        # if the left is a zero and the right is not:
        if arr[left] == 0 and arr[right] != 0:
            # swap
            arr[left], arr[right] = arr[right], arr[left]
            # narrow down the array, from both sides in
            left +=1
            right -=1
        else:
            # keep the left from moving on unless
            # it is not a zero, and the right from
            # moving on unless it IS zero--this is
            # the same effect as moving_zeroes_old
            # has when it decrements i by i to 
            # move back
            if arr[left] != 0:
                left += 1
            if arr[right] == 0:
                right -=1
    return arr

def moving_zeroes_old(arr):
    # loop thru the array, and while the value on the current
    # value's LEFT is zero, swap
    
    # the index of the current item being considered
    i = 0
    while i < len(arr):
        # skip the first element, since it won't have
        # anything before it
        if i != 0:
            
            # get the previous element, if it exists
            prev = None
            if i-1 != -1:
                prev = arr[i-1]
            # while the previous item is zero, and
            # the current item is not, swap
            while prev == 0 and arr[i] != 0:
                # swap
                arr[i-1], arr[i] = arr[i], arr[i-1]
                # if we are in a situation like this:
                # [1, 0, 0, 2]
                #           ^
                # then we need to swap:
                # [1, 0, 2, 0]
                # but the two still needs to be moved to
                # the left again, so the index must be decremented:
                # [1, 0, 2, 0]
                #        ^
                # ...then the next iteration in this while will move
                # the two again: [1, 2, 0, 0]
                i -=1
                # update the previous as well
                if i-1 != -1:
                    prev = arr[i-1]
        i +=1
    
    return arr
            

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print('is it an infinate loop?')
    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
    print(f"The resulting of moving_zeroes_ntime is: {moving_zeros_ntime(arr)}")
    print("No, you're all good!")