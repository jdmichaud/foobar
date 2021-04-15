# Find a triplet of integers in l such that the first divides the second and the
# second divides the third. They are to be taken in the order provided in the list.
# The list is not sorted and contain integer from 1 to 999999.

# The number of triplet of elements in a list of size n is C(n, 3).
# Pascal's rule: C(n, k) = C(n-1, k-1) + C(n-1, k).
# So in our case, C(n, 3) = C(n-1, 2) + C(n-1, 3).
# First term (C(n-1, 2)):
#   This is the triangular sequence: C(n-1, 2) = sum(x, 0, n-2) = T(n-2).
#   This triangular sequence is, at any point in the list, the number of divisors
#   among the previous entry in the list. For example:
#       list: [1, 5, 2, 7, 4, 2]
#       T:    [0, 1, 1, 1, 2, 2]
#       5 is divided only by 1 and 4 is divided by 2 and 1.
# Second term (C(n-1, 3)):
#   This is the term introducing recursion in the list.
#     As if n-1 < 3 it's value is 0 then for n-1 >= 3 it's value is deduced from
#     the previous elements in the sequence.
#
# As an example:
#   C(5, 3) = C(4, 2) + C(4, 3)
#           = T(3) + C(3, 2) + C(3, 3)
#           = T(3) + T(2) + C(2, 2) + C(2, 3)
#           = T(3) + T(2) + T(1) + 0
#           = 10
#
# So, when construcing the list T, containing the number of previous divisors,
# we can add that number in an accumulator to get the number of combination of
# triplet so far reached.


# O(n^2)
def solution(l):
  len_l = len(l)
  count = 0
  T = [0] * len_l
  for i in range(len_l):
    for j in range(i):
      if l[i] % l[j] == 0:
        count += T[j]
        T[i] += 1
  return count


# O(n^3)
def bf_solution(l):
  len_l = len(l)
  count = 0
  for i in range(len_l - 2):
    for j in range(i + 1, len_l - 1):
      if l[j] % l[i] == 0:
        for k in range(j + 1, len_l):
          if l[k] % l[j] == 0:
            count += 1
  return count


if __name__ == "__main__":
  # execute only if run as a script
  print(solution([1, 2, 3, 4, 5, 6]))
  assert(solution([1, 2, 3, 4, 5, 6]) == 3)
