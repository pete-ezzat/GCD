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

print(numbers)

#gcd = get_gcd(numbers)
