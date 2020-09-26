import unittest


def contact_trace(infected, origin, cluster):
    traces = []
    for c in cluster:
        s1, s2, s3 = infected["genome"], c["genome"], origin["genome"]
        if related(s1, s2) and related(s1, s3):
            traces.append(f"{infected['name']} -> {c['name']}")
            traces.append(f"{infected['name']} -> {origin['name']}")
        elif related(s1, s2) and related(s2, s3):
            traces.append(f"{infected['name']}* -> {c['name']} -> {origin['name']}")
    return traces


def related(s1, s2):
    return sum([int(c1 != c2) for c1, c2 in zip(s1, s2)]) <= 2


class Test(unittest.TestCase):

    def test_connect_ropes(self):
        self.assertEqual(["orange -> magenta", "orange -> turquoise"], contact_trace(
            {
                "name": "orange",
                "genome": "acg-gcu-uca-gca-acu-ccc-gua-acg-gcu-uca-gca-acu-cac-gaa"
            },
            {
                "name": "turquoise",
                "genome": "acg-gcu-uca-gca-acu-ccc-gua-acg-gcu-uca-gca-acu-cac-gaa"
            },
            [
                {
                    "name": "magenta",
                    "genome": "acg-gcu-uca-gca-acu-ccc-gua-acg-gcu-uca-gca-acu-cac-gaa"
                }
            ]))
        self.assertEqual(["plastic* -> thread -> metal"], contact_trace(
            {
                "name": "plastic",
                "genome": "acg-gcu-uca-gca-acu-ccc-gua-acg-gcu-uca-gca-acu-cac-gaa"
            },
            {
                "name": "metal",
                "genome": "acg-acu-uca-gca-acu-ccc-gua-acg-ccu-uca-gca-acu-cac-gac"
            },
            [
                {
                    "name": "thread",
                    "genome": "acg-acu-uca-gca-acu-ccc-gua-acg-ccu-uca-gca-acu-cac-gaa"
                }
            ]))

        if __name__ == "__main__":
            unittest.main()
