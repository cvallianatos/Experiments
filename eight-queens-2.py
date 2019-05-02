def evaluateTopSouthWest(strArr):
    for i in range(8):
        sum = 0
        for j in range(i+1):
            sum = sum + int(strArr[i-j][j])
        if sum > 1:
            return False
    return True

def evaluateBottomSouthWest(strArr):
    for j in range(8,15):
        sum = 0
        for i in range(j-7,8):
            sum = sum + int(strArr[i][j-i])
        if sum > 1:
            return False
    return True

def evaluateTopSouthEast(strArr):
    for j in range(8):
        sum = 0
        for i in range(0,8-j):
            sum = sum + int(strArr[i][j+i])
        if sum > 1:
            return False
    return True

def evaluateBottomSouthEast(strArr):
    for i in range(1,8):
        sum = 0
        for j in range(i,8):
            sum = sum + int(strArr[j][j-i])
        if sum > 1:
            return False
    return True         
    
def generateBoards():
    code = [1,2,4,8,16,32,64,128]

    k = 0

    for row1 in code:
        for row2 in [x for x in code if x != row1]:
            for row3 in [x for x in code if (x != row2) and (x != row1)]:
                for row4 in [x for x in code if (x != row3) and (x != row2) and (x != row1)]:
                    for row5 in [x for x in code if (x != row4) and (x != row3) and (x != row2) and (x != row1)]:
                        for row6 in [x for x in code if (x != row5) and (x != row4) and (x != row3) and (x != row2) and (x != row1)]:
                            for row7 in [x for x in code if (x != row6) and (x != row5) and (x != row4) and (x != row3) and (x != row2) and (x != row1)]:
                                for row8 in [x for x in code if (x != row7) and (x != row6) and (x != row5) and (x != row4) and (x != row3) and (x != row2) and (x != row1)]:
                                    a = []
                                    a.append (str(bin(row8)[2:]).rjust(8, '0'))
                                    a.append (str(bin(row7)[2:]).rjust(8, '0'))
                                    a.append (str(bin(row6)[2:]).rjust(8, '0'))
                                    a.append (str(bin(row5)[2:]).rjust(8, '0'))
                                    a.append (str(bin(row4)[2:]).rjust(8, '0'))
                                    a.append (str(bin(row3)[2:]).rjust(8, '0'))
                                    a.append (str(bin(row2)[2:]).rjust(8, '0'))
                                    a.append (str(bin(row1)[2:]).rjust(8, '0'))
                                    if (evaluateTopSouthEast(a) and evaluateBottomSouthEast(a) and evaluateTopSouthWest(a) and evaluateBottomSouthWest(a)):
                                        k = k + 1
                                        print ("Board: ",k)
                                        printBoard(a)
                                        print("------------------------")
                                  
def printBoard(strArr):
    n = len(strArr)
    for i in range(n):
        print(strArr[i])

generateBoards()