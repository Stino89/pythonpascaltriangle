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
# Test mult_list function
print(mult_list([1, 2, 3]))  # Output: 6
print(mult_list([]))         # Output: 0
print(mult_list([15]))       # Output: 15

# Function to reverse a string
def rev_string(my_str):
    """
    Reverses a given string.

    Parameters:
    my_str: The string to reverse.

    Returns:
    The reversed string.
    """
    return my_str[::-1]

# Test rev_string function
print(rev_string(""))         # Output: ""
print(rev_string("apple"))    # Output: "elppa"
print(rev_string("mt string"))  # Output: "gnirts tm"

# Function to check whether a number falls within a given range (inclusive)
def num_within(x, a, b):
    """
    Checks if a number is within a given range (inclusive).

    Parameters:
    x: The number to check.
    a: The beginning of the range.
    b: The end of the range.

    Returns:
    True if x is within the range [a, b], False otherwise.
    """
    return x in range(a, b + 1)  # Use range to check if x is within the inclusive range

# Test
print(num_within(3, 2, 4))  # Output: True
print(num_within(3, 1, 3))  # Output: True
print(num_within(10, 2, 5)) # Output: False