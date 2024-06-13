#!/usr/bin/python3
"""
THis rotates the 2d matrix by first transposing then swapping
positions
"""
def rotate_2d_matrix(matrix):

    for a in range(len(matrix)):
        for b in range(a, len(matrix)):
            matrix[a][b], matrix[b][a] = matrix[b][a], matrix[a][b]
    for a in range(len(matrix)):
        matrix[a].reverse()
    return matrix
