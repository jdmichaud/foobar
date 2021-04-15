INFINITY = float("inf")

def solution(m): # 3 x O(HW)

  def mst(m, height, width, initial_position):
    cost = [[INFINITY for _ in range(width)] for __ in range(height)]
    cost[initial_position[0]][initial_position[1]] = 1

    queue = [initial_position]
    while queue:
      p = queue.pop()
      for edge in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        neighbor = (p[0] + edge[0], p[1] + edge[1])
        if (neighbor[0] >= 0 and neighbor[0] < height and
            neighbor[1] >= 0 and neighbor[1] < width):
          if cost[neighbor[0]][neighbor[1]] > cost[p[0]][p[1]] + 1:
            cost[neighbor[0]][neighbor[1]] = cost[p[0]][p[1]] + 1
            # This way walls are evaluated only when next to a path, inner walls ignored
            if m[neighbor[0]][neighbor[1]] != 1:
              queue.append(neighbor)

    return cost


  height = len(m)
  width = len(m[0])
  # By going back and forth, only paths separated by one wall with "connect"
  # 1 2 3 4 5 4 3 2 1
  # -------> <-------
  #         9
  a2b = mst(m, height, width, (0, 0)) # O(HW)
  b2a = mst(m, height, width, (height - 1, width - 1)) # O(HW)
  shortest = INFINITY
  for y in range(height): # O(HW)
    for x in range(width):
      shortest = min(shortest, a2b[y][x] + b2a[y][x] - 1)
      if shortest == height * width:
        # micro optim: improve best case
        return shortest

  return shortest

if __name__ == "__main__":
  print(solution([
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0]
  ]))
