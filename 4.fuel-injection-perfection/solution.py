# solution is given a number of maximum 309 digits. Three operations can be applied:
# - add one
# - remove one
# - div 2 if number if even
# Find the minimum number of operations to reach 1
#
# solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

def solution(n):
  # Python knows how to handle arbitrary large integers: https://www.python.org/dev/peps/pep-0237/
  p = int(n)

  # We manage a state machine:
  # 1. XXXXX...XXX0 : we divide by 2
  # 2. 00000...0011 : special case for 3 where the -1 route is better than case 3
  # 3. XXXXX...XX11 : adding 1 allow us to perform two divisions
  # 4. XXXXX...XX01 : we subtract 1 then we'll divide by 2
  # Any other cases can be reduced to those 4

  count = 0
  while p > 1:
    if p & 1 == 0:
      p = p >> 1
      count += 1
    elif p == 3:
      p = 1
      count += 2
    elif p & 1 and p & 2:
      p += 1
      count += 1
    else:
      p -= 1
      count += 1

  return count

if __name__ == "__main__":
  # execute only if run as a script
  import random
  # print(solution(1024))
  # r = random.Random(0)
  # print(solution(long(''.join([str(r.randrange(0, 9)) for i in range(309)]))))
  print(solution(3))
  print(solution(4))
  print(solution(15))
