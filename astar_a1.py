import heapq
import math

# Representasi kota dan koordinatnya
cities = {
    "A": (0, 0),
    "B": (2, 1),
    "C": (4, 2),
    "D": (5, 5),
    "E": (1, 4)
}

# Representasi jalan antar kota
roads = {
    "A": ["B", "E"],
    "B": ["A", "C"],
    "C": ["B", "D"],
    "D": ["C"],
    "E": ["A", "D"]
}

def heuristic(a, b):
    # Menghitung jarak Euclidean antara dua titik
    return math.dist(cities[a], cities[b])

def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        for neighbor in roads[current]:
            if neighbor not in visited:
                new_g = g + heuristic(current, neighbor)
                new_f = new_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    return None

# Contoh penggunaan
print("A* Path from A to D:", a_star("A", "D"))
