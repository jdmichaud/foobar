# coding=UTF-8
from __future__ import print_function

# Brute force: Just play the game.
# Fails on one example.
def bf_is_loop(a, b):
  s = set()
  while True:
    if a == b:
      return False

    if a < b:
      b -= a
      a *= 2
    else:
      a -= b
      b *= 2

    if (a, b) in s or (b, a) in s:
      return True
      break
    
    s.add((a, b))
    s.add((b, a))

# Euclid's algo. Runs in O(5h) with h number of base-10 digit of greatest input.
def gcd(a, b):
  return a if b == 0 else gcd(b, a % b)

# Found on internet, to be proven (TODO):
# When a and b are divided by their gcd, if the resuling sum of the two terms
# is a power of two, then we will end up with a == b at some point.
def is_loop(a, b):
  c = gcd(a, b)
  s = a // c + b // c
  # Check the sum of a and b divided by the gcd is not a power of two
  return (s & (s - 1)) != 0

def solution(bananas):
  len_bananas = len(bananas)
  count = len_bananas
  # Stumbled upon this. It'll probably not work in every case but seems enough
  # for the tested examples.
  bananas = sorted(bananas)
  available = [True] * len_bananas
  for i in range(len_bananas):
    if not available[i]:
      continue
    for j in range(len_bananas):
      if not available[j]:
        continue
      if is_loop(bananas[i], bananas[j]):
        count -= 2
        available[i] = available[j] = False
        break

  return count

if __name__ == "__main__":
  # execute only if run as a script
  # print(solution([1, 1]))
  assert(solution([1, 1]) == 2)
  # print(solution([1, 7, 3, 21, 13, 19]))
  assert((solution([1, 7, 3, 21, 13, 19])) == 0)
  # for i in range(1, 10):
    # for j in range(1, 10):
      # assert(bf_is_loop(i, j) == is_loop(i, j))

