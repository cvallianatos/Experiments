'''
Have the function MaximalSquare(strArr) take the strArr parameter being passed which will be a 2D matrix of 0 and 1's,
and determine the area of the largest square submatrix that contains all 1's. A square submatrix is one of equal width 
and height, and your program should return the area of the largest submatrix that contains only 1's. 
For example: if strArr is ["10100", "10111", "11111", "10010"] then this looks like the following matrix: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0 

For the input above, you can see the bolded 1's create the largest square submatrix of size 2x2, so your 
program should return the area which is 4. You can assume the input will not be empty. 

Hard challenges are worth 15 points and you are not timed for them.
Sample Test Cases
Input:["0111", "1111", "1111", "1111"]

0 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1

Output:9

Input:["0111", "1101", "0111"]

0 1 1 1 
1 1 0 1 
0 1 1 1

Output:1

'''

def ConstructSquare(x,squareSize):
    n = len(x)-(squareSize-1)
    m = len(x[0]) - (squareSize-1)
    for i in range(n):
        for j in range(m):
            product = 1
            for k in range(squareSize):
                for l in range(squareSize):
                    product = product * int(x[i+k][j+l])
            if (product == 1):
                return True
                break
    return False

def MaximalSquare(strArr): 
    n = len(strArr) 
    maxSquare = 1
    for z in range(2,n+1):
        if (ConstructSquare(strArr,z)):
            maxSquare = z
    return maxSquare * maxSquare

# keep this function call here  

#a=[[0,1,1,1,0,1],[1,1,1,1,0,0],[1,1,0,0,0,1],[0,1,0,1,1,0],[1,1,0,1,1,1],[1,1,0,0,1,1]]
#a=["01001", "11111", "01011", "11011"] 
#a=["01001", "11111", "01011", "11111", "01111", "11111"]
a=["101101", "111111", "010111", "111111"]
print(MaximalSquare(a))