import Waypoint

global i,j
i = 2
j = 0

Rot = 0
visited=[[0,0,0],[0,0,0],[0,0,0]]
maze=[['A','B','C'],['D','E','F'],['G','H','I']]

def neighbour(L,F,R,Vertex,maze,Vertices,Rot):

    print(i,j)
    if Rot == 0:
        if L == 0:

            Vertices[Vertex] += maze[i][j-1]

        if F == 0:

            Vertices[Vertex] += maze[i-1][j]

        if R == 0:

            Vertices[Vertex] += maze[i][j+1]

    elif Rot == 1:
        if L == 0:

            Vertices[Vertex] += maze[i+1][j]

        if F == 0:

            Vertices[Vertex] += maze[i][j-1]

        if R == 0:

            Vertices[Vertex] += maze[i-1][j]

    elif Rot == 2:
        if L == 0:

            Vertices[Vertex] += maze[i-1][j]

        if F == 0:

            Vertices[Vertex] += maze[i][j+1]

        if R == 0:

            Vertices[Vertex] += maze[i+1][j]

    elif Rot == 3:
        if L == 0:

            Vertices[Vertex] += maze[i][j+1]

        if F == 0:

            Vertices[Vertex] += maze[i+1][j]

        if R == 0:

            Vertices[Vertex] += maze[i][j-1]
    return

def move(L,F,R,Rot):

    if Rot == 0:
        if L == 0:
            j =- 1

        elif F == 0:
            i =- 1

        elif R == 0:
            j =+ 1

    elif Rot == 1:
        if L == 0:
            i =+ 1

        elif F == 0:
            j =- 1

        elif R == 0:
            i =- 1

    elif Rot == 2:
        if L == 0:
            i =- 1

        elif F == 0:
            j=+ 1

        elif R == 0:
            i =+ 1

    elif Rot == 3:
        if L == 0:
            j =+ 1

        elif F == 0:
            i=+ 1

        elif R == 0:
            j =- 1
    return

Vertices = {}


#Getting the sensor values
for n in  letters:
    Vertex = maze[i][j]
    L,F,R = map(int,input('Left, Front, Right: ').split(','));

    print(L,F,R)

    if visited[i][j] == 0:

        Update = {Vertex:[]}
        Vertices.update(Update)
        print(Vertices)

        neighbour(L,F,R,Vertex,maze,Vertices,Rot)
        visited[i][j] = 1
        move(L,F,R,Rot)
    print(Vertices)
