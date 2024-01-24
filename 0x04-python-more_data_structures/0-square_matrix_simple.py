#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for arr in matrix:
        newMatrix.append(list(map(lambda x : x*x,matrix)))
    return newMatrix
