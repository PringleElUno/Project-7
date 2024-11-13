# Author: Luis Pringle
# GitHub username: PringleElUno
# Date: 11/12/2024
# Define a function named reverse_list that takes as a parameter a list and reverses the order
# of the elements in that list

def reverse_list(vals):
    """
    Modifying the input list but reversing the order of the elements in the list
    Parameters:
    reverse list (vals): A list of numbers to be reverse. It should mutate to the original list

    """
    # Add the start and end pointers
    start = 0
    end = len(vals) - 1

    # Loops until start is less then end
    while start < end:
        #Swapping elements to reverse the order manually
        vals[start], vals[end] = vals[end], vals[start]

        #Move start forward and end backwards
        start += 1
        end -= 1

nums = [7, -3, 12, 9]
reverse_list(nums)
