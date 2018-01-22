def LetterChanges(str)
 
  # code goes here
  alfabet = "abcdefghijklmnopqrstuvwxyz"
   
  lenOfStr = str.length
  chngStr=""
 
  for i in 0..lenOfStr-2
    letterInStr = str[i] 
    locInAlfabet = alfabet.index(letterInStr)
	incLocInAlfabet = locInAlfabet + 1
	if incLocInAlfabet == 26
		incLocInAlfabet = 0
	end
	
	if [0, 4, 8, 14, 20 ].include? incLocInAlfabet
		chngStr[i] = alfabet[incLocInAlfabet].upcase!
	else
		chngStr[i] = alfabet[incLocInAlfabet]
	end
		
  end
    
  return chngStr 
         
end
   
# keep this function call here    
puts LetterChanges(STDIN.gets)  