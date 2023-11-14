from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        current_node = frontier.pop() 
        for neighbor in graph[current_node]:
            if neighbor not in result:  
                result.add(neighbor)
                frontier.add(neighbor) 
    return result


def connected(graph):
  if not graph:
      return True
  start_node = list(graph.keys())[0]
  return len(reachable(graph, start_node)) == len(graph)




def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    i = set()
    connected_components = 0
    for node in list(graph.keys()):
      if node not in i:
        connected_components += 1
        i.update(reachable(graph, node))
    return connected_components


