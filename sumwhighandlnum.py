# Task
# Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

# The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

# Mind the input validation.

# Input validation
# If an empty value ( null, None, Nothing etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0.

def sum_array(arr):
    if not arr:
        return 0
    if len(arr) == 1 or len(arr) == 2:
        return 0
    high = arr[0]
    low = arr[0]
    sumarr = 0
    for x in arr:
        if x > high:
            high = x
        if x < low:
            low = x
        sumarr += x
    sumarr = sumarr - high - low
    print(low, high)
    return sumarr

print (sum_array([6, 2, 1, 8, 10]))
print (sum_array([-6, -20, -1, -10, -12]))