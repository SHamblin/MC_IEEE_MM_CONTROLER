def floodfillb(startx, starty, endx, endy, lastx, lasty, vis, n, path, maze):

    positionx = endx
    positiony = endy

    if (positionx != startx or positiony != starty) and (not(vis[positionx][positiony].__eq__('x')) or path[positionx][positiony] > n):
        path[positionx][positiony] = n
        vis[positionx][positiony] = 'x'
        n = n + 1
        if maze[positionx][positiony] == 1:
            if lastx == positionx-1:
                floodfillb(startx, starty, positionx, positiony + 1, positionx, positiony, vis, n, path, maze)
                floodfillb(startx, starty, positionx, positiony - 1, positionx, positiony, vis, n, path, maze)
            elif lasty == positiony-1:
                floodfillb(startx, starty, positionx - 1, positiony, positionx, positiony, vis, n, path, maze)
                floodfillb(startx, starty, positionx, positiony + 1, positionx, positiony, vis, n, path, maze)
            elif lasty == positiony+1:
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


def floodfill(startx, starty, endx, endy, vis, path, maze):

    positionx = endx
    positiony = endy
    n = 0

    if positionx != startx or positiony != starty:
        path[positionx][positiony] = n
        vis[positionx][positiony] = 'x'
        n = n + 1
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


def path(startx, starty, endx, endy, visited, pathfound, maze):

    floodfill(startx, starty, endx, endy, visited, pathfound, maze)

    return pathfound
