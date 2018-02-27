# Those three functions work together to find the path.
# findpath() function is the one to be called initially. this
# function calls the function floodfill(), which will get
# the code started. This function only visits the end
# cell, and then calls the function floodfillb(), which will visit all
# the remaining cells until it gets the shortest path. floodfillb() visits
# the matrix cells using recursion.
# To understand the code, start with the function findpath() first, then floodfill(),
# and floodfillb() last.


# lastx represents the last cell x position
# lasty represents the last cell y position
# those two parameters help determine in what direction to go.

def floodfillb(startx, starty, posx, posy, lastx, lasty, vis, n, path, maze):

    positionx = posx
    positiony = posy

    # The following code only execute if the current cell is not the starting point cell and the current cell
    # has not be visited yet, or the current cell is not the starting point cell and the current cell has been visited
    # but the number assigned to it in path is greater than the one that is going to be assigned by this traversal
    if (positionx != startx or positiony != starty) and (not(vis[positionx][positiony].__eq__('x')) or path[positionx][positiony] > n):
        path[positionx][positiony] = n
        vis[positionx][positiony] = 'x'
        n = n + 1
        if maze[positionx][positiony] == 1:  # represents cell with a bottom wall
            if lastx == positionx-1:         # if coming from the top, go right(first call) and go left(second call)
                floodfillb(startx, starty, positionx, positiony + 1, positionx, positiony, vis, n, path, maze)
                floodfillb(startx, starty, positionx, positiony - 1, positionx, positiony, vis, n, path, maze)
            elif lasty == positiony-1:       # if coming from left, go up(first call) and go right(second call)
                floodfillb(startx, starty, positionx - 1, positiony, positionx, positiony, vis, n, path, maze)
                floodfillb(startx, starty, positionx, positiony + 1, positionx, positiony, vis, n, path, maze)
            elif lasty == positiony+1:       # if coming from right, go up(first call) and go left(second call)
                floodfillb(startx, starty, positionx - 1, positiony, positionx, positiony, vis, n, path, maze)
                floodfillb(startx, starty, positionx, positiony - 1, positionx, positiony, vis, n, path, maze)
        elif maze[positionx][positiony] == 2:
            if lastx == positionx-1:
                floodfillb(startx, starty, positionx, positiony - 1, positionx, positiony, vis, n, path, maze)
                floodfillb(startx, starty, positionx + 1, positiony, positionx, positiony, vis, n, path, maze)
            elif lastx == positionx+1:
                floodfillb(startx, starty, positionx - 1, positiony, positionx, positiony, vis, n, path, maze)
                floodfillb(startx, starty, positionx, positiony - 1, positionx, positiony, vis, n, path, maze)
            elif lasty == positiony-1:
                floodfillb(startx, starty, positionx + 1, positiony, positionx, positiony, vis, n, path, maze)
                floodfillb(startx, starty, positionx - 1, positiony, positionx, positiony, vis, n, path, maze)
        elif maze[positionx][positiony] == 3:
            if lastx == positionx-1:
                floodfillb(startx, starty, positionx, positiony - 1, positionx, positiony, vis, n, path, maze)
            elif lasty == positiony-1:
                floodfillb(startx, starty, positionx - 1, positiony, positionx, positiony, vis, n, path, maze)
        elif maze[positionx][positiony] == 4:
            if lastx == positionx+1:
                floodfillb(startx, starty, positionx, positiony - 1, positionx, positiony, vis, n, path, maze)
                floodfillb(startx, starty, positionx, positiony + 1, positionx, positiony, vis, n, path, maze)
            elif lasty == positiony-1:
                floodfillb(startx, starty, positionx + 1, positiony, positionx, positiony, vis, n, path, maze)
                floodfillb(startx, starty, positionx, positiony + 1, positionx, positiony, vis, n, path, maze)
            elif lasty == positiony+1:
                floodfillb(startx, starty, positionx + 1, positiony, positionx, positiony, vis, n, path, maze)
                floodfillb(startx, starty, positionx, positiony - 1, positionx, positiony, vis, n, path, maze)
        elif maze[positionx][positiony] == 5:
            if lasty == positiony-1:
                floodfillb(startx, starty, positionx, positiony + 1, positionx, positiony, vis, n, path, maze)
            elif lasty == positiony+1:
                floodfillb(startx, starty, positionx, positiony - 1, positionx, positiony, vis, n, path, maze)
        elif maze[positionx][positiony] == 6:
            if lastx == positionx+1:
                floodfillb(startx, starty, positionx, positiony - 1, positionx, positiony, vis, n, path, maze)
            elif lasty == positiony-1:
                floodfillb(startx, starty, positionx + 1, positiony, positionx, positiony, vis, n, path, maze)
        # elif maze[positionx][positiony] == 7:
            # if lasty == positiony-1:
        elif maze[positionx][positiony] == 8:
            if lastx == positionx-1:
                floodfillb(startx, starty, positionx + 1, positiony, positionx, positiony, vis, n, path, maze)
                floodfillb(startx, starty, positionx, positiony + 1, positionx, positiony, vis, n, path, maze)
            elif lastx == positionx+1:
                floodfillb(startx, starty, positionx - 1, positiony, positionx, positiony, vis, n, path, maze)
                floodfillb(startx, starty, positionx, positiony + 1, positionx, positiony, vis, n, path, maze)
            elif lasty == positiony+1:
                floodfillb(startx, starty, positionx - 1, positiony, positionx, positiony, vis, n, path, maze)
                floodfillb(startx, starty, positionx + 1, positiony, positionx, positiony, vis, n, path, maze)
        elif maze[positionx][positiony] == 9:
            if lastx == positionx-1:
                floodfillb(startx, starty, positionx, positiony + 1, positionx, positiony, vis, n, path, maze)
            elif lasty == positiony+1:
                floodfillb(startx, starty, positionx - 1, positiony, positionx, positiony, vis, n, path, maze)
        elif maze[positionx][positiony] == 10:
            if lastx == positionx-1:
                floodfillb(startx, starty, positionx + 1, positiony, positionx, positiony, vis, n, path, maze)
            elif lastx == positionx+1:
                floodfillb(startx, starty, positionx - 1, positiony, positionx, positiony, vis, n, path, maze)
        # elif maze[positionx][positiony] == 11:
            # floodfill(startx, starty, positionx-1, positiony, positionx, positiony, maze)
        elif maze[positionx][positiony] == 12:
            if lastx == positionx+1:
                floodfillb(startx, starty, positionx, positiony + 1, positionx, positiony, vis, n, path, maze)
            elif lasty == positiony+1:
                floodfillb(startx, starty, positionx + 1, positiony, positionx, positiony, vis, n, path, maze)
        # elif maze[positionx][positiony] == 13:
            # floodfill(startx, starty, positionx, positiony+1, positionx, positiony, maze)
        # elif maze[positionx][positiony] == 14:
            # floodfill(startx, starty, positionx+1, positiony, positionx, positiony, maze)

    if positionx == startx and positiony == starty:
        path[positionx][positiony] = n
        print('path found')

    return


