# Using the Ruby language, have the function LongestWord(sen) take the sen 
# arameter being passed and return the largest word in the string. 
# f there are two or more words that are the same length, return the first word 
# from the string with that length. Ignore punctuation and assume sen will not be empty. 

# Sample Test Cases
# Input:"fun&!! time"

# Output:"time"


# Input:"I love dogs"

# Output:"love"

def LongestWord(sen)

  myArray = sen.split
  wordLength = 0
  for aWord in myArray
  		if aWord.length > wordLength
  		   myWord = aWord
  		   wordLength = aWord.length
  		end
  end

  return myWord
         
end

# keep this function call here    
puts LongestWord(STDIN.gets)