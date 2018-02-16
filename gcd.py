def get_gcd(numbers):
	

#.#.#.

numbers = input("Numbers: ")

# Convert Strings to Ints
numbers = numbers.split(" ")
numbers = list(map(int, numbers))

gcd = get_gcd(numbers)
