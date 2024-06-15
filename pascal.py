def max_num(a, b, c):
    """
    Returns the maximum of three numbers.

    Parameters:
    a, b, c: Three numbers to compare.

    Returns:
    The maximum of the three numbers.
    """
    return max([a, b, c])  # Use the built-in max function on a list of the three numbers

# Test
print(max_num(1, 2, 3))      # Output: 3
print(max_num(100, 50, 1))   # Output: 100
print(max_num(15, 30, 2))    # Output: 30

# Function to multiply all the numbers in a list
def mult_list(lst):
    """
    Multiplies all the numbers in a list.

    Parameters:
    lst: A list of numbers.

    Returns:
    The product of all the numbers in the list, or 0 if the list is empty.
    """
    if len(lst) == 0:
        return 0
    prod = lst[0]
    if len(lst) > 1:
        for i in lst[1:]:
            prod *= i
    return prod