# This module is only made up of matrices to test the code
# matr is a matrix representing the maze
# visited is a matrix representing the visited cells. Initially,
# this matrix is filled of 'o', meaning no cell visited.
# pathfound is the matrix where the found path will be read from.
matr = [[14, 12,  5,  5,  6, 14],
        [10,  8,  5,  4,  2, 10],
        [10, 10, 14, 10, 11, 10],
        [10, 10,  8,  1,  4,  2],
        [10,  8,  2, 12,  3, 11],
        [9,  3, 11,  9,  5,  7]]


visited = [['o', 'o', 'o', 'o', 'o', 'o'],
           ['o', 'o', 'o', 'o', 'o', 'o'],
           ['o', 'o', 'o', 'o', 'o', 'o'],
           ['o', 'o', 'o', 'o', 'o', 'o'],
           ['o', 'o', 'o', 'o', 'o', 'o'],
           ['o', 'o', 'o', 'o', 'o', 'o']]

pathfound = [[10000, 10000, 10000, 10000, 10000, 10000],
             [10000, 10000, 10000, 10000, 10000, 10000],
             [10000, 10000, 10000, 10000, 10000, 10000],
             [10000, 10000, 10000, 10000, 10000, 10000],
             [10000, 10000, 10000, 10000, 10000, 10000],
             [10000, 10000, 10000, 10000, 10000, 10000]]