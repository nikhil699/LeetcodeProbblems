# You are given:
# A graph of locations connected by paths (edges with weights)
# A list of friends at specific locations
# A list of cafes at specific locations
# You have to choose one cafe such that:
# The maximum time taken by any friend to reach that cafe is minimized.

# Problem Intuition (Real-life Story Style)
# Soch lo:
# Tumhare 3 dost hai: Amit (A), Deepak (D), Neha (N)
# Tum chahte ho ki sab milke ek cafe jaayein
# Lekin har dost apne ghar (node) se chalega, aur raste alag-alag ho sakte hain
# Goal:
# Aisa cafe choose karo jahan har dost time pe pahuch sake, aur jo sabse late pahuch raha hai uska time minimum ho.

# Approach
# 1. Model the graph as an adjacency list.
# 2. For each friend:
# Run Dijkstra's algorithm to find shortest distance to all nodes.
# 3. For each cafe:
# Gather shortest distances from all friends
# Get the maximum of those
# Track the cafe with minimum of these max values

# Why Dijkstra?
# Because we need shortest paths in a weighted graph (non-negative)

import heapq

def dijkstra(graph, start):
    # The shortest distance from the starting node to all other nodes in the graph.
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    return dist

graph = {
    'A': [('B', 1), ('D', 4)],
    'B': [('A', 1), ('C', 2)],
    'C': [('B', 2), ('F', 1)],
    'D': [('A', 4), ('E', 3)],
    'E': [('D', 3), ('F', 2)],
    'F': [('E', 2), ('C', 1)]
}

friends = ['A', 'D']
cafes = ['C', 'F']

# Step 1: Get shortest distances from each friend
friend_distances = {}
for friend in friends:
    friend_distances[friend] = dijkstra(graph, friend)

# A : ['A':0,'B':1,'C:3]
# B : ['B':0,'A':2,'C:1]

# Step 2: For each cafe, find the max time taken by any friend
min_max_time = float('inf')
best_cafe = None

for cafe in cafes:
    max_time = max(friend_distances[friend][cafe] for friend in friends)
    if max_time < min_max_time:
        min_max_time = max_time
        best_cafe = cafe

print("Best cafe is:", best_cafe, "with max time:", min_max_time)

