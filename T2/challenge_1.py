import math
side1 = float(input())
side2 = float(input())
side3 = float(input())
s = (side1 + side2 + side3)/2
area = math.sqrt(s*(s - side1)*(s - side2)*(s - side3))
print(area)