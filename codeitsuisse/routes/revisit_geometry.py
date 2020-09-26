import unittest
from pprint import pprint

from shapely.geometry import LineString


def revisit_geometry(shape_coords, line_coords):
    shape = LineString([(l['x'], l['y']) for l in shape_coords])
    line = LineString([(l['x'], l['y']) for l in line_coords])

    pprint(shape.intersection(line))
    return [{'x': p.x, 'y': p.y} for p in line.intersection(shape)]


class Test(unittest.TestCase):

    def test_connect_ropes(self):
        self.assertEqual(
            [
                {"x": 72, "y": 108},
                {"x": 45.52, "y": 97.41}
            ],
            revisit_geometry(
                [
                    {"x": 21, "y": 70},
                    {"x": 72, "y": 70},
                    {"x": 72, "y": 127}
                ],
                [
                    {"x": -58, "y": 56},
                    {"x": -28, "y": 68}
                ]))


if __name__ == "__main__":
    unittest.main()
