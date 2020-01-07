#function
def socksMerchant(socks):
    totalPair = 0
    for val in socks :
        total = 0 
        for i in range(0,len(socks)):
                if val == socks[i]:
                    total = total + 1
        pair = int(total / 2)
        totalPair += pair
    return (totalPair)


#driverCode
n  = int(input("")) #number of socks in the pile
socks = list(map(int, input().split(" ")))
result = socksMerchant(socks)
print(result)
