def get_divisors(number):
	divisor = 2
	numbers_list = []
	
	while divisor < number:
		if number % divisor == 0: numbers_list.append(divisor)	
		divisor += 1
	
	return numbers_list

#.#.#.

def get_gcd(numbers):
	
	pass
	
#.#.#.

numbers = input("Numbers: ")

while len(numbers) < 2:
	print("\nNumbers must be more than 1 input.")
	numbers = input("Numbers: ")

# Convert Strings to Ints
numbers = numbers.split(" ")
numbers = list(map(int, numbers))

for number in numbers:
	print(number, ": ", get_divisors(number))

#gcd = get_gcd(numbers)
