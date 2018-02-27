# This module test the code using the test matrices and prints the found path
import findPath
import testmatrices

path = findPath.findpath(0, 0, 5, 5, testmatrices.visited, testmatrices.pathfound, testmatrices.matr)
print(path)
