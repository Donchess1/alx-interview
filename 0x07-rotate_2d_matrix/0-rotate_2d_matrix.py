#!/usr/bin/python3
def rotate_2d_matrix(matrix):
    """
    THis rotates the 2d matrix by first transposing then swapping
    positions

    """
    for a in range(len(matrix)):
        for b in range(a, len(matrix)):
            matrix[a][b], matrix[b][a] = matrix[b][a], matrix[a][b]
    for a in range(len(matrix)):
        matrix[a].reverse()
