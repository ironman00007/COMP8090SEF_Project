from dijkstra import dijkstra

def main():
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    start_node = 'A'
    result = dijkstra(graph, start_node)

    print("Shortest distances from node", start_node)
    for node, distance in result.items():
        print(f"{node}: {distance}")

if __name__ == "__main__":
    main()
