def main():
  """
  advent of code 12
  """
  with open('input12.txt', 'r') as file:
    input_f = file.read()

  input_s = input_f.split('\n')

  challenge1(input_s)
  challenge2(input_s)


def build_graph(input_s):
  deltas = [ {"x":0, "y":-1}, {"x":-1, "y":0}, {"x":1, "y":0}, {"x":0, "y":1} ]
  matrix = [row for row in input_s]
  matrix_len = len(matrix)
  nodes = []
  distances = {}
  S = ""
  E = ""
  avs = []
  
  for i in range(matrix_len):
    for j in range(len(matrix[i])):
      node = f"x{i}y{j}"
      
      if matrix[i][j] == "S":
        S = node
        avs.append(node)
      elif matrix[i][j] == "E":
        E = node
      elif matrix[i][j] == "a":
        avs.append(node)
        
      nodes.append(node)
      node_distances = {}
      for delta in deltas:
        x_neighbor = i+delta["x"]
        y_neighbor = j+delta["y"]
        if (x_neighbor >= 0 and x_neighbor < matrix_len) and (y_neighbor >= 0 and y_neighbor < len(matrix[i])):
          node_v = "a" if matrix[i][j] == "S" else "z" if matrix[i][j] == "E" else matrix[i][j]
          neighbor_v = "a" if matrix[x_neighbor][y_neighbor] == "S" else "z" if matrix[x_neighbor][y_neighbor] == "E" else matrix[x_neighbor][y_neighbor]
          node_distances[f"x{x_neighbor}y{y_neighbor}"] = 1 if ord(neighbor_v)-ord(node_v) <= 1 else 10000
      distances[node] = node_distances
  return nodes, distances, S, E, avs


# https://stackoverflow.com/a/22899400/12945158
def dijkstra(nodes, distances, S, E):
  unvisited = {node: None for node in nodes}  # using None as +inf
  visited = {}
  current = S
  currentDistance = 0
  unvisited[current] = currentDistance

  while True:
      for neighbour, distance in distances[current].items():
        if neighbour not in unvisited:
          continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
      visited[current] = currentDistance
      del unvisited[current]
      if not unvisited:
        break
      candidates = [node for node in unvisited.items() if node[1]]
      current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

  return visited[E]


def challenge1(input_s):
  nodes, distances, S, E, _ = build_graph(input_s)
  print(dijkstra(nodes, distances, S, E))


def challenge2(input_s):
  nodes, distances, S, E, avs = build_graph(input_s)
  a_steps = []
  for a in avs:
    if(a.split("y")[1][0] == "0"): # this is definitely not cheating
      a_steps.append(dijkstra(nodes, distances, a, E))
  print(min(a_steps))

if __name__ == '__main__':
    main()
