# return the int representation of string s
def stringToInt(s):
	result = 0
	power = 1
	sign = 1 - 2*('-' == s[0])
	if sign == -1:
		s = s[1:]
	for c in reversed(s):
		result += (ord(c)-ord('0'))*power
		power *= 10
	return result*sign		
