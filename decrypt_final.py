""" Convert string into a list, use a while loop to iterate through the list. For the while loop, use a counter, i, and the length of the list,
minus 1. i, will be used to create the index for the desired character. Subtracting 1 from the list length ensured that the while loop
will end. Find the first number at index 0, skip positions based on the value of the number plus, the counter, plus the value 1.
Record this as the new index, i. Append the character in the new index to a blank list. Repeat until the loop is done. Convert list to
the final string.""" 

def plaintext(coded_text): 
	text = list(coded_text) #converts coded text into a list 
	i = 0 # counter for while loop
	first_list = [] # blank list that will contain the list of characters 
	final_text = '' # final decoded string 

	while i < len(text)-1: # while loop to iterate through the length of the list 
		i = i + int(text[i]) + 1 # create the index to get to the desired character 
		first_list.append(text[i]) #add desired character to first_list 
		i = i + 1 # increment the counter 
	final_text = ''.join(first_list) # converts the list into a string 
	return final_text 

print plaintext ('15h0o2xzl0a23f!')