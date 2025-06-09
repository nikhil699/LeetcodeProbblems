from collections import defaultdict
class Solution:
	def isCycle(self, V, edges):
	    
	    graph = defaultdict(list)
	    visited = set()
	    
		# create adjacency list
		for u,v in edges:
		    graph[u].append(v)
		    graph[v].append(u)
		   
        
		#using DFS i will check each node with their parent
		def dfs(node,parent):
		    visited.add(node)
		    
		    for neighbour in graph[node]:
		        if neighbour not in visited:
		            if dfs(neighbour,node):
		                return True
		        elif neighbour != parent:
		            return True
		    return False
		
		
		for i in range(v):
		    if i not in visited:
		        if dfs(i,-1):
		            return True
		
		return False

V = 4
E = 4
edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]

