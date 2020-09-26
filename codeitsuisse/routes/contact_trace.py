import unittest


def contact_trace(n, arrs):
    pass


class Test(unittest.TestCase):

    def test_connect_ropes(self):
        self.assertEqual(24, contact_trace(3, [["12", "12", "3", "X", "3"], ["23", "X", "X", "X", "3"],
                                               ["33", "21", "X", "X", "X"], ["9", "12", "3", "X", "X"],
                                               ["X", "X", "X", "4", "5"]]))

        if __name__ == "__main__":
            unittest.main()
