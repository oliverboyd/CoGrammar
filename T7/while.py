x = 0
sum = 0
f = 0
while x != -1:
    x = int(input())
    sum = sum + x
    f = f + 1
print((sum+1)/(f-1)) # we are adding 1 to the sum to account for the -1 which was added to the sum in the final iteration. For similar reasons we divide by f-1 instead of f.
