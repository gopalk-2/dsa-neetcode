class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = [[0] * n for _ in range(n)]
        for i, (x1, y1) in enumerate(points):
            for j in range(i + 1, n):
                x2, y2 = points[j]
                manhattan_distance = abs(x1 - x2) + abs(y1 - y2)
                graph[i][j] = graph[j][i] = manhattan_distance
        min_distance = [float('inf')] * n  
        visited = [False] * n 
        min_distance[0] = 0
        total_cost = 0
        for _ in range(n):
            current_node = -1
            for node in range(n):
                if not visited[node] and (current_node == -1 or min_distance[node] < min_distance[current_node]):
                    current_node = node
            visited[current_node] = True
            total_cost += min_distance[current_node]
          
            for neighbor in range(n):
                if not visited[neighbor]:
                    min_distance[neighbor] = min(min_distance[neighbor], graph[current_node][neighbor])
      
        return total_cost
