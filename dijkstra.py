# Time: O((V + E) log V)
# Because each pop/push in heap costs logV.

# Space: O(V + E)
# For dist array + graph adjacency list + heap.


import heapq

def dijkstra(graph, src, n):
    # graph: adjacency list → graph[u] = [(v, weight), ...]
    # n: number of nodes
    # src: starting node

    dist = [float('inf')] * n
    dist[src] = 0

    min_heap = [(0, src)]   # (distance, node)

    while min_heap:
        curr_dist, node = heapq.heappop(min_heap)

        # skip if outdated entry
        if curr_dist > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = curr_dist + weight

            # relaxation
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))

    return dist


graph = {
    0: [(1,2), (3,3)],
    1: [(2,1)],
    2: [(3,4)],
    3: []
}

print(dijkstra(graph, 0, 4))