print("Please enter a sentence: ")
str_manip = input()
length = len(str_manip)
print('Length: ' + str(length))
lastletter = str_manip[-1]
str_2 = str_manip.replace(lastletter,"@")
print(str_2)
str_3 = str_manip[-1:-4:-1]
print(str_3)
str_4 = str_manip[0:3] 
str_5 = str_manip[-2:]
str_6 = str_4 + str_5
print(str_6)