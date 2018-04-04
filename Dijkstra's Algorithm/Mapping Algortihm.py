class Graph(object):
    def __init__(self, graph_dict=None):
        # initializes a graph object
        # If no dictionary or None is given,
        # an empty dictionary will be used
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        # returns the vertices of a graph
        return list(self.__graph_dict.keys())

    def edges(self):
        # returns the edges of a graph
        return self.__generate_edges()

    def add_vertex(self, vertex):
        # If the vertex "vertex" is not in
        # self.__graph_dict, a key "vertex" with an empty
        # list as a value is added to the dictionary.
        # Otherwise nothing has to be done.
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        # assumes that edge is of type set, tuple or list;
        # between two vertices can be multiple edges!
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        # A static method generating the edges of the
        # graph "graph". Edges are represented as sets
        # with one (a loop back to the vertex) or two
        # vertices
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


# if __name__ == "__main__":
g = {}

graph = Graph(g)

nodes_visited_counter = 0

for i in range(0, 6):              # Creates vertices for map
    for j in range(0, 6):
        v = str(i) + "_" + str(j)            # i <- row
        graph.add_vertex(v)                  # j <- column
print(graph.vertices())

def movement(*sensors, current_vertex):         # Moves west, north, east, or south based on input
    *_, left_sensor, front_sensor, right_sensor, _ = sensors

    if (left_sensor + front_sensor + right_sensor) == 1:      # if condition is true, there is two exits
        print("Place Flag")

    elif (left_sensor + front_sensor + right_sensor) == 2:      # if condition is true, there is only one exit
        motion = str(left_sensor) + str(front_sensor) + str(right_sensor) + str(0)
        print(motion)


    elif (left_sensor + front_sensor + right_sensor) == 3:      # if condition is true, there is 3 wall
        move_to_flag(sensors)                          # we ave to return to last node with  flag

def graph_map(*sensors, current_vertex, orientation):           # connects edge based on sensor input and orientation

    *_, left_sensor, front_sensor, right_sensor, _ = sensors

    current_row, current_column = current_vertex.split("_")

    if orientation == 0:             # Robot is facing West

        left_row = int(current_row) + 1
        left_column = int (current_column)
        left_vertex = str(left_row) + "_" + str(left_column)

        front_row = int(current_row)
        front_column = int(current_column) - 1
        front_vertex = str(front_row) + "_" + str(front_column)

        right_row = int(current_row) - 1
        right_column = int(current_column)
        right_vertex = str(right_row) + "_" + str(right_column)

        if left_sensor == 0:
            graph.add_edge({current_vertex,left_vertex})
        if front_sensor == 0:
            graph.add_edge({current_vertex,front_vertex})
        if right_sensor == 0:
            graph.add_edge({current_vertex,right_vertex})

    elif orientation == 1:                # Robot is facing North

        left_row = int(current_row)
        left_column = int(current_column) - 1
        left_vertex = str(left_row) + "_" + str(left_column)

        front_row = int(current_row) - 1
        front_column = int(current_column)
        front_vertex = str(front_row) + "_" + str(front_column)

        right_row = int(current_row)
        right_column = int (current_column) + 1
        right_vertex = str(right_row) + "_" + str(right_column)

        if left_sensor == 0:
            graph.add_edge({current_vertex,left_vertex})
        if front_sensor == 0:
            graph.add_edge({current_vertex,front_vertex})
        if right_sensor == 0:
            graph.add_edge({current_vertex,right_vertex})

    elif orientation == 2:              # Robot is facing East

        left_row = int(current_row) - 1
        left_column = int(current_column)
        left_vertex = str(left_row) + "_" + str(left_column)

        front_row = int(current_row)
        front_column = int(current_column) + 1
        front_vertex = str(front_row) + "_" + str(front_column)

        right_row = int(current_row) + 1
        right_column = int(current_column)
        right_vertex = str(right_row) + "_" + str(right_column)

        if left_sensor == 0:
            graph.add_edge([current_vertex,left_vertex])
        if front_sensor == 0:
            graph.add_edge([current_vertex,front_vertex])
        if right_sensor == 0:
            graph.add_edge([current_vertex,right_vertex])

    elif orientation == 3:              # Robot is facing South

        left_row = int(current_row)
        left_column = int(current_column) + 1
        left_vertex = str(left_row) + "_" + str(left_column)

        front_row = int(current_row) + 1
        front_column = int(current_column)
        front_vertex = str(front_row) + "_" + str(front_column)

        right_row = int(current_row)
        right_column = int(current_column) - 1
        right_vertex = str(right_row) + "_" + str(right_column)

        if left_sensor == 0:
            graph.add_edge({current_vertex,left_vertex})
        if front_sensor == 0:
            graph.add_edge({current_vertex,front_vertex})
        if right_sensor == 0:
            graph.add_edge({current_vertex,right_vertex})

    # # print("Edges of graph:")
    # # print(graph.edges())
    # # print("Add vertex:")
    # # graph.add_vertex("z")
    # # print("Vertices of graph:")
    # # print(graph.vertices())
    # # print("Add an edge:")
    # # graph.add_edge({"a", "z"})
    # # print("Vertices of graph:")
    # # print(graph.vertices())
    # # print("Edges of graph:")
    # # print(graph.edges())
    # # print('Adding an edge {"x","y"} with new vertices:')
    # # graph.add_edge({"x", "y"})
    # # print("Vertices of graph:")
    # # print(graph.vertices())
    # # print("Edges of graph:")
    # # print(graph.edges())

def move_to_flag(*sensors):      # Goes back to last marked flag
    print(1)

def mapping_algorithm(graph, start, end):
