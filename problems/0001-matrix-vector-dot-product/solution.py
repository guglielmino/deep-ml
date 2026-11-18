def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    if len(a[0]) != len(b):
        return -1
    
    tot = []
    for row in a:
        row_val = 0
        for i in range(0, len(row)):
            row_val += row[i] * b[i]
        tot.append(row_val)
    return tot
        