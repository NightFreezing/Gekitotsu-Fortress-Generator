#setting
import random
totalMoney = 1500
priceMap = {
    "r": 5,
    "v": 10,
    "p": 15,
    "L": 20,
    "1": 30, "3": 30, "7": 30, "8": 30, "a": 30,
    "q": 40, "T": 40,
    "5": 50, "d": 50, "U": 50, "G": 50,
    "4": 60, "x": 60, "A": 60, "C": 60, "D": 60, "E": 60, "Y": 60,
    "2": 70, "9": 70, "b": 70, "c": 70, "e": 70, "f": 70, "w": 70, "z": 70, "B": 70, "I": 70,
    "g": 80, "W": 80, "V": 80,
    "o": 90,
    "h": 100, "i": 100, "n": 100, "s": 100, "t": 100, "O": 100,
    "j": 150, "k": 150, "l": 150, "F": 150, "H": 150, "K": 150, "J": 150, "M": 150, "R": 150,
    "6": 200, "m": 200, "y": 200, "N": 200, "P": 200, "Q": 200, "S": 200, "X": 200,
    "u": 250
}
strings = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
fortressInfo = []
coreVar = []
unitVar = []
code = ''

def decToBase62(n):
    result = []
    while n > 0:
        n, remainder = divmod(n,61)
        result.append(strings[remainder])
    return ''.join(reversed(result))

#generation
remainingMoney = totalMoney
coreId = strings[random.randint(0,61)]
coreX = random.randint(0,276)
coreY = random.randint(0,276)
coreAngle = random.randint(0,359)
coreVar = [coreId, coreX, coreY, coreAngle]
if coreId =='1':
    remainingMoney -= 750
fortressInfo.append(coreVar)
while remainingMoney > 0:
    unitId = strings[random.randint(1,60)]
    if remainingMoney >= priceMap[unitId]:
       remainingMoney -= priceMap[unitId]
       unitX = random.randint(0,348)
       unitY = random.randint(0,349)
       unitAngle = random.randint(0,359)
       unitVar = [unitId, unitX, unitY, unitAngle]
       fortressInfo.append(unitVar)
code = coreVar[0] + decToBase62(52058 + 1000 * coreVar[1] + coreVar[2] + 1000000 * coreVar[3]).zfill(5)
for i in range(1,len(fortressInfo)):
    code += fortressInfo[i][0] + decToBase62(16020 + 1000 * fortressInfo[i][1] + fortressInfo[i][2] + 1000000 * fortressInfo[i][3]).zfill(5)
print(code)
