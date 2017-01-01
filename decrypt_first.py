"""This function decrypts a coded message and returns the message in plain text. 
Note that there are limits to this program:  
- The digits cannot be the same
- Numbers cannot be followed by another number
- You cannot use 0z23xe2hyn as it breaks the rules above. 

The extra print statements are used to check that the desired output is correct.
"""


def plaintext(coded_text):
	first_index = [] # blank list that contains the index of the numbers in the coded message
	first_num = [] # blank list that contains the numbers in the coded message
	final_index = [] # final list that contains the index corresponding to the letters in the coded message
	first_text = [] # blank list that contains the characters that correspond to the final index
	final_text = "" # blank string that will be the final plaintext message
	text = list(coded_text) #splits string elements and converts to a list
	# print len(text)
	# print text
	
	# loop that creates a list of index numbers
	for indx in range(len(text)):
		if text[indx].isdigit(): # identifies if the element is a number
		# .isdigit() doesn't work if the next number is the same 
			new_indx = text.index(text[indx]) # assigns the index to a variable 
			first_index.append(new_indx) # adds the index number to a list
	# print first_index # creates the list of index numbers that contains the digits

	# loop that appends numbers based on the first_index list
	# puts into a new list, converts to an integer
	for num in first_index:
		first_num.append(int(text[num]))
	# print first_num		

	# create the final index that corresponds to the letters
	for i in range(len(first_index)):
		final_index.append(first_index[i] + first_num[i] + 1)
	# print final_index

	# create final list that contains the text
	for character in final_index:
		first_text.append(text[character])
	# print first_text	

	# converts the first_text list into the final decoded string 
	final_text = ''.join(first_text)
	return final_text

print plaintext ('0z2zye3xyin')
