import unittest


def clean_floor(tests):
    print(tests.items())
    return {k: clean(v["floor"]) for k, v in tests.items()}


def clean(arr):
    first_one = None
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] == 1:
            first_one = i
            break

    return sum(arr[:first_one + 1])


class Test(unittest.TestCase):

    def test_connect_ropes(self):
        self.assertEqual(1, clean_floor([0, 1]))
        self.assertEqual(2, clean_floor([1, 1]))


if __name__ == "__main__":
    unittest.main()
