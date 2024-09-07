def depth_first_search(graph, current_node, target_node, current_path=None, visited_nodes=None):
    while current_path is None:
        current_path = []
    if visited_nodes is None:
        visited_nodes = set()

    current_path.append(current_node)
    visited_nodes.add(current_node)

    if current_node == target_node:
        print("Found path:", "_".join(current_path))
    else:
        
        for adjacent_node in graph[current_node]:
            if adjacent_node not in visited_nodes:
                depth_first_search(graph, adjacent_node, target_node, current_path, visited_nodes)

    current_path.pop()
    visited_nodes.remove(current_node)
    
graph_structure = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
end_node = 'F'

depth_first_search(graph_structure, start_node, end_node)