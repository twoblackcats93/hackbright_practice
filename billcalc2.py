#Simple Bill Calculator

bill = float(raw_input("How much is the bill? "))
tip_perc = float(raw_input("What tip percentage would you like to leave? "))
peeps = float(raw_input("How many people are in your group? "))

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

print tip()
print total_bill()
print split_bill()







	