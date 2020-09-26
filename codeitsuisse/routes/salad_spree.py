import logging
import unittest
from collections import deque

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/salad-spree', methods=['POST'])
def evaluate_salad_spree():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    n, arrs = data.get("number_of_salads"), data.get("salad_prices_street_map")
    result = salad_spree(n, arrs)
    logging.info("My result :{}".format(result))
    return jsonify(result)


def salad_spree(n, arrs):
    min_amt = 2 ** 64
    arrs = [[int(a) if a.isnumeric() else 2 ** 64 for a in arr] for arr in arrs]
    for arr in arrs:
        dq = deque(arr[:n].copy())
        sum_a = sum(dq)
        for i in range(n, len(arr)):
            min_amt = min(min_amt, sum_a)
            sum_a -= dq[0]
            sum_a += arr[i]
            dq.popleft()
            dq.append(arr[i])
    return min_amt if min_amt < 2 ** 64 else 0


class Test(unittest.TestCase):

    def test_connect_ropes(self):
        self.assertEqual(24, salad_spree(3, [["12", "12", "3", "X", "3"], ["23", "X", "X", "X", "3"],
                                             ["33", "21", "X", "X", "X"], ["9", "12", "3", "X", "X"],
                                             ["X", "X", "X", "4", "5"]]))
        self.assertEqual(0, salad_spree(3, [["X", "X", "2"], ["2", "3", "X"], ["X", "3", "2"]]))
        self.assertEqual(5, salad_spree(2, [["2", "3", "X", "2"], ["4", "X", "X", "4"], ["3", "2", "X", "X"],
                                            ["X", "X", "X", "5"]]))


if __name__ == "__main__":
    unittest.main()
