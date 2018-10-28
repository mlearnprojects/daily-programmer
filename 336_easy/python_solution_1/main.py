# ALGORITHM (created and implemented by ME)

def cannibal(input_numbers, borders):
    """
    >>> cannibal([6, 20, 15, 17, 14, 13, 4, 8, 2, 1, 10], [7, 10, 15])
    [8, 7, 5]
    >>> cannibal([3, 3, 3, 2, 2, 2, 1, 1, 1], [4])
    [1]
    >>> cannibal([21, 9, 5, 8, 10, 1, 3], [10, 15])
    [4, 2]
    >>> cannibal([1, 2, 3, 4, 5], [5])
    [2]
    """
    sorted_numbers = sorted(set(input_numbers), reverse=True)

    cannibals = []
    for border in borders:
        numbers = sorted_numbers[:]
        number_of_cannibals = 0
        for number_index, number in enumerate(numbers):
            if number >= border:
                number_of_cannibals += 1
            else:
                victims_needed = border - number
                remaining_victims = numbers[number_index + 1:]

                if len(remaining_victims) >= victims_needed:
                    number_of_cannibals += 1
                    del numbers[-victims_needed:]
                else:
                    break

        cannibals.append(number_of_cannibals)

    return cannibals

if __name__ == '__main__':
    import doctest
    doctest.testmod()