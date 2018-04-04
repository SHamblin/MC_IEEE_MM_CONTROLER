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


if __name__ == "__main__":
    g = {}

    graph = Graph(g)

    nodes_visited_counter = 0

    for i in range(0, 6):               # Creates Vertices
        for j in range(0, 6):
            v = str(i) + str(j)
            graph.add_vertex(v)

    def movement(left_sensor, front_sensor, right_sensor):
        determine_flag = left_sensor + front_sensor + right_sensor
        if determine_flag == 3:     # all sensors are blocked (nowhere to move)
            return # INSERT turn 180 degrees
        
        elif determine_flag == 2:
            if left_sensor == 0:
                return # INSERT move left
            elif front_sensor == 0:
                return # INSERT move forward
            elif right_sensor == 0:
                return # INSERT move right

        elif determine_flag == 1:    # one sensor is blocked (two open paths. set a flag)
            go_back_to_flag()

    def go_back_to_flag(left_sensor, front_sensor, right_sensor):
        return



    def map_algorithm(left_sensor, front_sensor, right_sensor, initial_V, final_V, orientation):
        #left_sensor, front_sensor, right_sensor, _ = *sensor

        if orientation == 0:
            return

        if orientation == 1:
            return

        if orientation == 2:
            return

        if orientation == 3:
            return



    # print("Edges of graph:")
    # print(graph.edges())
    # print("Add vertex:")
    # graph.add_vertex("z")
    # print("Vertices of graph:")
    # print(graph.vertices())
    # print("Add an edge:")
    # graph.add_edge({"a", "z"})
    # print("Vertices of graph:")
    # print(graph.vertices())
    # print("Edges of graph:")
    # print(graph.edges())
    # print('Adding an edge {"x","y"} with new vertices:')
    # graph.add_edge({"x", "y"})
    # print("Vertices of graph:")
    # print(graph.vertices())
    # print("Edges of graph:")
    # print(graph.edges())




