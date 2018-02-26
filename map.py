map_dict = {'M_0': (0, 0, 0, 0),            ## Possible Wall Orientations
            "M_1": (0, 0, 0, 1),                ## (Left, Up, Righ Down)
            "M_2": (0, 0, 1, 0),                ## 0  <=  No Wall
            "M_3": (0, 0, 1, 1),                ## 1  <=  Wall
            "M_4": (0, 1, 0, 0),
            "M_5": (0, 1, 0, 1),
            "M_6": (0, 1, 1, 0),
            "M_7": (0, 1, 1, 1),
            'M_8': (1, 0, 0, 0),
            "M_9": (1, 0, 0, 1),
            "M_10": (1, 0, 1, 0),
            "M_11": (1, 0, 1, 1),
            "M_12": (1, 1, 0, 0),
            "M_13": (1, 1, 0, 1),
            "M_14": (1, 1, 1, 0),
            "M_15": (1, 1, 1, 1)}

# for possibility in map_dict:              ## Use as refererence for acessing tupples inside dictionary
#     print(map_dict[possibility])

w, h = 6, 6;       ## Use for Creating Matrix of Values
maze = [[0 for x in range(w)] for y in range(h)]       ## Matrix <= Representation of 6X6 Maze

maze[0][0] = map_dict["M_14"],          # Mazed <= Provided by Spencer
maze[0][1] = map_dict["M_10"],
maze[0][2] = map_dict["M_10"],
maze[0][3] = map_dict["M_10"],
maze[0][4] = map_dict["M_10"],
maze[0][5] = map_dict["M_9"],
maze[1][0] = map_dict["M_12"],
maze[1][1] = map_dict["M_8"],
maze[1][2] = map_dict["M_10"],
maze[1][3] = map_dict["M_10"],
maze[1][4] = map_dict["M_8"],
maze[1][5] = map_dict["M_3"],
maze[2][0] = map_dict["M_5"],
maze[2][1] = map_dict["M_5"],
maze[2][2] = map_dict["M_14"],
maze[2][3] = map_dict["M_8"],
maze[2][4] = map_dict["M_2"],
maze[2][5] = map_dict["M_11"],
maze[3][0] = map_dict["M_5"],
maze[3][1] = map_dict["M_4"],
maze[3][2] = map_dict["M_10"],
maze[3][3] = map_dict["M_1"],
maze[3][4] = map_dict["M_12"],
maze[3][5] = map_dict["M_9"],
maze[4][0] = map_dict["M_6"],
maze[4][1] = map_dict["M_2"],
maze[4][2] = map_dict["M_11"],
maze[4][3] = map_dict["M_4"],
maze[4][4] = map_dict["M_3"],
maze[4][5] = map_dict["M_5"],
maze[5][0] = map_dict["M_14"],
maze[5][1] = map_dict["M_10"],
maze[5][2] = map_dict["M_10"],
maze[5][3] = map_dict["M_2"],
maze[5][4] = map_dict["M_11"],
maze[5][5] = map_dict["M_7"],