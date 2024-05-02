#!/usr/bin/python3
"""main class"""


def pascal_triangle(n):
    """class triangle"""

    triangle = []
    for x in range(n):
        row = []
        row.append(1)
        for y in range(1, x):
            row.append(triangle[x-1][y-1] + triangle[x-1][y])
        if x > 0:
            row.append(1)
        triangle.append(row)
    return triangle
