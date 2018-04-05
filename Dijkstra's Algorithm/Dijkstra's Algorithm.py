
# This algorithm can find the shortest distance in a graph
    # We can pass in a graph of mapped out matrix
import Map

def dijkstra(graph,start,goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 99999999
    path = []

    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            weight = 1
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)

    currentNode = goal

    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print("Ooops! Something went wrong")
            break

    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        print('shortest_distance is ' + str(shortest_distance[goal]))
        print(str(path))

dijkstra(Map.map, 'F1', 'F6')
