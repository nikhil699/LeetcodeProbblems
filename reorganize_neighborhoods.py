#  Problem Statement : Tumhare paas 3 mohallas (neighborhoods) hain.
# Har mohalla mein kuch houses hain.
# Har house ka ek number hai (like 1, 2, 4...) and har house painted hai kisi color se ('r', 'b', etc).

# Final Output Format
# Each house is represented as a string: "number+color"

# Example output:

# python
# Copy
# Edit
# [
#   ['1b', '2g', '4w'],
#   ['4b', '4x', '5y'],
#   ['6c', '8r', '9b']
# ]


#              Time    Space
# Min-Heap	O(N log N)	O(N)
import heapq

def reorganize_neighborhoods(houses,colors):
    min_heap = []

    for i in range(len(houses)):
        for j in range(len(houses[i])):
            heapq.heappush(min_heap,(houses[i][j], colors[i][j]))
    
    result = []

    for house in houses:
        new_row = []
        for _ in house:
            num, col = heapq.heappop(min_heap)
            new_row.append(f"{num}{col}")

        result.append(new_row)
    return result

houses = [[8, 2, 9], [4, 6, 4], [4, 5, 1]]
colors = [['r', 'g', 'b'], ['w', 'c', 'b'], ['x', 'y', 'b']]

output = reorganize_neighborhoods(houses, colors)

for row in output:
    print(row)
