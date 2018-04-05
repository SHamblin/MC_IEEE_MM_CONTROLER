
Vertices ={'F1': ['E1'],
       'E1': ['F1' ,'D1'],
       'D1': ['E1','C1'],
       'C1': ['D1','B1'],
       'B1': ['C1','A1'],
       'A1': ['B1','A2'],
       'F2': ['E2','F3'],
       'E2': ['D2','F2','E3'],
       'D2': ['E2','C2'],
       'C2': ['D2','B2'],
       'B2': ['A2','C2','B3'],
       'A2': ['A1','B2'],
       'F3': ['F2','F4'],
       'E3': ['E2','E4'],
       'D3': ['C3'],
       'C3': ['B3','D3','C4'],
       'B3': ['A3','C3'],
       'A3': ['B3'],
       'F4': ['F3','F5'],
       'E4': ['D4','E3', 'E5'],
       'D4': ['C4','E4'],
       'C4': ['C3','D4','C5'],
       'B4': ['A4','B5'],
       'A4': ['B4','A5'],
       'F5': ['E5','F4'],
       'E5': ['D5','E4','F5'],
       'D5': ['D5','E5'],
       'C5': ['B5','C4','C6'],
       'B5': ['B4','C5'],
       'A5': ['A4','A6'],
       'F6': ['D6'],
       'E6': ['D6','F6'],
       'D6': ['C6','E6'],
       'C6': ['B6','C5','D6'],
       'B6': ['C6'],
       'A6': ['A5']
}

def Waypoint(Vertices, Position, Destination, Path =[]):
        Path = Path + [Position]
        if Position == Destination:
            return Path
        Dest = None
        for Vertex in Vertices[Position]:
            if Vertex not in Path:
                newPath = Waypoint(Vertices, Vertex, Destination, Path)
                if newPath:
                    if not Dest or len(newPath) < len(Dest):
                        Dest = newPath
        return Dest

print(Waypoint(Vertices, 'F1', 'F5'))
