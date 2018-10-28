"""
ALGORITHM (created and implemented by ME)
-------
Example
numbers: [5, 4, 4, 4, 4, 4, 4, 1, 1]
border: 6

**) It's easy to prove that each number (smaller than the border) has greater chance to 
reach to the border than any number that is smaller than that number. (In the example: 
4 has greater chance to reach to 6 than 1):
Therefore if for any number in the list we approve that it doesn't have a chance to reach 
to the border, it means that any number that is smaller or equal to that number can't 
reach to the border too.

1) Sort the list of numbers and iterate through every number in the list starting from 
the largest number. At the beginning remove the "ready cannibals" from the list,
i.e. the numbers that are greater than or equal to the border.

Then at every iteration assign name 'candidate' to the current largest number of the list. 
a) If we approve that the candidate is a cannibal, we remove it from the list and add the 
number of victims (that are needed for the candidate to reach to the border) to the 
cannibals_needed_victims variable which holds the total number of victims that are needed 
for all previously discovered cannibals.

b) If we approve that the candidate can't reach to the border we stop the iteration 
(according to "**" statement above).

2) How to approve the candidate is cannibal or not. The candidate is cannibal if these two 
conditions are both valid:

a) there is at least one victim which is smaller than candidate.(In this case the candidate 
will increase by one and it will be able to eat every victim).
b) there is enough victims to feed both previously discovered cannibals and the 
current candidate.

"""

def how_many_clones(number, sorted_numbers):
    # Don't use count() method because its complexity is O(n).
    # We use this method of finding occurences because we already know that list is sorted.

    number_of_clones = 0
    i = -1
    while True:
        try:
            x = sorted_numbers[i]
        except IndexError:
            break
        else:
            if x == number:
                number_of_clones += 1
                i -= 1
            else:
                break

    return number_of_clones

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
        cannibals_quantity = 0

        victims = sorted(numbers)

        cannibals_needed_victims = 0
        while victims:
            candidate = victims[-1]

            # ready cannibals
            if candidate >= border:
                victims.pop()
                cannibals_quantity += 1
                continue
            
            number_of_candidates = how_many_clones(candidate, victims)
            candidate_needed_victims = border - candidate
            
            for candidate_index in range(number_of_candidates):
                smaller_victims_len = len(victims) - (number_of_candidates - candidate_index)
                
                # -1 because the candidate is in the 'victims' list
                available_victims_for_candidate = len(victims) - cannibals_needed_victims - 1
                
                if smaller_victims_len >= candidate_index + 1 and \
                   available_victims_for_candidate >= candidate_needed_victims:

                    victims.pop()
                    cannibals_quantity += 1
                    cannibals_needed_victims += candidate_needed_victims
                else:
                    victims = []
                    break
          
        cannibals_quantities.append(cannibals_quantity)

    return cannibals_quantities


if __name__ == '__main__':
    import doctest
    doctest.testmod()