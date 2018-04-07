
import Map
# from smbus2 import SMBusWrapper

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

for i in range(0, 6):  # Creates vertices for map
    for j in range(0, 6):
        v = str(i) + "_" + str(j)  # i <- row
        graph.add_vertex(v)  # j <- column

# print(graph.vertices())     # tests created vertices

def graph_map(sensors, current_vertex, orientation):  # connects edge based on sensor input and orientation

    *_, left_sensor, front_sensor, right_sensor, _ = sensors
    # print('Left Sensor: ' + str(left_sensor))                # Used for testing input
    # print('Front Sensor: ' + str(front_sensor))
    # print('Right Sensor: ' + str(right_sensor))

    current_row, current_column = current_vertex.split("_")
    print('Current Vertex: '+ current_vertex)
    # print('Current Row: ' + str(current_row))                     # Used for tersting location
    # print('Current Collumn: ' + str(current_column))

    print("Orientation: " + str(orientation))                 # Used for testing orientation

    if orientation == 0:             # Robot is facing West

        left_row = int(current_row) + 1
        left_column = int (current_column)
        left_vertex = str(left_row) + "_" + str(left_column)
        # print('Left Vertex: ' + left_vertex)

        front_row = int(current_row)
        front_column = int(current_column) - 1
        front_vertex = str(front_row) + "_" + str(front_column)
        # print('Front Vertex: ' + front_vertex)

        right_row = int(current_row) - 1
        right_column = int(current_column)
        right_vertex = str(right_row) + "_" + str(right_column)
        # print('Right Vertex: ' + right_vertex)

        back_row = int(current_row)
        back_column = int(current_column) + 1
        back_vertex = str(back_row) + "_" + str(back_column)
        # print('Back Vertex: ' + back_vertex)

        if int(left_sensor) == int(0):
            graph.add_edge({current_vertex,left_vertex})
            # print('Left Edge Added')
            # print(graph.edges())

        if int(front_sensor) == int(0):
            graph.add_edge({current_vertex,front_vertex})
            # print('Front Edge Added')
            # print(graph.edges())

        if int(right_sensor) == int(0):
            graph.add_edge({current_vertex,right_vertex})
            # print('Right Edge Added')
            # print(graph.edges())

        left, front, right = movement(sensors, current_vertex)

        if int(left) == int(0):
            # print(left_vertex)
            return left_vertex

        if int(front) == int(0):
            # print(front_vertex)
            return front_vertex

        if int(right) == int(0):
            # print(right_vertex)
            return right_vertex

        if int(left) == int(1) and int(front) == int(1) and int(right) == int(1):
            # print(back_vertex)
            return back_vertex

    elif orientation == 1:                # Robot is facing North

        left_row = int(current_row)
        left_column = int(current_column) - 1
        left_vertex = str(left_row) + "_" + str(left_column)
        # print('Left Vertex: ' + left_vertex)

        front_row = int(current_row) - 1
        front_column = int(current_column)
        front_vertex = str(front_row) + "_" + str(front_column)
        # print('Front Vertex: ' + front_vertex)

        right_row = int(current_row)
        right_column = int(current_column) + 1
        right_vertex = str(right_row) + "_" + str(right_column)
        # print('Right Vertex: ' + right_vertex)

        back_row = int(current_row) + 1
        back_column = int(current_column)
        back_vertex = str(back_row) + "_" + str(back_column)
        # print('Back Vertex: ' + back_vertex)

        if int(left_sensor) == int(0):
            graph.add_edge({current_vertex,left_vertex})
            # print('Left Edge Added')
            # print(graph.edges())

        if int(front_sensor) == int(0):
            graph.add_edge({current_vertex,front_vertex})
            # print('Front Edge Added')
            # print(graph.edges())

        if int(right_sensor) == int(0):
            graph.add_edge({current_vertex,right_vertex})
            # print('Right Edge Added')
            # print(graph.edges())

        left, front, right = movement(sensors, current_vertex)

        if int(left) == int(0):
            # print(left_vertex)
            return left_vertex

        if int(front) == int(0):
            # print(front_vertex)
            return front_vertex

        if int(right) == int(0):
            # print(right_vertex)
            return right_vertex

        if int(left) == int(1) and int(front) == int(1) and int(right) == int(1):
            # print(back_vertex)
            return back_vertex

    elif orientation == 2:              # Robot is facing East

        left_row = int(current_row) - 1
        left_column = int(current_column)
        left_vertex = str(left_row) + "_" + str(left_column)
        # print('Left Vertex: ' + left_vertex)

        front_row = int(current_row)
        front_column = int(current_column) + 1
        front_vertex = str(front_row) + "_" + str(front_column)
        # print('Front Vertex: ' + front_vertex)

        right_row = int(current_row) + 1
        right_column = int(current_column)
        right_vertex = str(right_row) + "_" + str(right_column)
        # print('Right Vertex: ' + right_vertex)

        back_row = int(current_row)
        back_column = int(current_column) - 1
        back_vertex = str(back_row) + "_" + str(back_column)
        # print('Back Vertex: ' + back_vertex)

        if int(left_sensor) == int(0):
            graph.add_edge([current_vertex,left_vertex])
            # print('Left Edge Added')
            # print(graph.edges())

        if int(front_sensor) == int(0):
            graph.add_edge([current_vertex, front_vertex])
            # print('Front Edge Added')
            # print(graph.edges())

        if int(right_sensor) == int(0):
            graph.add_edge([current_vertex, right_vertex])
            # print('Right Edge Added')
            # print(graph.edges())

        left, front, right = movement(sensors, current_vertex)

        if int(left) == int(0):
            # print(left_vertex)
            return left_vertex

        if int(front) == int(0):
            # print(front_vertex)
            return front_vertex

        if int(right) == int(0):
            # print(right_vertex)
            return right_vertex

        if int(left) == int(1) and int(front) == int(1) and int(right) == int(1):
            # print(back_vertex)
            return back_vertex

    elif orientation == 3:              # Robot is facing South

        left_row = int(current_row)
        left_column = int(current_column) + 1
        left_vertex = str(left_row) + "_" + str(left_column)
        # print('Left Vertex: ' + left_vertex)

        front_row = int(current_row) + 1
        front_column = int(current_column)
        front_vertex = str(front_row) + "_" + str(front_column)
        # print('Front Vertex: ' + front_vertex)

        right_row = int(current_row)
        right_column = int(current_column) - 1
        right_vertex = str(right_row) + "_" + str(right_column)
        # print('Right Vertex: ' + right_vertex)

        back_row = int(current_row) - 1
        back_column = int(current_column)
        back_vertex = str(back_row) + "_" + str(back_column)
        # print('Back Vertex: ' + back_vertex)

        if int(left_sensor) == int(0):
            graph.add_edge({current_vertex,left_vertex})
            # print('Left Edge Added')
            # print(graph.edges())

        if int(front_sensor) == int(0):
            graph.add_edge({current_vertex,front_vertex})
            # print('Front Edge Added')
            # print(graph.edges())

        if int(right_sensor) == int(0):
            graph.add_edge({current_vertex,right_vertex})
            # print('Right Edge Added')
            # print(graph.edges())

        left, front, right = movement(sensors,current_vertex)

        if int(left) == int(0):
            # print(left_vertex)
            return left_vertex

        if int(front) == int(0):
            # print(front_vertex)
            return front_vertex

        if int(right) == int(0):
            # print(right_vertex)
            return right_vertex

        if int(left) == int(1) and int(front) == int(1) and int(right) == int(1):
            # print(back_vertex)
            return back_vertex

