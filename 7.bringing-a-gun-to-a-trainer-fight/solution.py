import math

INFINITY = float('inf')

"""
You are in a room of dimension 0 < w < 1250 and 0 < h < 1250 with x and y integers.
Your position is between 0 and w inclusive and 0 and h inclusive.
A trainer is in the room with the same positioning constraints but at a different
distinct position.
Your laser beam reflects on the walls up to a distance between 0 and 10000 inclusive.
How many distinct directions can you fire your beam to hit the trainer without
hitting you first?
"""

"""
Special ceil function which always map to the integer immedialy greater.

>>> ceil(1.5)
2
>>> ceil(-1.5)
-1
"""
def ceil(x):
  return int(x + 0.5) if x >= 0 else int(x)

"""
In a 1d space, if a point is at `x`, a mirror is at `0` and another mirror at `a`,
then the positions of `x`'s reflections follow this sequence:
[...]
-4 -4*a+x
-3 -2*a-x
-2 -2*a+x
-1 0*a-x
 0 0*a+x
 1 2*a-x
 2 2*a+x
 3 4*a-x
[...]
"""
def mirror(room, point, i, j):
  return [
    int(2 * ceil(i / 2.0) * room[0] + ((-1)**(i % 2) * point[0])),
    int(2 * ceil(j / 2.0) * room[1] + ((-1)**(j % 2) * point[1])),
  ]

def norm(u):
  return math.sqrt(u[0]**2 + u[1]**2)

"""
Angle with the unit vector [1, 0]

>>> import math.pi
>>> angle([1, 0]) / math.pi
0
>>> angle([0, 1]) / math.pi
0.5
>>> angle([-0.5, 0.5]) / math.pi
0.75
>>> angle([0.5, -0.5]) / math.pi
-0.25
"""
def angle(u):
  return math.atan2(u[1], u[0])

def solution(room, me, trainer, distance):
  # Compute the furthest reflections we need to consider
  maxx = int(math.ceil(distance / room[0])) + 1
  maxy = int(math.ceil(distance / room[1])) + 1
  # First compute the angle that would shoot me
  me_dist = {}
  for i in range(-maxx, maxx + 1):
    for j in range(-maxy, maxy + 1):
      if i == 0 and j == 0:
        continue
      my_image = mirror(room, me, i, j)
      beam = [my_image[0] - me[0], my_image[1] - me[1]]
      beam_angle = angle(beam)
      me_dist[beam_angle] = min(me_dist.get(beam_angle, INFINITY), norm(beam))

  # Then compute all the valid firing solutions to the trainer
  firing_solutions = set()
  for i in range(-maxx, maxx + 1):
    for j in range(-maxy, maxy + 1):
      trainer_image = mirror(room, trainer, i, j)
      beam = [trainer_image[0] - me[0], trainer_image[1] - me[1]]
      beam_angle = angle(beam)
      beam_norm = norm(beam)
        # Stop the beam at distance
      if (beam_norm <= distance and
        # Avoid shooting at myself
        (beam_angle not in me_dist or beam_norm < me_dist[beam_angle]) and
        # If a reflection is aligned with another, do not count it twice
        beam_angle not in firing_solutions):
        firing_solutions.add(beam_angle)

  return len(firing_solutions)

if __name__ == "__main__":
  # execute only if run as a script
  print(solution([3, 2], [1, 1], [2, 1], 4))
  assert(solution([3, 2], [1, 1], [2, 1], 4) == 7)
  print(solution([300, 275], [150, 150], [185, 100], 500))
  assert(solution([300, 275], [150, 150], [185, 100], 500) == 9)
  print(solution([2, 5], [1, 2], [1, 4], 11))
  assert(solution([2, 5], [1, 2], [1, 4], 11) == 27)
  print(solution([23, 10], [6, 4], [3, 2], 23))
  assert(solution([23, 10], [6, 4], [3, 2], 23) == 8)
  print(solution([1250, 1250], [1000, 1000], [500, 400], 10000))
  assert(solution([1250, 1250], [1000, 1000], [500, 400], 10000) == 196)
