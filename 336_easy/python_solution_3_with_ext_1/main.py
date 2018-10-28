"""
ALGORITHM (created by my friend A. and implemented by ME)

1) Sort the list of numbers. Then remove the "ready cannibals" from the list,
i.e. the numbers that are greater than or equal to the border.

2) For example, let's imagine after removing ready cannibals we have:
numbers: [5, 4, 4, 4, 4, 4, 4, 1, 1]
border: 6

At the first iteration we divide the list of numbers into two parts like this:
cannibals: [5]
victims: [4, 4, 4, 4, 4, 4, 1, 1]
Then we check if the cannibal 5 can reach to the border.

At the second iteration we divide the list of numbers into two parts like this:
cannibals: [5, 4]
victims: [4, 4, 4, 4, 4, 1, 1]
Then we check if the cannibals 5 and 4 both can reach to the border.

And so on.

3) At every iteration we do these steps:

Get the smallest cannibal. Let's assign this value to the variable x.
Note that the biggest number in 'victims' can't be bigger than x.
Therefore every cannibal, which is bigger than x, can eat 
*any* number from 'victims' list.
On the other hand, x cannibals can't eat any number from 'victims'
because there could be victims equal to x. For that reason first of all
every x cannibal eats 1 victim which is smaller than x and becomes x+1.
And now every cannibal can eat any remaining victim.

"""

def sort_and_remove_ready_cannibals(border, numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    ready_numbers = [num for num in sorted_numbers if num >= border]
    del sorted_numbers[:len(ready_numbers)]
    
    return sorted_numbers, ready_numbers

def remove_clones(number, arr):
    return [x for x in arr if x != number]


def cannibal(numbers, borders):
    """
    >>> cannibal([3, 3, 3, 2, 2, 2, 1, 1, 1], [4])
    [4]
    >>> cannibal([4, 4, 4, 4, 1, 1, 1, 1, 1], [5])
    [4]
    >>> cannibal([21, 9, 5, 8, 10, 1, 3], [10, 15])
    [4, 2]
    >>> cannibal([1, 2, 3, 4, 5], [5])
    [2]
    >>> cannibal([15, 1, 5, 20, 2, 8, 6, 6, 8, 7, 7, 8], [6, 8])
    [10, 8]
    >>> cannibal([66, 70, 80, 120, 30, 55, 75, 44, 44, 55, 66, 70, 70, 80, 80, 22, 80], [66, 67, 68, 70, 73, 75, 77])
    [11, 11, 11, 10, 8, 7, 7]
    >>> cannibal([10, 9, 9, 1, 1, 1, 1, 1, 1, 1], [12])
    [2]
    >>> cannibal([4, 4, 4, 4, 4, 4, 4], [5])
    [0]
    >>> cannibal([1, 5, 4, 4, 4], [6])
    [2]
    >>> cannibal([1, 1, 4, 4, 4, 5, 4, 4, 4], [6])
    [3]
    >>> cannibal([120, 50, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 1, 1], [11])
    [8]
    >>> cannibal([5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1], [6])
    [5]
    """

    if not numbers or not borders:
        raise Exception('numbers and borders are required')

    cannibals_quantities = []
    for border in borders:
        sorted_numbers, ready_cannibals = sort_and_remove_ready_cannibals(border, numbers)

        i = 1
        number_of_cannibals = 0
        cannibals, victims = sorted_numbers[:1], sorted_numbers[1:]

        while victims:

            smallest_cannibal = cannibals[-1]
            smallest_cannibal_quantity = cannibals.count(smallest_cannibal)

            rest_victims = remove_clones(smallest_cannibal, victims)
            if len(rest_victims) < smallest_cannibal_quantity:
                break

            combined_needed_victims = 0
            for cannibal in cannibals:
                cannibal_needed_victims = border - cannibal
                combined_needed_victims += cannibal_needed_victims

            if combined_needed_victims <= len(victims):
                number_of_cannibals = len(cannibals)
                i += 1
                cannibals, victims = sorted_numbers[:i], sorted_numbers[i:]
            else:
                break

        cannibals_quantities.append(number_of_cannibals + len(ready_cannibals))

    return cannibals_quantities


if __name__ == '__main__':
    import doctest
    doctest.testmod()