def movement(sensors, current_vertex):
    *_, left_sensor, front_sensor, right_sensor, _ = sensors

    flag = "No Flag Yet Placed"

    if int(left_sensor) + int(front_sensor) + int(right_sensor) == int(1):  # if condition is true, there is two exits

        if left_sensor == 0:

            front_sensor = 1
            right_sensor = 1

            motion = str(left_sensor) + str(front_sensor) + str(right_sensor)
            # print("Moving Left")

            # with SMBusWrapper(1) as bus:
            #     data = 1
            #     bus.write_byte(33, data)

            return motion

        elif front_sensor == 0:

            left_sensor = 1
            right_sensor = 1

            motion = str(left_sensor) + str(front_sensor) + str(right_sensor)
            # print('Moving Forward')

            # with SMBusWrapper(1) as bus:
            #     data = 2
            #     bus.write_byte(33, data)

            return motion

        elif right_sensor == 0:
            left_sensor = 1
            front_sensor = 1

            motion = str(left_sensor) + str(front_sensor) + str(right_sensor)
            # print('Moving Right')

            # with SMBusWrapper(1) as bus:
            #     data = 3
            #     bus.write_byte(33, data)

            return motion

    elif int(left_sensor) + int(front_sensor) + int(right_sensor) == int(2):  # if conditioin is true, there is only one exit

        motion = str(left_sensor) + str(front_sensor) + str(right_sensor)

        if int(left_sensor) == int(0):
            # print('Moving Left')

            # with SMBusWrapper(1) as bus:
            #     data = 1
            #     bus.write_byte(33, data)

            return motion

        if int(front_sensor) == int(0):
            # print('Moving Forward')

            # with SMBusWrapper(1) as bus:
            #     data = 2
            #     bus.write_byte(33, data)

            return motion

        if int(right_sensor) == int(0):
            # print('Moving Right')

            # with SMBusWrapper(1) as bus:
            #     data = 2
            #     bus.write_byte(33,data)

            return motion

    elif int(left_sensor + front_sensor + right_sensor) == int(3):  # if condition is true, there is 3 wall
        print("Closed Path Encountered")
        motion = str(left_sensor) + str(front_sensor) + str(right_sensor)
        print(motion)
        return motion






# def move_to_flag(sensors, current_vertex, last_flagged):  # Goes back to last marked flag
#
#     with SMbusWrapper(1) as bus:
#         data = 4
#         bus.write_byte(33, data)
#
#     while current_vertex != last_flagged:
#         movement(current_vertex)
#     #   elif int(left_sensor + front_sensor + right_sensor) == int(2):# if condition is true, there is only one exit
#         print("Okay")

# for i in range(7):
#     if i == 0:
#         initial_vertex = "2_1"
#         new_vertex = graph_map(Map.input[i], initial_vertex, Map.orientation[i])
#     else:
#         new_vertex = graph_map(Map.input[i], new_vertex, Map.orientation[i])

graph_map("00001110", '1_1', 0)



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

