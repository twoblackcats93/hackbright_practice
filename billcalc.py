# Bill Calculator with prompts

choice = input("Choose 1 - calculate tip or 2 - split the bill: ")

def tip():
	global bill
	tip_amt = bill * tip_perc/100
	return (tip_amt)

def total_bill():
	global bill
	t_bill= bill + tip()
	return t_bill

def split_bill():
	global bill
	global peeps
	split_bill = bill/peeps
	return split_bill

def main():
	if choice == 1:
		global bill
		global peeps
		global tip_perc
		bill = float(input("How much is the bill? "))
		tip_perc = float(input("What tip percentage would you like to leave? "))
		print "Your tip is" , tip()
		print "Your total bill is" , total_bill()
		bill_split = raw_input("Would you like to split the bill? ")
	

		if bill_split.lower() == "yes":
			peeps = float(input("How many people are in your group? "))
			print "Each person pays" , split_bill()
		else:
			print "Your total bill is" , total_bill()	
	

	elif choice == 2:
		bill = float(input("How much is the bill? "))
		peeps = float(input("How many people are in your group? "))
		print "Each person pays" , split_bill()
	
	else:
		print "Invalid choice, enter 1 or 2"		

if __name__ == "__main__": 
	main()	








	