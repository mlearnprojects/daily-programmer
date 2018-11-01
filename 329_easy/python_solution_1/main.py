"""
ALGORITHM created and implemented by ME
"""

def nearest_lucky_numbers(threshold, supplement=100):
	"""
	>>> nearest_lucky_numbers(137)
	135 < 137 < 141
	>>> nearest_lucky_numbers(237)
	Lucky number 237
	>>> nearest_lucky_numbers(270)
	267 < 270 < 273
	"""

	# remove even numbers
	numbers = list(range(1, threshold + supplement, 2))
	
	i = 1
	while True:
		try:
			next_number = numbers[i]
		except IndexError:
			break

		first_remove_index = next_number - 1

		if first_remove_index > len(numbers):
			break

		# delete unlucky numbers
		del numbers[first_remove_index::next_number]

		i += 1


	previous_lucky_number = None
	next_lucky_number = None
	if threshold in numbers:
		print(f"Lucky number {threshold}")
	else:
		## we could use bisect.bisect to find previous_lucky_number and next_lucky_number (from solution in reddit)
		# from bisect import bisect
		# pos = bisect(numbers, threshold) # threshold could have this index if inserted to the list
		# previous_lucky_number = numbers[pos-1]
		# next_lucky_number = numbers[pos]

		previous_number = None
		for k, number in enumerate(reversed(numbers)):
			if number < threshold:
				previous_lucky_number = number
				if previous_number is not None:
					next_lucky_number = previous_number
					break
				else:
					raise Exception("Increase supplement number")
			else:
				previous_number = number
		else:
			raise Exception("No lucky number is found")

		print(f"{previous_lucky_number} < {threshold} < {next_lucky_number}")


if __name__ == '__main__':
    import doctest
    doctest.testmod()

