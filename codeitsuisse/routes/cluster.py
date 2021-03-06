import unittest


def cluster(m):
    count = 0
    vis = set()
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == '1':
                dfs(m, i, j)
                count += 1
    return count


def dfs(m, i, j):
    if min(i, j) < 0 or i >= len(m) or j >= len(m[0]) or m[i][j] in ['*', '-']:
        return

    m[i][j] = '-'
    dfs(m, i - 1, j - 1)
    dfs(m, i - 1, j)
    dfs(m, i - 1, j + 1)
    dfs(m, i, j + 1)
    dfs(m, i + 1, j - 1)
    dfs(m, i + 1, j)
    dfs(m, i + 1, j + 1)
    dfs(m, i, j - 1)


class Test(unittest.TestCase):

    def test_connect_ropes(self):
        self.assertEqual(2, cluster([
            ["*", "*", "*", "*"],
            ["*", "1", "*", "*"],
            ["*", "*", "*", "*"],
            ["*", "*", "*", "1"],
            ["*", "*", "*", "*"]
        ]))
        self.assertEqual(1, cluster([
            ["*", "*", "*", "*"],
            ["*", "1", "0", "*"],
            ["*", "*", "*", "*"],
            ["*", "*", "0", "0"],
            ["*", "*", "*", "*"]
        ]))
        self.assertEqual(1, cluster([
            ["*", "*", "*", "*"],
            ["*", "1", "0", "*"],
            ["*", "*", "*", "1"],
            ["*", "*", "0", "0"],
            ["*", "*", "*", "*"]
        ]
        ))
        self.assertEqual(1, cluster([
            ["1", "0", "*", "*"],
            ["0", "0", "*", "0"],
            ["*", "*", "0", "*"],
            ["*", "*", "*", "*"],
            ["*", "*", "*", "*"],
            ["*", "0", "0", "*"]
        ]))
        self.assertEqual(2, cluster([
            ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "0", "0", "0", "*", "*", "*", "*", "*"],
            ["*", "*", "1", "*", "*", "*", "*", "*", "*"],
            ["*", "0", "0", "0", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "0", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "0", "0", "*", "*"],
            ["*", "*", "*", "*", "1", "*", "*", "*", "0"],
            ["*", "*", "*", "*", "0", "*", "*", "0", "0"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "*", "1", "0", "0", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*"]
        ]))


if __name__ == "__main__":
    unittest.main()
