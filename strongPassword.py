#lengtOfString
lenstr = int(input())
#password
password = input()
#criteriaToFulfil
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
num = 0
lc = 0
uc = 0
sc = 0
tofulfill = 0
for i in range(len(password)):
    for j in range(len(numbers)):
        if(password[i] == numbers[j]):
            num = 1 
    for j in range(len(lower_case)):
        if(password[i] == lower_case[j]):
            lc = 1
    for j in range(len(upper_case)):
        if(password[i] == upper_case[j]):
            uc = 1
    for j in range(len(special_characters)):
        if(password[i] == special_characters[j]):
            sc = 1
#there are four conditions to fulfill after checking for length 6
tofulfill = 4 -(num +lc + uc + sc)
#checking for length of string
#if string length is greater than 6 but still has a condition to fulfill
if(lenstr>=6):
    print(tofulfill)
#if length is less than 6
else:
#if conditions are greater than 6 - length of password
    if(tofulfill>6-lenstr):
        print(tofulfill)
    else:
        print(6-lenstr)

