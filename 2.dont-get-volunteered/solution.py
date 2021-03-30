# On a chess board:
# -------------------------
# | 0| 1| 2| 3| 4| 5| 6| 7|
# -------------------------
# | 8| 9|10|11|12|13|14|15|
# -------------------------
# |16|17|18|19|20|21|22|23|
# -------------------------
# |24|25|26|27|28|29|30|31|
# -------------------------
# |32|33|34|35|36|37|38|39|
# -------------------------
# |40|41|42|43|44|45|46|47|
# -------------------------
# |48|49|50|51|52|53|54|55|
# -------------------------
# |56|57|58|59|60|61|62|63|
# -------------------------
# You start a a particular position. How many moves, as a chess knight, you have
# to do to reach a particular position?
#
# solution(1, 2) -> 3
# 3 moves to go from 0 to 1 as a chess knight.

def create_path(current, parents):
  path = []
  while parents[current] != None:
    path.append(current)
    current = parents[current]
  return list(reversed(path))

# Solution using A*
def solution(src, dest):
  knight_moves = [
    (-10, (-2, -1)),
    (-17, (-1, -2)),
    (-15, (1, -2)),
    (-6, (2, -1)),
    (10, (2, 1)),
    (17, (1, 2)),
    (15, (-1, 2)),
    (6, (-2, 1)),
  ]

  # Heuristic that gives the potential cost to go from a to b
  # The heuristic is not adapted to knights move, but will keep the algo heading
  # in the right direction.
  def h(a, b):
    return abs(int(a / 8) - int(b / 8)) + abs(int(a % 8) - int(b % 8))

  def allowed(position, move):
    shift, moves = move
    posx = int(position % 8)
    posy = int(position / 8)

    return (
      posx + moves[0] >= 0 and posx + moves[0] < 8 and
      posy + moves[1] >= 0 and posy + moves[1] < 8
    )

  # The map of node to best score to go from n
  gscore = [float("inf") for x in range(64)]
  gscore[src] = 0
  # The map of node to the best estimated possible score to go from n
  fscore = [float("inf") for x in range(64)]
  fscore[src] = h(src, dest)
  # The previous best node from n
  parents = [None for x in range(64)]

  # The list of node to visit
  tovisit = set()
  tovisit.add(src)

  while (len(tovisit) > 0):
    # Chose the best score as the next moving point
    current = sorted([(x, fscore[x]) for x in tovisit], key=lambda x: x[1])[0][0]
    if (current == dest):
      # We've just arrived!
      # print(create_path(current, parents))
      return fscore[current]

    tovisit.remove(current)

    # Retrieve all possible moves from current
    possible_moves = [x for x in knight_moves if allowed(current, x)]
    for move in possible_moves:
      next_position = current + move[0]
      tentative_score = gscore[current] + 1
      if tentative_score < gscore[next_position]:
        # The previous score of that square is worst, actualize
        gscore[next_position] = tentative_score
        fscore[next_position] = tentative_score + h(next_position, dest)
        parents[next_position] = current
        tovisit.add(next_position)

  # Should not reach here...
  return 0

if __name__ == "__main__":
  # execute only if run as a script
  print(solution(0, 1))
