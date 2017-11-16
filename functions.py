'''
Function: int2bin
Description: Takes an integer number as input, outputs the binary of the number
Parameters:
	n <int> : Integer number as input
Return:
	x <int> : Binary number of n as integer
'''
def int2bin(n):
	return int(str(bin(n))[2:])

	
	
'''
Function: bin2int
Description: Takes string/integer as input and outputs the integer of that number
Parameters:
	n <int/str> : Number as input, could be string or integer
Return:
	x <int> : Integer version of number n as integer
'''
def bin2int(n):
	return int(str(n), 2)

	
'''
Function: str2bin
Parameters:
	n <str> : String to be converted to binary. ByteArray does have a limit on max
		string size so an extremely large string will cause an error
Return:
	x <str> : String of binary representing the original string, separated by space
'''
def str2bin(n):
	return "".join([bin(ord(n[i]))[2:].zfill(7) for i in range(len(n))])

	
'''
Function: bin2str
Description: Takes a binary string as input, outputs the string of the string
	Assumes that string will be all together and will read in chunks of 7 bits
Parameters:
	n <str> : String input of binary
Returns:
	x <str> : String of binary input
'''
def bin2str(n):
	return "".join([chr(int(n[i:i+7], 2)) for i in range(0, len(n), 7)])

'''
Function: progress_bar
Description: Prints a progress bar for visual indication of progress
Parameters:
	cur <int> : How much progress has been made
	ttl <int> : Total progress to be made
	max_len <int> : Maximum length of the progress bar
Return:
	None
	function prints progress bar to screen
'''
from math import ceil
def progress_bar(cur, ttl, max_len):
	percentage = (cur / ttl) * 100
	per_bar = 100 // max_len
	print("\r|%s%s| %g%%" %(
		"="*(int(percentage)//per_bar),
		" "*(max_len - int(percentage)//per_bar),
		ceil(percentage)
	), end='\r')