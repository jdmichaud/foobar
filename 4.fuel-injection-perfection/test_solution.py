import random
import unittest

from solution import solution

class TestSolution(unittest.TestCase):
  def test_solution(self):
    r = random.Random(0)
    test_cases = [{
      'input': {
        'pellets': '15',
      },
      'expected_outcome': 5,
    }, {
      'input': {
        'pellets': '4',
      },
      'expected_outcome': 2,
    }, {
      'input': {
        'pellets': '30',
      },
      'expected_outcome': 6,
    }, {
      'input': {
        'pellets': '34',
      },
      'expected_outcome': 6,
    }, {
      'input': {
        'pellets': str(2**12),
      },
      'expected_outcome': 12,
    }, {
      'input': {
        'pellets': str(2**1024),
      },
      'expected_outcome': 1024,
    }, {
      'input': {
        'pellets': 768,
      },
      'expected_outcome': 10,
    }, {
      'input': {
        'pellets': ''.join([str(r.randrange(0, 9)) for i in range(309)]),
      },
      'expected_outcome': 1372,
    }]

    for test_case in test_cases:
      print('test_case', test_case)
      self.assertEqual(
        solution(test_case['input']['pellets']),
        test_case['expected_outcome']
      )
