def supermarket(tests):
    d = {k: solve(v["maze"], v["start"][::-1], v["end"][::-1]) for k, v in tests.items()}
    return {k: v if v < 2 ** 64 else -1 for k, v in d.items()}


def solve(m, s, e, steps=0, vis=set()):
    if min(s[0], s[1]) < 0 or s[0] >= len(m) or s[1] >= len(m[0]) or \
            tuple(s) in vis or m[s[0]][s[1]] == 1 or m[e[0]][e[1]] == 1:
        return 2 ** 64
    if s == e:
        return steps + 1

    vis.add(tuple(s))
    soln = min(solve(m, [s[0] - 1, s[1]], e, steps + 1, vis),
               solve(m, [s[0] + 1, s[1]], e, steps + 1, vis),
               solve(m, [s[0], s[1] - 1], e, steps + 1, vis),
               solve(m, [s[0], s[1] + 1], e, steps + 1, vis))
    vis.remove(tuple(s))
    return soln
