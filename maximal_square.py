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

def ConstructSquare(strArr,squareSize):
    return True

def ValidateSquare(origin, size):
    
    # This function takes an origin point and a size and determines if the submitted square is valid. That is if it is 
    # composed by all 1's
    # It returns True if it is valid or False if it is not

    return True 

def MaximalSquare(strArr): 

    # code goes here 
    return strArr
    
# keep this function call here  
#print(MaximalSquare(input()))

a=[[0,1,1,1,0],[1,1,1,1,0],[1,1,0,0,0],[0,1,0,1,1],[1,1,0,0,1]]

inputLength = len(a)

# dimension of input matrix is n = len(a) + 1 

n = len(a) 

for i in range(inputLength):
    for j in range(inputLength):
        print(a[i][j],end='')
    print("\n")


for i in range(2,n+1):
    print("There are ", ((n-i)+1)**2, " squares of ", i, " edges")
