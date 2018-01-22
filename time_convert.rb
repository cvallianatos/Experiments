# Using the Ruby language, have the function TimeConvert(num) take the num parameter being passed
# and return the number of hours and minutes the parameter converts to (ie. if num = 63 then the
# output should be 1:3). Separate the number of hours and minutes with a colon. 

# Sample Test Cases
# Input:126
# Output:"2:6"

# Input:45
# Output:"0:45"

def TimeConvert(str)

  inTime = str.to_i
  hrs = inTime / 60
  mins = inTime - (hrs * 60)
  
  return hrs.to_s + ":" + mins.to_s
         
end
   
# keep this function call here    
puts TimeConvert(STDIN.gets)