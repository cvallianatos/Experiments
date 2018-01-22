# Challenge
# Using the Ruby language, have the function KaprekarsConstant(num) take the num parameter being passed which will be a 4-digit number with at least two distinct digits. Your program should perform the following routine on the number: Arrange the digits in descending order and in ascending order (adding zeroes to fit it to a 4-digit number), and subtract the smaller number from the bigger number. Then repeat the previous step. Performing this routine will always cause you to reach a fixed number: 6174. Then performing the routine on 6174 will always give you 6174 (7641 - 1467 = 6174). Your program should return the number of times this routine must be performed until 6174 is reached. For example: if num is 3524 your program should return 3 because of the following steps: (1) 5432 - 2345 = 3087, (2) 8730 - 0378 = 8352, (3) 8532 - 2358 = 6174. 

# Hard challenges are worth 15 points and you are not timed for them.
# Sample Test Cases
# Input:2111
# Output:5

# Input:9831
# Output:7

def ProcessKaprekarsConstant(num)

  w = num + "0000"
  q = w.slice(0,4)
  a = q.split(//).sort
  b = a.reverse
  
  c = a.join
  d = b.join
  
  x = c.to_i
  y = d.to_i
  
  if x > y
	result = x-y
  else
	result = y-x
  end
  
  return result.to_s
         
end

def KaprekarsConstant(num)
	target = "6174"
	counter = 0
	outcome = num
	while outcome != target
		outcome = ProcessKaprekarsConstant(outcome)
		counter = counter + 1
	end
	return counter
end
   
# keep this function call here    
puts KaprekarsConstant(STDIN.gets)  