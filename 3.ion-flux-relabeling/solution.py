import math

# From a perfect binary tree of height h, find the parent of the provided node q.
# If no parent or index out of range, return -1.
#
#    7
#  3   6
# 1 2 4 5
# solution(3, [1, 6, 7]) -> [3, 7, -1]

# In a binary tree heap, the parent's index is:       (i - 1) / 2
# In a binary tree heap, the left child's index is:   (2 * i) + 1
# In a binary tree heap, the right child's index is:  (2 * i) + 2

# Returns the level of a particular node index in a perfect binary tree
def level(index):
  return (int(math.log(index + 1, 2))) + 1

# Returns the label of a flux converted based on its index in a perfect binary tree if height h
def get_label(index, h):
  if index == 0:
    return 2**h - 1

  parent = int((index - 1) / 2)
  if (index % 2) == 0:
    # even
    return (get_label(parent, h) - 1)
  else:
    # odd
    return (get_label(parent, h) - 1) - 2 * (2**(h - level(index)) - 1) - 1

# Returns the index of a flux converted based on its label in a perfect binary tree if height h
def get_index(label, h, index=0):
  if label == get_label(index, h):
    return index

  left_child_index = 2 * index + 1
  left_child_label = get_label(left_child_index, h)
  if (label <= left_child_label):
    return get_index(label, h, left_child_index)
  else:
    right_child_index = 2 * index + 2
    return get_index(label, h, right_child_index)

def solution(h, q):
  nb_of_elements = 2**h - 1

  return [
    # Find the parent of the flux converter based on its index
    get_label(int((get_index(fc, h) - 1) / 2), h)
    # If the flux converter is in range of the tree otherwise -1
    if fc > 0 and fc < nb_of_elements else -1
    # For each flux converter
    for fc in q
  ]

if __name__ == "__main__":
  # execute only if run as a script
  print(solution(30, [2**30 - 2]))
