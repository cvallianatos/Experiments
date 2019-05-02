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
    for i in range(n):
        for j in range(n):
            product = 1
            for k in range(squareSize):
                for l in range(squareSize):
                    product = product * x[i+k][j+l]
                    #print(x[i+k][j+l], end='')
                #print()
            #print("Product is: ", product)
            #print("========")
            if (product == 1):
                return True
                break
        #print('**************')

    return False

def MaximalSquare(strArr): 

    # code goes here 
    return 1

def PrintMatrix(strArr):
# dimension of input matrix is n = len(a) + 1 
    n = len(strArr) 

    for i in range(n):
        for j in range(n):
            print(strArr[i][j],end='')
        print()

def MatrixStats(strArr):
    n = len(strArr) 

    for i in range(2,n+1):
        print("There are ", ((n-i)+1)**2, " squares of ", i, " edges")

# keep this function call here  
#print(MaximalSquare(input()))

a=[[0,1,1,1,0,1],[1,1,1,1,0,0],[1,1,0,0,0,1],[0,1,0,1,1,0],[1,1,0,1,1,1],[1,1,0,0,1,1]]
#a=[['a','b','c','d','e','f'],['g','h','i','j','k','l'],['m','n','o','p','q','r'],['s','t','u','v','w','x'],['y','z','A','B','C','D'],['E','F','G','H','I','J']]


n = len(a) 
print()
PrintMatrix(a)
print()
MatrixStats(a)
print()

maxSquare = 1
for z in range(2,n+1):
    if (ConstructSquare(a,z)):
        maxSquare = z
        print("The Max Square is: ", maxSquare)   