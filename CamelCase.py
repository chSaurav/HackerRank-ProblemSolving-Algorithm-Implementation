#takingInputOfaString
s = input()
#taking first word as 1
count = 1
for i in range(len(s)):
    if(s[i].isupper() == True):
        count += 1
#printing total words     
print(count)
