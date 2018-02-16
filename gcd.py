def get_divisors(number):
	divisor = 2
	numbers_list = []
	
	while divisor < number:
		if number % divisor == 0: numbers_list.append(divisor)	
		divisor += 1
	
	return numbers_list

#.#.#.

def get_gcd(numbers):
	
	non_list = []
	
	for number in numbers:
		non_list.append(get_divisors(number))
	
	# Sort the numbers inside the list (DSC):
	for number_list in non_list:
		number_list.reverse()

	# Arrange NON List by length (DSC):
	for item in range(0, len(non_list)-1):
		for jtem in range(item+1, len(non_list)):
			if len(non_list[item]) < len(non_list[jtem]):
				non_list[item], non_list[jtem] = non_list[jtem], non_list[item]

	print (non_list)
	
#.#.#.

numbers = input("Numbers: ")

while len(numbers) < 2:
	print("\nNumbers must be more than 1 input.")
	numbers = input("Numbers: ")

# Convert Strings to Ints
numbers = numbers.split(" ")
numbers = list(map(int, numbers))

gcd = get_gcd(numbers)
