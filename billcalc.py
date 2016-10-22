# Bill Calculator

prompt = float(raw_input("Enter 1 if you'd like to calculate tip and 2 if you'd like to split the bill: "))

def main():
	if prompt == 1:
		bill = float(raw_input("How much is the bill? "))
		tip_perc = tip_perc = float(raw_input("What tip percentage would you like to leave? "))
print total_bill()
	
bill_split = raw_input("Would you like to split the bill")
if bill_split.lower("yes"):
	peeps = float(raw_input("How many people are in your group? "))
print split_bill()
elif:
	print total_bill()	

elif prompt == 2:
	bill = float(raw_input("How much is the bill? "))
	peeps = float(raw_input("How many people are in your group? "))
print split_bill()
else:
	print "Invalid choice, enter 1 or 2"	

def tip():
	global bill
	tip_amt = bill*tip_perc/100
	return (tip_amt)

def total_bill():
	t_bill= bill + tip()
	return t_bill

def split_bill():
	split_bill = bill/peeps
	return split_bill


		
if __name__ == '__main__':
	main()







	