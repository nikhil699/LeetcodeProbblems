# Problem satement:
# Movies ka graph diya gaya hai.
# Har movie ek node hai.
# Agar do movies similar hain, to unke beech edge (connection) hoga.
# Har movie ka ek rating diya gaya hai (e.g., 4.5, 3.2, etc.).
# Tumhe ek movie di jaayegi, aur tumhe uske similar movies dhoondhni hain:
# Jo uske graph component mein hain (i.e., graph ke us part mein jo connected hai).
# Unmein se top N highest rated movies return karni hai.
# Example:
# A -- B -- C
# D -- E
# Ratings:
# A: 4.2
# B: 3.5
# C: 4.8
# D: 3.0
# E: 4.0
# Agar input ho:
# movie = A, N = 2
# A, B, C connected hain (same component).
# Inmein se top 2 rating wale movies: C (4.8) and A (4.2)
# So, output:
# ["C", "A"]

# Approach
# 1. Traverse the graph using BFS or DFS starting from the given movie
# 2. For each reachable movie:
#    - Add it into a min-heap of size N (based on rating)
# 3. After traversal, return the N movies from the heap

# Time complexity : Visits each movie once → O(K)
# Processes each edge once → O(K + E'), where E' are the edges in that connected component
# Push/pops up to N items → O(log N) per operation
# Worst case: do it for K neighbors → O(K log N)
# Time : O(K + E') + O(K log N)
# Space Complexity
# Visited Set: O(K)
# Queue for BFS: O(K)
# Heap: Stores up to N elements → O(N)
# Graph and Ratings Storage (already maintained in the class): Not counted per call
# ➡️ Total Space:
# O(K + N)

import heapq
from collections import defaultdict,deque

class MovieGraph:
    def __init__(self):
        self.graph = defaultdict(list) # adjacency list
        self.ratings = {} # for the ratings to be stored
    
    def add_similarity(self,movie01, movie02):
        self.graph[movie01].append(movie02)
        self.graph[movie02].append(movie01)
    
    def add_movie(self,movie,rating):
        self.ratings[movie] = rating
    

    def get_top_n_similar(self,movie,numberOfRating):
        visited = set()
        queue = deque()
        heap = []
        visited.add(movie)
        queue.append(movie)
        heapq.heappush(heap, (self.ratings[movie], movie))

        while queue:
            item = queue.popleft()

            for neighbour in self.graph[item]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                
                    heapq.heappush(heap,(self.ratings[neighbour],neighbour))
                    if len(heap) > numberOfRating:
                        heapq.heappop(heap)
                    
       
        return [movie for _, movie in heap]


g = MovieGraph()

# Add movies
g.add_movie('A', 4.3)
g.add_movie('B', 3.2)
g.add_movie('C', 5.0)
g.add_movie('D', 2.1)
g.add_movie('E', 4.9)

# Similarity connections
g.add_similarity('A', 'B')
g.add_similarity('B', 'C')
g.add_similarity('D', 'E')

# Query top N similar movies to A
print("Top 2 similar to A:", g.get_top_n_similar('A', 2))  # ['C', 'A']
print("Top 1 similar to D:", g.get_top_n_similar('D', 1))  # ['E']
