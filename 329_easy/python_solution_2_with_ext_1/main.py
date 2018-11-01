"""
ALGORITHM created and implemented by ME
"""

def test_first_lucky_numbers(numbers):
	#test first 57 lucky numbers
	test_lucky_numbers = [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 
					 79, 87, 93, 99, 105, 111, 115, 127, 129, 133, 135, 141, 151, 159, 163, 
					 169, 171, 189, 193, 195, 201, 205, 211, 219, 223, 231, 235, 237, 241, 
					 259, 261, 267, 273, 283, 285, 289, 297, 303]

	if len(numbers) >= 57:
		assert numbers[:57] == test_lucky_numbers
	else:
		assert numbers == test_lucky_numbers[:len(numbers)]

def get_lucky_numbers(n):
	# remove even numbers
	numbers = list(range(1, n+1, 2))
	
	i = 1
	while True:
		try:
			next_number = numbers[i]
		except IndexError:
			break

		first_remove_index = next_number - 1

		# if there is no number to remove
		if first_remove_index > len(numbers):
			break

		# slice deleting is very fast in python. When n=100.000, lucky numbers are found in ~0.005 seconds
		del numbers[first_remove_index::next_number]
	
		## It's very slow when we remove unlucky numbers one by one.
		## When n=100.000, lucky numbers are found in ~0.25 seconds.
		# while True:
		# 	try:
		# 		del numbers[first_remove_index]
		# 		first_remove_index -= 1
		# 	except:
		# 		break
		# 	else:
		# 		first_remove_index += next_number

		i += 1

	test_first_lucky_numbers(numbers)

	return numbers


if __name__ == '__main__':
	from timeit import default_timer as timer

	start = timer()
	# ~13 seconds for n=10million
	get_lucky_numbers(10000000)
	end = timer()
	print(f"{end - start} seconds")
