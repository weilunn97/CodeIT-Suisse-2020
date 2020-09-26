import unittest
from collections import deque


def inventory_mgmt(name, items):
    finals = []
    for item in items:
        ops, final = convert(name, item)
        finals.append([ops, final])
    return [final[-1] for final in sorted(finals)]


def convert(src, dst):
    # KEEP TRACK OF [MIN_OPS, PARENT, STRING]
    dp = [[[0, None, None] for _ in range(len(dst) + 1)] for _ in range(len(src) + 1)]
    nrows, ncols = len(dp), len(dp[0])

    # ROW 0
    for j in range(1, ncols):
        dp[0][j][0] = j
        dp[0][j][1] = [0, j - 1]
        dp[0][j][2] = f"+{dst[j - 1]}"

    # COL 0
    for i in range(1, nrows):
        dp[i][0][0] = i
        dp[i][0][1] = [0, i - 1]
        dp[i][0][2] = f"-{src[i - 1]}"

    # OTHER CELLS
    for i in range(1, nrows):
        for j in range(1, ncols):

            if src[i - 1].lower() == dst[j - 1].lower():
                dp[i][j][0] = dp[i - 1][j - 1][0]
                dp[i][j][1] = [i - 1, j - 1]
                dp[i][j][2] = f"{src[i - 1]}"

            else:
                min_ops = min(dp[i - 1][j][0], dp[i][j - 1][0], dp[i - 1][j - 1][0])
                dp[i][j][0] = 1 + min_ops

                # DELETE (UP)
                if dp[i - 1][j][0] == min_ops:
                    dp[i][j][1] = [i - 1, j]
                    dp[i][j][2] = f"-{src[i - 1]}"

                # INSERT (LEFT)
                elif dp[i][j - 1][0] == min_ops:
                    dp[i][j][1] = [i, j - 1]
                    dp[i][j][2] = f"+{dst[j - 1]}"

                # REPLACE (TOP-LEFT)
                else:
                    dp[i][j][1] = [i - 1, j - 1]
                    dp[i][j][2] = f"{dst[j - 1]}"

    return dp[-1][-1][0], get_path(dp)


def get_path(dp):
    # for row in dp:
    #     print([r[2] for r in row])

    curr = dp[-1][-1]
    path = deque([])
    while curr[2] is not None:
        path.appendleft(curr[2])
        xy = curr[1]
        curr = dp[xy[0]][xy[1]]
    return ''.join(path)


class Test(unittest.TestCase):

    def test_connect_ropes(self):
        # self.assertEqual(["ACO-YZ"], inventory_mgmt("ABOYZ", ["ACOZ"]))
        self.assertEqual(["-Samsung+h Aircon", "Samsung+a Air-con", "S-ams-ung Au-r-con"],
                         inventory_mgmt("Samsung Aircon", ["Smsng Auon", "Amsungh Aircon", "Samsunga Airon"]))


if __name__ == "__main__":
    unittest.main()
