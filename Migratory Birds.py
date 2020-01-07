

Question  : Migratory Birds

solution : 

#function
def migratoryBirds(birds):
    count = [0,0,0,0,0,0]
    for i in birds :
        count[i] += 1
    return (count.index(max(count)))
#driverCode
n = int(input("")) #numbers of bird of every type that is seen
birds = list(map(int,input().split(" ")))
result = migratoryBirds(birds)
print(result)
