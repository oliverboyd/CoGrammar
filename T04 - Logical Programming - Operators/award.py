print("Time taken for swimming: ")
swimming = int(input())
print("Time taken for cycling: ")
cycling = int(input())
print("Time taken for running: ")
running = int(input())
sum = swimming + cycling + running
print("Total time taken: " + str(sum))
if sum <= 100:
    print("Provincial Colours")
elif 101 <= sum <= 105:
    print("Provincial Half Colours")
elif 106 <= sum <= 110:
    print("Provincial Scroll")
elif sum >= 111:
    print("No award")
