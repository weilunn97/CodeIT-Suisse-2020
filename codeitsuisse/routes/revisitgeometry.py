import unittest

ROUND_LIMIT = 0.01


class Line:
    def __init__(self, m, c, xmin, xmax, ymin, ymax, x_intercept=None):
        self.m = m
        self.c = c
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.x_intercept = x_intercept


def revisitgeometry(shape_coords, line_coords):
    shape_lines = get_shape_lines(shape_coords)
    line = get_line(line_coords)
    itxs = []
    for sl in shape_lines:
        itx = get_intersection_point(line, sl)
        itx[0] = int(itx[0]) if itx[0] == int(itx[0]) else round(itx[0], 2)
        itx[1] = int(itx[1]) if itx[1] == int(itx[1]) else round(itx[1], 2)
        print(f"y = {line.m}x + {line.c} | y = {sl.m}x + {sl.c}/{sl.x_intercept}| INTERSECTION : {itx}")
        if itx is not None and lies_on_line(itx, sl):
            print("LIES ON LINE")
            itxs.append(itx)
    print('\n----------------------------------------------------------------------\n')
    return [{'x': itx[0], 'y': itx[1]} for itx in itxs]


def get_line(line_coords):
    p1 = [line_coords[0]['x'], line_coords[0]['y']]
    p2 = [line_coords[1]['x'], line_coords[1]['y']]
    m, c = get_mc(p1, p2)
    return Line(m, c, -2 ** 64, 2 ** 64, -2 ** 64, 2 ** 64)


def get_shape_lines(shape_coords):
    shape_lines = []
    shape_coords.append(shape_coords[0])
    for i in range(1, len(shape_coords)):
        p1 = [shape_coords[i - 1]['x'], shape_coords[i - 1]['y']]
        p2 = [shape_coords[i]['x'], shape_coords[i]['y']]
        m, c = get_mc(p1, p2)

        if c is None:
            shape_lines.append(Line(m, c,
                                    p1[0], p1[0],
                                    min(p1[1], p2[1]), max(p1[1], p2[1]),
                                    p1[0]))
        else:
            shape_lines.append(Line(m, c,
                                    min(p1[0], p2[0]), max(p1[0], p2[0]),
                                    min(p1[1], p2[1]), max(p1[1], p2[1])))
    return shape_lines


def get_mc(p1, p2):
    if p2[0] - p1[0] == 0: return 2 ** 64, None
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    c = p1[1] - m * p1[0]  # c = y - mx, using (x1, y1)
    return m, c


def get_intersection_point(l1, l2):
    if l1.m == l2.m:
        return None

    # CHECK IF ONE OF THEM IS VERTICAL
    if l1.c is None:
        x = l1.x_intercept
        y = l2.m * x + l2.c
        return [x, y]

    if l2.c is None:
        x = l2.x_intercept
        y = l1.m * x + l1.c
        return [x, y]

    # SOLVE FOR X-INTERSECTION (M1X + C1 = M2X + C2)
    x = (l2.c - l1.c) / (l1.m - l2.m)
    y = l1.m * x + l1.c
    return [x, y]


def lies_on_line(p, l):
    # CHECK FOR VERTICAL LINE
    if l.c is None:
        print(l.x_intercept - ROUND_LIMIT, p[0], l.x_intercept + ROUND_LIMIT)
        return l.x_intercept - ROUND_LIMIT <= p[0] <= l.x_intercept + ROUND_LIMIT and l.ymin <= p[1] <= l.ymax

    # PROCEED AS USUAL
    if not (l.m * p[0] + l.c - ROUND_LIMIT <= p[1] <= l.m * p[0] + l.c + ROUND_LIMIT):
        return False
    return l.xmin <= p[0] <= l.xmax and l.ymin <= p[1] <= l.ymax


class Test(unittest.TestCase):

    def test_connect_ropes(self):
        self.assertEqual(
            [
                {"x": 72, "y": 108},
                {"x": 45.52, "y": 97.41}
            ],
            revisitgeometry(
                [
                    {"x": 21, "y": 70},
                    {"x": 72, "y": 70},
                    {"x": 72, "y": 127}
                ],
                [
                    {"x": -58, "y": 56},
                    {"x": -28, "y": 68}
                ]))

        self.assertEqual(
            [
                {"x": 60, "y": -18},
                {"x": 71, "y": -4.25}
            ],
            revisitgeometry(
                [
                    {"x": -21, "y": -18},
                    {"x": 71, "y": -18},
                    {"x": 71, "y": 71},
                    {"x": -21, "y": 71}
                ],
                [
                    {"x": 68, "y": -8},
                    {"x": 108, "y": 42}
                ]))

        self.assertEqual(
            [],
            revisitgeometry(
                [
                    {"x": 63, "y": 26},
                    {"x": 115, "y": 26},
                    {"x": 115, "y": 54},
                    {"x": 63, "y": 54}
                ],
                [
                    {"x": -88, "y": 85},
                    {"x": -58, "y": 97}
                ]))


if __name__ == "__main__":
    unittest.main()