# The findpath() function calls the floodfill() function

def floodfill(startx, starty, posx, posy, vis, path, maze):

    positionx = posx
    positiony = posy

    # n is the number to be assigned to every cell in the path matrix. It is initially
    # set to zero for the target
    n = 0

    # the code below will only execute if the current position is not the starting point
    if positionx != startx or positiony != starty:
        path[positionx][positiony] = n   # set the cell in path at the current row and column to n
        vis[positionx][positiony] = 'x'  # mark this cell as visited in the vis matrix using 'x'
        n = n + 1                        # increment n by 1

        # depending on the cell configuration, move to all the open adjacent cells by calling floodfillb()
        if maze[positionx][positiony] == 1:
            floodfillb(startx, starty, positionx-1, positiony, positionx, positiony, vis, n, path, maze)
            floodfillb(startx, starty, positionx, positiony+1, positionx, positiony, vis, n, path, maze)
            floodfillb(startx, starty, positionx, positiony-1, positionx, positiony, vis, n, path, maze)
        elif maze[positionx][positiony] == 2:
            floodfillb(startx, starty, positionx + 1, positiony, positionx, positiony, vis, n, path, maze)
            floodfillb(startx, starty, positionx - 1, positiony, positionx, positiony, vis, n, path, maze)
            floodfillb(startx, starty, positionx, positiony-1, positionx, positiony, vis, n, path, maze)
        elif maze[positionx][positiony] == 3:
            floodfillb(startx, starty, positionx - 1, positiony, positionx, positiony, vis, n, path, maze)
            floodfillb(startx, starty, positionx, positiony - 1, positionx, positiony, vis, n, path, maze)
        elif maze[positionx][positiony] == 4:
            floodfillb(startx, starty, positionx+1, positiony, positionx, positiony, vis, n, path, maze)
            floodfillb(startx, starty, positionx, positiony-1, positionx, positiony, vis, n, path, maze)
            floodfillb(startx, starty, positionx, positiony+1, positionx, positiony, vis, n, path, maze)
        elif maze[positionx][positiony] == 5:
            floodfillb(startx, starty, positionx, positiony+1, positionx, positiony, vis, n, path, maze)
            floodfillb(startx, starty, positionx, positiony-1, positionx, positiony, vis, n, path, maze)
        elif maze[positionx][positiony] == 6:
            floodfillb(startx, starty, positionx, positiony-1, positionx, positiony, vis, n, path, maze)
            floodfillb(startx, starty, positionx+1, positiony, positionx, positiony, vis, n, path, maze)
        elif maze[positionx][positiony] == 7:
            floodfillb(startx, starty, positionx, positiony-1, positionx, positiony, vis, n, path, maze)
        elif maze[positionx][positiony] == 8:
            floodfillb(startx, starty, positionx+1, positiony, positionx, positiony, vis, n, path, maze)
            floodfillb(startx, starty, positionx-1, positiony, positionx, positiony, vis, n, path, maze)
            floodfillb(startx, starty, positionx, positiony+1, positionx, positiony, vis, n, path, maze)
        elif maze[positionx][positiony] == 9:
            floodfillb(startx, starty, positionx-1, positiony, positionx, positiony, vis, n, path, maze)
            floodfillb(startx, starty, positionx, positiony+1, positionx, positiony, vis, n, path, maze)
        elif maze[positionx][positiony] == 10:
            floodfillb(startx, starty, positionx+1, positiony, positionx, positiony, vis, n, path, maze)
            floodfillb(startx, starty, positionx-1, positiony, positionx, positiony, vis, n, path, maze)
        elif maze[positionx][positiony] == 11:
            floodfillb(startx, starty, positionx-1, positiony, positionx, positiony, vis, n, path, maze)
        elif maze[positionx][positiony] == 12:
            floodfillb(startx, starty, positionx+1, positiony, positionx, positiony, vis, n, path, maze)
            floodfillb(startx, starty, positionx, positiony+1, positionx, positiony, vis, n, path, maze)
        elif maze[positionx][positiony] == 13:
            floodfillb(startx, starty, positionx, positiony+1, positionx, positiony, vis, n, path, maze)
        elif maze[positionx][positiony] == 14:
            floodfillb(startx, starty, positionx+1, positiony, positionx, positiony, vis, n, path, maze)

    return


# function to be called to solve the maze. the function takes 7 parameters
# startx is the x position of the starting point
# starty is the y position of the starting point
# endx is the x position of the target
# endy is the y position of the target
# vis is a matrix to be provided, that has the same size as the
#   maze matrix, and which is initially filled with 'o's, meaning that no cell has been
#   visited yet.
# path is another matrix to be provided, that also has the same size as the maze matrix, and
#   which is initially filled with a very high number. This is the matrix where the shortest path to the
#   target will be read from.
# maze is the matrix representing the maze
# It returns the matrix path, which contains the shortest from the starting point to the target


def findpath(startx, starty, endx, endy, vis, path, maze):

    floodfill(startx, starty, endx, endy, vis, path, maze)  # function floodfill() is called with all the parameters

    return path
