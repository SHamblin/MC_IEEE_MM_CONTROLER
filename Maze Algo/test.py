import Waypoint

#PLEASE READ BEFORE RUNNING
#This is a quick test set up. It uses a 3x3 Grid for testing so keep that in mind
#as you run the code. you can decide where the wall are but as of right now
#it is still not fully implemented.
#MISSING:
#Edge detection
#Fagging

#These two just need to be implemented with the current set up.
#should not take long.


def maze_map():#Maze mapping

    #Getting the sensor values
    Rot = 0
    Vertices = {}

    visited=[[0,0,0],[0,0,0],[0,0,0]]
    maze=[['A','B','C'],['D','E','F'],['G','H','I']]
    Start = 0 #The code can be easily changed so these initial values are from outside

    while True:

        if Start == 0:
            i = 2
            j = 0
            Vertex = maze[i][j]
            Update = {Vertex:[]}
            Vertices.update(Update)
            print(Vertices)
            Start = Start + 1

        Vertex = maze[i][j]

        L,F,R = map(int,input('Left, Front, Right (1 is wall, 0 is no wall): ').split(','));

        print(L,F,R)
        print(Vertex)

        if visited[i][j] == 0:

            neighbour(L,F,R,Vertex,maze,Vertices,Rot,i,j)
            visited[i][j] = 1
            m = move(L,F,R,Rot,i,j)
            i = 0 + m[0]
            j = 0 + m[1]
            Rot = 0 + m[2]
            print (m[0],m[1])
            print(i,j)
        else:
            print('Visited')
        print(Vertices)

def neighbour(L,F,R,Vertex,maze,Vertices,Rot,i,j): #This sets the neighbours

    print(i,j)
    if Rot == 0:
        if L == 0:

            Vertices[Vertex] += maze[i][j-1]
            Update = {maze[i][j-1]:[]}
            Vertices.update(Update)
            Vertices[maze[i][j-1]] += Vertex


        if F == 0:

            Vertices[Vertex] += maze[i-1][j]
            Update = {maze[i-1][j]:[]}
            Vertices.update(Update)
            Vertices[maze[i-1][j]] += Vertex

        if R == 0:

            Vertices[Vertex] += maze[i][j+1]
            Update = {maze[i][j+1]:[]}
            Vertices.update(Update)
            Vertices[maze[i][j+1]] += Vertex

    elif Rot == 1:
        if L == 0:

            Vertices[Vertex] += maze[i+1][j]
            Update = {maze[i+1][j]:[]}
            Vertices.update(Update)
            Vertices[maze[i+1][j]] += Vertex

        if F == 0:

            Vertices[Vertex] += maze[i][j-1]
            Update = {maze[i][j-1]:[]}
            Vertices.update(Update)
            Vertices[maze[i][j-1]] += Vertex

        if R == 0:

            Vertices[Vertex] += maze[i-1][j]
            Update = {maze[i-1][j]:[]}
            Vertices.update(Update)
            Vertices[maze[i-1][j]] += Vertex

    elif Rot == 2:
        if L == 0:

            Vertices[Vertex] += maze[i][j-1]
            Update = {maze[i][j-1]:[]}
            Vertices.update(Update)
            Vertices[maze[i][j-1]] += Vertex

        if F == 0:

            Vertices[Vertex] += maze[i+1][j]
            Update = {maze[i+1][j]:[]}
            Vertices.update(Update)
            Vertices[maze[i+1][j]] += Vertex

        if R == 0:

            Vertices[Vertex] += maze[i][j+1]
            Update = {maze[i][j+1]:[]}
            Vertices.update(Update)
            Vertices[maze[i][j+1]] += Vertex

    elif Rot == 3:
        if L == 0:

            Vertices[Vertex] += maze[i-1][j]
            Update = {maze[i-1][j]:[]}
            Vertices.update(Update)
            Vertices[maze[i-1][j]] += Vertex

        if F == 0:

            Vertices[Vertex] += maze[i][j+1]
            Update = {maze[i][j+1]:[]}
            Vertices.update(Update)
            Vertices[maze[i][j+1]] += Vertex

        if R == 0:

            Vertices[Vertex] += maze[i+1][j]
            Update = {maze[i+1][j]:[]}
            Vertices.update(Update)
            Vertices[maze[i+1][j]] += Vertex
    return

def move(L,F,R,Rot,i,j):#This changes the current position of within the matrix

    a = i
    b = j

    if Rot == 0:
        if L == 0:
            b = b - 1
            Rot = 1

        elif F == 0:
            a = a - 1

        elif R == 0:
            b = b + 1
            Rot = 3

    elif Rot == 1:
        if L == 0:
            a = a + 1
            Rot = 2

        elif F == 0:
            b = b - 1

        elif R == 0:
            a = a - 1
            Rot = 0

    elif Rot == 2:
        if L == 0:
            a = a - 1
            Rot = 3

        elif F == 0:
            b= b + 1

        elif R == 0:
            a = a + 1
            Rot = 1

    elif Rot == 3:
        if L == 0:
            a = a - 1
            Rot = 0

        elif F == 0:
            b= b + 1

        elif R == 0:
            a = a + 1
            Rot = 2
    m = [a,b,Rot]
    print(m)
    return m

maze_map()
