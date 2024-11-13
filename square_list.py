# Author: Luis Pringle
# GitHub username: PringleElUno
# Date: 11/12/2024
# Define a function named square_list that takes as a parameter a list of numbers and replaces each value
# With the square of that value.

def square_list(nums):
    """

    Modifying the input list b replace each element with its square.

    Parameters:
    nums (list): A list of numbers to be squared. The list is mutated in place.

    This function does not return a new list, but it specifically mutates the original list.
    """
    nums[:] = [x * x for x in nums]

nums = [7, -3, 12, 9]
square_list(nums)
