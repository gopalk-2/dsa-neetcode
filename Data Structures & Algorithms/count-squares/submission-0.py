class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point):
        self.points[tuple(point)] += 1

    def count(self, point):
        x, y = point
        ans = 0

        for (px, py), cnt in self.points.items():

            if abs(px - x) != abs(py - y) or px == x:
                continue

            ans += (
                cnt *
                self.points.get((px, y), 0) *
                self.points.get((x, py), 0)
            )

        return ans