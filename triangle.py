def pascal(n):
    """
    Prints the first n rows of Pascal's triangle.

    Parameters:
    n: The number of rows to print.

    Returns:
    None
    """
    # Initialize the first two rows of Pascal's triangle
    triangle = [[1], [1, 1]]

    # Base case for invalid input
    if n < 1:
        print("invalid number of rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        # Fill up the correct number of rows in the triangle
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            # Create the correct row, then add it to the triangle (this row will be 1 longer than the row before it)
            length = len(row_prev) + 1
            for i in range(length):
                # First number is always 1
                if i == 0:
                    row.append(1)
                # Intermediate numbers are the sum of the two numbers above them
                elif i > 0 and i < length - 1:
                    row.append(triangle[row_number - 1][i - 1] + triangle[row_number - 1][i])
                # Last number is always 1
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

        # Print the triangle
        for row in triangle:
            print(row)

# Test
pascal(2)  # Output:
# [1]
# [1, 1]

pascal(5)  # Output:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
