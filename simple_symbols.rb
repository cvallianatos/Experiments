# Using the Ruby language, have the function SimpleSymbols(str) take the str parameter being passed
# and determine if it is an acceptable sequence by either returning the string true or false. The str
# parameter will be composed of + and = symbols with several letters between them
# (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol.
# So the string to the left would be false. The string will not be empty and will have at least one
# letter. 

def all_letters(str)
    # Use 'str[/[a-zA-Z]*/] == str' to let all_letters
    # yield true for the empty string
    str[/[a-zA-Z]+/]  == str
end

def SimpleSymbols(str)

  numOfChars = str.length
  assess = false
  for i in 1..numOfChars -3
    if all_letters(str[i])
		if str[i-1] == "+" and str[i+1] == "+"
			assess = true
		else
			assess = false
		end
	end
  end
  
  return assess
         
end
   
# keep this function call here    
puts SimpleSymbols(STDIN.gets)