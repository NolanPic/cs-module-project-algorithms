'''
Input: an integer
Uses a cache to yeild a runtime of O(n) instead of O(3^n)
Returns: an integer
'''
def eating_cookies(n, cache=None):
    # base
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3: # three has 4 possible combinations, thus return 4
        return 4
    # if there is a value for n in the cache,
    # just use it
    if cache and cache[n] > 0:
        return cache[n]
    # there is no cache or n could not be found in it
    else:
        # there is no cache, create it
        if not cache:
            cache = {i: 0 for i in range(n+1)}
        # set the cache to the value of the recursive calls
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 1000

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
