import unittest

from solution import get_index, get_label, solution

#    7
#  3   6
# 1 2 4 5
class TestSolution(unittest.TestCase):
  def test_get_label(self):
    test_cases = [
      { 'h': 1, 'indices': [1] },
      { 'h': 2, 'indices': [3, 1, 2] },
      { 'h': 3, 'indices': [7, 3, 6, 1, 2, 4, 5] },
      { 'h': 4, 'indices': [15, 7, 14, 3, 6, 10, 13, 1, 2, 4, 5, 8, 9, 11, 12] },
      { 'h': 5, 'indices': [
        31,
        15, 30,
        7, 14, 22, 29,
        3, 6, 10, 13, 18, 21, 25, 28,
        1, 2, 4, 5, 8, 9, 11, 12, 16, 17, 19, 20, 23, 24, 26, 27,
      ]},
    ]

    for test_case in test_cases:
      for i in range(len(test_case['indices'])):
        self.assertEqual(
          get_label(i, test_case['h']),
          test_case['indices'][i],
        )

  def test_get_index(self):
    test_cases = [
      { 'h': 1, 'indices': [1] },
      { 'h': 2, 'indices': [3, 1, 2] },
      { 'h': 3, 'indices': [7, 3, 6, 1, 2, 4, 5] },
      { 'h': 4, 'indices': [15, 7, 14, 3, 6, 10, 13, 1, 2, 4, 5, 8, 9, 11, 12] },
      { 'h': 5, 'indices': [
        31,
        15, 30,
        7, 14, 22, 29,
        3, 6, 10, 13, 18, 21, 25, 28,
        1, 2, 4, 5, 8, 9, 11, 12, 16, 17, 19, 20, 23, 24, 26, 27,
      ]},
    ]

    for test_case in test_cases:
      for i in range(len(test_case['indices'])):
        self.assertEqual(
          get_index(test_case['indices'][i], test_case['h']),
          i,
        )


  def test_solution(self):
    test_cases = [{
      'input': {
        'h': 3,
        'q': [7, 3, 5, 1],
      },
      'expected_outcome': [-1, 7, 6, 3],
    }, {
      'input': {
        'h': 5,
        'q': [19, 14, 28],
      },
      'expected_outcome': [21, 15, 29],
    }, {
      'input': {
        'h': 5,
        'q': [],
      },
      'expected_outcome': [],
    }, {
      'input': {
        'h': 5,
        'q': [
          1, 2, 4, 5, 8, 9, 11, 12, 16, 17, 19, 20, 23, 24, 26, 27,
          3, 6, 10, 13, 18, 21, 25, 28,
          7, 14, 22, 29,
          15, 30,
          31,
        ],
      },
      'expected_outcome': [
          3, 3, 6, 6, 10, 10, 13, 13, 18, 18, 21, 21, 25, 25, 28, 28,
          7, 7, 14, 14, 22, 22, 29, 29,
          15, 15, 30, 30,
          31, 31,
          -1,
        ],
    }, {
      'input': {
        'h': 1,
        'q': [1, 2],
      },
      'expected_outcome': [-1, -1],
    }, {
      'input': {
        'h': 2,
        'q': [10],
      },
      'expected_outcome': [-1],
    }, {
      'input': {
        'h': 30,
        'q': [2**30 - 2],
      },
      'expected_outcome': [2**30 - 1],
    }]

    for test_case in test_cases:
      self.assertEqual(
        solution(test_case['input']['h'], test_case['input']['q']),
        test_case['expected_outcome']
      )
