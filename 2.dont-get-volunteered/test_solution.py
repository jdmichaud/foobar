import datetime
import random
import unittest

from solution import solution

# -------------------------
# | 0| 1| 2| 3| 4| 5| 6| 7|
# -------------------------
# | 8| 9|10|11|12|13|14|15|
# -------------------------
# |16|17|18|19|20|21|22|23|
# -------------------------
# |24|25|26|27|28|29|30|31|
# -------------------------
# |32|33|34|35|36|37|38|39|
# -------------------------
# |40|41|42|43|44|45|46|47|
# -------------------------
# |48|49|50|51|52|53|54|55|
# -------------------------
# |56|57|58|59|60|61|62|63|
# -------------------------

class TestSolution(unittest.TestCase):
  def test_solution(self):
    test_cases = [{
      'input': {
        'src': 0,
        'dest': 1,
      },
      'expected_outcome': 3,
    }, {
      'input': {
        'src': 19,
        'dest': 36,
      },
      'expected_outcome': 1,
    }, {
      'input': {
        'src': 0,
        'dest': 63,
      },
      'expected_outcome': 6,
    }, {
      'input': {
        'src': 1,
        'dest': 0,
      },
      'expected_outcome': 3,
    }, {
      'input': {
        'src': 36,
        'dest': 19,
      },
      'expected_outcome': 1,
    }, {
      'input': {
        'src': 28,
        'dest': 27,
      },
      'expected_outcome': 3,
    }]

    for test_case in test_cases:
      self.assertEqual(
        solution(test_case['input']['src'], test_case['input']['dest']),
        test_case['expected_outcome']
      )
