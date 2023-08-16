import numpy as np

# 10 by 10 grid
maze_layout = [
    "##########", "#S_______#", "#_##_##_##", "#__#_____#", "#_##_##_##",
    "#__#__#__#", "#_##_##_##", "#_______E#", "#_##_##_##", "##########"
]

maze_array = np.array([list(row) for row in maze_layout])

d = []
queue = []
visited = []
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
graph = {}

print(maze_array)

# locate the starting and end point coordinates (row - i, column - k)
for i in range(0, len(maze_array)):
    for k in range(0, len(maze_array[i])):
        if maze_array[i][k] == "S":
            s = (i, k)  # (1, 1)
        elif maze_array[i][k] == "E":
            e = (i, k)  # (7, 8)

current_node = s

def is_valid(point):
    i, k = point
    if 0 <= i < len(maze_array) and 0 <= k < len(maze_array[i]) and maze_array[i][k] != "#":
        return True
    return False

while True:
    if current_node == e:
        break

    visited.append(current_node)

    for direction in directions:
        new_row = current_node[0] + direction[0]
        new_col = current_node[1] + direction[1]
        neighbor_node = (new_row, new_col)

        if is_valid(neighbor_node) and neighbor_node not in visited and neighbor_node not in queue:
            queue.append(neighbor_node)
            graph[neighbor_node] = current_node

    if not queue:
        print("No Path")
        break

    current_node = queue.pop(0)

path = []

while current_node in graph:
    path.insert(0, current_node)
    current_node = graph[current_node]

print(len(path))
