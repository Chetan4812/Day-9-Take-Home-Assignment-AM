def matrix_add(A, B):
    """
    Perform element-wise matrix addition
    """
    # Check dimensions
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Error: Matrices must have the same dimensions for addition.")
        return None

    result = [
        [A[i][j] + B[i][j] for j in range(len(A[0]))]
        for i in range(len(A))
    ]

    return result


def matrix_transpose(matrix):
    """
    Return the transpose of a matrix using nested list comprehension
    """

    # Using zip(*matrix)
    transpose = [list(row) for row in zip(*matrix)]

    return transpose


def matrix_multiply(A, B):
    """
    Perform matrix multiplication using dot product logic
    """

    # Dimension check
    if len(A[0]) != len(B):
        print("Error: Matrix multiplication not possible (dimension mismatch).")
        return None

    result = [
        [
            sum(a * b for a, b in zip(row_a, col_b))
            for col_b in zip(*B)
        ]
        for row_a in A
    ]

    return result


# -------------------------
# Testing Section
# -------------------------
if __name__ == "__main__":

    # Test Case 1 (2x2 matrices)
    a = [[1, 2],
         [3, 4]]

    b = [[5, 6],
         [7, 8]]

    print("Matrix A:", a)
    print("Matrix B:", b)

    print("\nMatrix Addition:")
    print(matrix_add(a, b))

    print("\nMatrix Transpose of A:")
    print(matrix_transpose(a))

    print("\nMatrix Multiplication:")
    print(matrix_multiply(a, b))


    # Test Case 2 (2x3 and 3x2 matrices)

    c = [[1, 2, 3],
         [4, 5, 6]]

    d = [[7, 8],
         [9, 10],
         [11, 12]]

    print("\nMatrix C:", c)
    print("Matrix D:", d)

    print("\nMatrix Multiplication (C x D):")
    print(matrix_multiply(c, d))