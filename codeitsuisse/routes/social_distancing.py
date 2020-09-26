import unittest


def social_distancing(tests):
    return {k: solve(v['seats'], v['people'], v['spaces']) for k, v in tests.items()}


def solve(seats, people, spaces, memo=dict()):
    c = (seats, people)

    # if memo.get(c) is not None:
    #     return memo[c]

    if seats <= 0:
        return 0

    if people <= 1:
        return seats

    # CHOOSE TO SEAT A PERSON HERE, OR NOT
    memo[c] = solve(seats - 1 - spaces, people - 1, spaces, memo) + \
              solve(seats - 1, people, spaces, memo)
    return memo[c]


class Test(unittest.TestCase):

    def test_connect_ropes(self):
        self.assertEqual(20, solve(8, 3, 1))
        self.assertEqual(10, solve(7, 3, 1))
        self.assertEqual(6, solve(6, 2, 2))


if __name__ == "__main__":
    unittest.main()
