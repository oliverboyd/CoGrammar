# I have solved this as a function called star of n. The desired output is then star(5)
def star(n):
    x = "*"
    y = "*"
    for i in range(0,2*n-1):
        print(y)
        if i < (n-1):
            y = y + x
        else: y = y[0:len(y)-1]
star(5)