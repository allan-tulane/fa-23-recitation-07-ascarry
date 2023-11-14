# CMPS 2200 Recitation 10## Answers

**Name:**__Abby Scarry____________
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.

- **2)** What is the work of `reachable`, assuming $n$ nodes and $m$ edges?
  
The work is O(n+m), n representing visiting each node, and m representing visting each edge.

- **4)** What is the worst case number of times we need to call `reachable` to determine if a graph is connected?
  
The worst case number of times we need to call 'reachable' to determine if a graph is connected is one, because the start node will determine if it is connected or not.

- **5)** What is the work of `connected`, assuming $n$ nodes and $m$ edges?
  
The work is the same as 'reachable', with O(n+m)

- **7)** What if we switched the graph representation to an adjacency matrix? Would the work of `reachable` change? If so, what would it be? If not, why not?

The work of 'reachable' would change to O(n^2) because to check all nodes from start node, O(n), and then need to check every row, so O(n^2)
