import math
import re
def get_distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

def solve():
    line = input()
    t = int(line.strip())
    for _ in range(t):
        figures = {}
        for _ in range(2):
            line = input().strip()

            # extracting the name and numbers
            match = re.match(r"(\w+)\((.+)\)", line)
            name = match.group(1)
            coords = [float(x) for x in match.group(2).split(", ")]
            figures[name] = coords
        ax, ay, bx, by = figures["rectangle"]
        ox, oy, r = figures['circle']
        vertices = [(ax, ay), (bx, ay), (ax, by), (bx, by)]
        rect_inside_circle = all(get_distance(vx, vy, ox, oy) <= r + 0.01 for vx, vy in vertices)
        if rect_inside_circle:
            print("Rectangle inside circle")
            continue
        circle_inside_rect = (ox - r >= ax - 0.01 and ox + r <= bx + 0.01 and
                              oy + r <= ay + 0.01 and oy - r >= by - 0.01)
        if circle_inside_rect:
            print("Circle inside rectangle")
            continue
        closest_x = max(ax, min(ox, bx))
        closest_y = max(by, min(oy, ay))

        dist_to_closest = get_distance(ox, oy, closest_x, closest_y)

        if dist_to_closest > r + 0.01:
            print("Rectangle and circle do not cross")
        else:
            print("Rectangle and circle cross")
solve()
