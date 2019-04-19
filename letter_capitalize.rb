def LetterCapitalize(str)

  wordsInStr = str.split
  numOfWords = wordsInStr.length
  retStr=""
  
  for i in 0..numOfWords - 1
    a = wordsInStr[i]
    
    retStr = retStr +  " " + a.capitalize
  end
  
  return retStr
         
end
   
# keep this function call here    
puts LetterCapitalize(STDIN.gets)