import random
import unittest
from functools import reduce

from solution import bf_solution, solution


def rising_fact(x, n):
  if n == 0:
    return 1
  return reduce(lambda acc, val: acc * val, [i for i in range(x, x + n)])


def tetrahedral(n):
  if n not in tetrahedral.__cache:
    tetrahedral.__cache[n] = rising_fact(n, 3) // 6
  return tetrahedral.__cache[n]

tetrahedral.__cache = {}


class TestSolution(unittest.TestCase):
  def test_solution(self):
    r = random.Random(0)

    test_cases = [{
      'input': {
        'list': [1, 1, 1],
      },
      'expected_outcome': 1,
    }, {
      'input': {
        'list': [1, 2, 3, 4, 5, 6],
      },
      'expected_outcome': 3,
    }, {
      'input': {
        'list': list(reversed([1, 2, 3, 4, 5, 6])),
      },
      'expected_outcome': 0,
    }, {
      'input': {
        'list': [4, 7, 14, 2, 8, 1, 28],
      },
      'expected_outcome': 1,
    }, {
      'input': {
        'list': [1, 2],
      },
      'expected_outcome': 0,
    }, {
      'input': {
        'list': [1, 1, 1, 1, 1],
      },
      'expected_outcome': 10,
    }, {
      'input': {
        'list': [1, 1, 1, 2],
      },
      'expected_outcome': 4,
    }, {
      'input': {
        'list': [1, 1, 1, 2, 1],
      },
      'expected_outcome': 7,
    }, {
      'input': {
        'list': [1, 2, 3, 4, 8, 6, 9],
      },
      'expected_outcome': 7,
    }, {
      'input': {
        'list': [1, 2, 8, 4, 8, 16],
      },
      'expected_outcome': 16,
    }, {
      'input': {
        'list': [r.randint(1, 999999) for _ in range(0, 2000)],
      },
      'expected_outcome': 0,
    }, {
      'input': {
        'list': [r.randint(1, 2000) for _ in range(0, 2000)],
      },
      'expected_outcome': 14580,
    }, {
      'input': {
        'list': [1 for x in range(2000)],
      },
      'expected_outcome': tetrahedral(2000 - 2),
    }]

    for (index, test_case) in enumerate(test_cases):
      self.assertEqual(
        solution(test_case['input']['list']),
        test_case['expected_outcome'],
        'failed on test index ' + str(index)
      )
