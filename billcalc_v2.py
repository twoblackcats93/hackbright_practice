#Bill Calculator with optional parameters
tip_amount = 0
total_bill = 0
split_amount = 0

def calculate_bill(original_bill, tip_perc = 18, peeps = 1):
	global tip_amount
	global total_bill
	global split_amount
	tip_amount = original_bill * tip_perc/100
	total_bill = tip_amount + original_bill
	split_amount = total_bill / peeps

calculate_bill(100, peeps = 2)
print "You're total bill is" , total_bill
print "You're tip is" , tip_amount
print "Each person pays" , split_amount


