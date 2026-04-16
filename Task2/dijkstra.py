from priority_queue import PriorityQueue

def dijkstra(graph, start):
    pq = PriorityQueue()
    pq.push(start, 0)

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while not pq.is_empty():
        current_node = pq.pop()

        for neighbor, weight in graph[current_node]:
            distance = distances[current_node] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                pq.push(neighbor, distance)

    return distances
