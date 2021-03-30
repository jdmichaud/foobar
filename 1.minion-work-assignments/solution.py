# Remove all the integers in data that appears n times or more.

def solution(data, n):
  to_remove = set()
  count = {}

  for d in data:
    count[d] = count[d] + 1 if d in count else 1
    if count[d] > n:
      to_remove.add(d)

  return [x for x in data if x not in to_remove]

if __name__ == "__main__":
  # execute only if run as a script
  print(solution([5, 2, 2, 0, 1, 0], 1))
