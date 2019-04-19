# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two 
# abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as 
# the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that
# the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def isAbundant(num)
	sumDiv = 0
	for i in 1..num.div(2)
		z = num.remainder(i)
		if z == 0
			sumDiv = sumDiv + i
#			print i, " "
		end
	end
#	print "Sum = ", sumDiv, " "
	if num == sumDiv
#		print "ABUNDAND NUMBER"
		return true
	else
		return false
	end
#	print "\n"
end

endNum = 28123

sum = 0
   

#for x in 25..endNum
#	if isAbundant(x)
#		print x,  "\n"
#	end
#end


for x in 25..endNum
	sum = sum + x
end

num1 = 28
num2 = 496
num3 = 8128

myList =[524, 8156, 8624]

mySum = 17304



print "RESULT IS: ", sum - mySum, "\n"