# calculates how many years until retirement 

# user input and input validation
age = int(input('how old are you? '))
while age < 0:
    age = int(input('your age cannot be negative, please try again: '))
initial = float(input("how much money are you starting with? "))
while initial < 0:
    initial = float(input("your initial amount cannot be negative, please try again: "))
target_age = int(input("by when do you plan to retire? "))
while target_age < age:
    target_age = int(input("your target age cannot be lower than your current age, please try again: "))
target_balance = float(input("how much money do you wish to retire with? "))
while target_balance < initial: 
    target_balance = float(input("your target balance cannot be lower than your initial balance, please try again: "))
contribution = float(input("how much do you wish to contribute yearly? "))
while contribution < 0: 
    contribution = float(input("your annual contribution cannot be negative, please try again: "))
rate = float(input("what is the annual growth as a percetnage? "))
while rate < 0:
    rate = float(input("your rate cannot be negative, please try again: "))

# place holder variable
x = 0

# create a loop for the calculations 
for i in range (age, target_age):
	# calculates total interest for initial 
	p = ((rate/100 + 1.0) ** (target_age - age)) * initial
	# conditions to see if the total interest would help you reach your goal 
	if ((initial + p) < target_balance): 
		interest = initial * (rate/100)
		end = initial + interest + contribution
		print(f'age: {i:<10}\tinitial: ${initial:<10.2f}\tinterest: ${interest:<10.2f}\tcontribution: ${contribution:<10.2f}\tend balance: ${end:>10.2f}')
		initial = end
		x += 1
		age += 1 
	elif ((initial + p) >= target_balance):
		interest = initial * (rate/100)
		contribution = 0
		end = initial + interest
		print(f'age: {i:<10}\tinitial: ${initial:<10.2f}\tinterest: ${interest:<10.2f}\tcontribution: ${contribution:<10.2f}\tend balance: ${end:>10.2f}')
		initial = end

# outcomes
if initial >= target_balance: 
	print(f'\nyou can reach your goal by contributing for {x} year(s) until age {age}, then coasting the rest until age {target_age}')
elif initial <= target_balance: 
	print('\nyour goal is impossible')