import datetime
import random
import unittest

from solution import solution

class TestSolution(unittest.TestCase):
  def test_solution(self):
    test_cases = [{
      'input': {
        'tasks': [1, 2, 3],
        'maximum': 0,
      },
      'expected_outcome': [],
    }, {
      'input': {
        'tasks': [1, 2, 2, 3, 3, 3, 4, 5, 5],
        'maximum': 1,
      },
      'expected_outcome': [1, 4],
    }, {
      'input': {
        'tasks': [1, 1, 1, 1],
        'maximum': 3,
      },
      'expected_outcome': [],
    }, {
      'input': {
        'tasks': [],
        'maximum': 2,
      },
      'expected_outcome': [],
    }, {
      'input': {
        'tasks': [2, 0, 1, 2],
        'maximum': 10,
      },
      'expected_outcome': [2, 0, 1, 2],
    }, {
      'input': {
        'tasks': [2, 0, 1, 2],
        'maximum': 1,
      },
      'expected_outcome': [0, 1],
    }]

    for test_case in test_cases:
      self.assertEqual(
        solution(test_case['input']['tasks'], test_case['input']['maximum']),
        test_case['expected_outcome']
      )

  def test_solution_perf(self):
    prgn = random.Random(123)
    data = list(prgn.randrange(0, 2**20) for x in range(2**20))
    then = datetime.datetime.now()
    solution(data, 6)
    now = datetime.datetime.now()
    self.assertEqual((now - then).total_seconds() < 1, True)
