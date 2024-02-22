print("Please enter a string: ")
astring = input()
length = len(astring)
newstring = ""
for i in range(0,length):
    if i % 2 == 0:
        newstring += astring[i].upper()
    elif i % 2 != 0:
        newstring += astring[i].lower()
print(newstring)

print("Please enter another string: ")
astring = input()
length = len(astring)
wordlist = astring.split()
for i in range(0,len(wordlist)):
    if i % 2 == 0:
        wordlist[i] = wordlist[i].lower()
    elif i % 2 != 0:
        wordlist[i] = wordlist[i].upper()
newstring = " ".join(wordlist)
print(newstring)