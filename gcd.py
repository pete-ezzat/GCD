
numbers = input("Numbers: ")

# Convert Strings to Ints
numbers = numbers.split(" ")
numbers = list(map(int, numbers))
print(numbers)
