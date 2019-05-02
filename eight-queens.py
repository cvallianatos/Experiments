def printBoard(strArr):
    n = len(strArr)
    for i in range(n):
        print(strArr[i])

x = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

printBoard(x)
print ("-----------------")

for j in range(8):
    for i in range(8):
        x[i] = [0,0,0,0,0,0,0,0]
        x[i][j] = 1
        printBoard(x)
        print ("-----------------")
    print ("***************************")
