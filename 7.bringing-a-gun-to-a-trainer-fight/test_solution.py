import unittest

from solution import solution

class TestSolution(unittest.TestCase):
  def test_solution(self):
    test_cases = [{
      'input': {
        'room': [3, 2],
        'm': [1, 1],
        't': [2, 1],
        'd': 4,
      },
      'expected_outcome': 7,
    }, {
      'input': {
        'room': [300, 275],
        'm': [150, 150],
        't': [185, 100],
        'd': 500,
      },
      'expected_outcome': 9,
    }, {
      'input': {
        'room': [3, 2],
        'm': [1, 1],
        't': [2, 1],
        'd': 10000,
      },
      'expected_outcome': 39788785,
    }]

    for (index, test_case) in enumerate(test_cases):
      self.assertEqual(
        solution(test_case['input']['room'], test_case['input']['m'],
          test_case['input']['t'], test_case['input']['d']),
        test_case['expected_outcome'],
        'failed on test index ' + str(index)
      )
