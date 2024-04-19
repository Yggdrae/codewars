# Given a non-negative integer, 3 for example, return a string with a murmur: 
# "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

# Meu:
def count_sheeps(n):
    sheep = ''
    i=0
    while(i<n):
        sheep += str(i+1) + " sheep..."
        i+=1
    return sheep

# Simplificado:
def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))

print(count_sheep(0))
print(count_sheep(1))
print(count_sheep(2))
print(count_sheep(3))