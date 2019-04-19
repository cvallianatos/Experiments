'''
Challenge
Have the function TimeConvert(num) take the num parameter being passed and return the number of hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3). Separate the number of hours and minutes with a colon. 
Sample Test Cases
Input:126
Output:2:6

Input:45
Output:0:45

'''

def TimeConvert(num): 

    hours = num // 60
    mins = num - (hours * 60)
    ans = str(hours) + ":" + str(mins)
    return ans
    
# keep this function call here  
g = input("Enter number minutes: ") 
print(TimeConvert(int(g)))