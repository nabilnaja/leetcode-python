import heapq
from builtins import float
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        for source, *detail in flights:
            if source in adj:
                adj[source].append(detail)
            else:
                adj[source] = [detail]

        distances = [float("inf") for _ in range(n)]
        current_stops = [float("inf") for _ in range(n)]
        distances[src], current_stops[src] = 0, 0

        heap = [(0, 0, src)]

        while heap:

            cost, stops, node = heapq.heappop(heap)

            if node == dst:
                return cost

            if stops == k + 1:
                continue

            for neighbor, neighborCost in adj.get(node, []):
                newCost = cost + neighborCost
                if distances[neighbor] > newCost or stops < current_stops[neighbor]:
                    distances[neighbor] = newCost
                    heapq.heappush(heap, (newCost, stops + 1, neighbor))
                current_stops[neighbor] = stops
        return -1 if distances[dst] == float("inf") else distances[dst]


if __name__ == '__main__':
    print(Solution().findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1))
