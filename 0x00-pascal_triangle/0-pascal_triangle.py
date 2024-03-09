#!/usr/bin/python3
"""
Function to lists of integers representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """Pascal Funcrion"""
    if n <= 0:
        return []
    pascal = [[1]]
    for i in range(1, n):
        new = [pascal[i-1][0]]
        for j in range(1, i):
            try:
                new.append(pascal[i-1][j-1] + pascal[i-1][j])
            except IndexError:
                new.append(pascal[i-1][j-1] + pascal[i-1][j-1])
        new.append(pascal[i-1][-1])
        pascal.append(new)
    return pascal
