# Given an array of integers, return a new array with each value doubled.

def maps(a):
    doubled = [number * 2 for number in a]
    return doubled

print(maps([1, 2, 3]))
print(maps([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(maps([]))