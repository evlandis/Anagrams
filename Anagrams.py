firstWord=input("Enter a string: ")
secondWord=input("Enter a string: ")
firstWordList=[]
secondWordList=[]
for letter in firstWord:
    if ord(letter)>=65 and ord(letter)<=90:
        letter=chr(ord(letter)+32)
    if ord(letter)!=ord(" ") and ord(letter)>=97 and ord(letter)<=122 and ord(letter)>=48 and ord(letter)<=57:
        firstWordList.append(letter)
for letter in secondWord:
    if ord(letter)>=65 and ord(letter)<=90:
        letter=chr(ord(letter)+32)
    if ord(letter)!=ord(" ") and ord(letter)>=97 and ord(letter)<=122 and ord(letter)>=48 and ord(letter)<=57:
        secondWordList.append(letter)
firstWordList.sort()
secondWordList.sort()
if len(firstWordList)==len(secondWordList):
    if firstWordList==secondWordList:
        print("They are anagrams")
    else:
        print("They are not anagrams")
