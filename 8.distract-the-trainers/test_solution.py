import unittest

from solution import solution

class TestSolution(unittest.TestCase):
  def test_solution(self):
    test_cases = [{
      'input': {
        bananas: [1, 1],
      },
      'expected_outcome': 2,
    }, {
      'input': {
        bananas: [1, 7, 3, 21, 13, 19],
      },
      'expected_outcome': 0,
    }]

    for (index, test_case) in enumerate(test_cases):
      self.assertEqual(
        solution(test_case['input']['bananas']),
        test_case['expected_outcome'],
        'failed on test index ' + str(index)
      )

