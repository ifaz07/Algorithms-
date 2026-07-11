# -*- coding: utf-8 -*-
"""Task3.py
| Function                | Time Complexity                         | Space Complexity                     |
| ----------------------- | --------------------------------------- | ------------------------------------ |
| `dfs()`                 | **O(V + E)** (overall across all calls) | **O(V)** (visited + recursion stack) |
| `build_reverse_graph()` | **O(V + E)**                            | **O(V + E)** (transpose graph)       |
| `reverse_dfs()`         | **O(V + E)** (overall across all calls) | **O(V)** (visited + recursion stack) |
| `kosaraju()`            | **O(V + E)**                            | **O(V + E)**                         |

"""

#Task3 Strongly Connected Components
input = open("/content/drive/MyDrive/CSE221_LAB/LAB5/input3.txt","r")
output = open("/content/drive/MyDrive/CSE221_LAB/LAB5/output3.txt","w")

n = input.readline().split(" ")
nodes = int(n[0])+1
edges = int(n[1])

def dfs_visit(node, graph, visited, stack):

      visited[node] = True
      for neighbour in graph[node]:
          if not visited[neighbour]:
             dfs_visit(neighbour, graph, visited, stack)

      stack.append(node)

def dfs_SCC(node, graph, visited, scc):

       visited[node] = True
       scc.append(node)

       for neighbour in graph[node]:
            if not visited[neighbour]:
                 dfs_SCC(neighbour, graph, visited, scc)

def transpose_graph(graph):

       transposed = [[] for _ in range(nodes)]
       for node in range(len(graph)):

           for neighbour in graph[node]:

                transposed[neighbour].append(node)

       return transposed

def strongly_connected_components(graph, nodes):


      visited = [False]*nodes
      stack = []

      for node in range(1,nodes):

          if not visited[node]:
              dfs_visit(node,graph,visited,stack)

      transposed_graph =  transpose_graph(graph)

      visited = [False]*nodes
      scc = []

      while stack:
           node = stack.pop()
           if not visited[node]:
               scc2 = []
               dfs_SCC(node, transposed_graph, visited, scc2)
               scc.append(scc2)

      return scc

Graph = [[] for i in range(nodes)]
for i in range(edges):

    var = list(input.readline().split(" "))
    Graph[int(var[0])].append(int(var[1]))

scc = strongly_connected_components(Graph, nodes)

for i in scc:
      for j in i:
          output.write(f'{j} ')
      output.write(f"\n")

input.close()
output.close()
