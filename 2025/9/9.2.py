with open("9.txt", "r") as file:
    lines = file.readlines()

coords = []
for pos in lines:
    x, y = map(int, pos.strip().split(","))
    coords.append((x, y))

red = set(coords)
hull = set()

for i in range(len(coords)):
    x1, y1 = coords[i]
    x2, y2 = coords[(i + 1) % len(coords)]
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            hull.add((x1, y))
    else:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            hull.add((x, y1))

def point_in_polygon(x, y, polygon):
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(1, n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
        p1x, p1y = p2x, p2y
    return inside

pip_cache = {}

def is_valid_tile(x, y):
    if (x, y) in red or (x, y) in hull:
        return True
    if (x, y) not in pip_cache:
        pip_cache[(x, y)] = point_in_polygon(x, y, coords)
    return pip_cache[(x, y)]

def is_rectangle_valid(x1, y1, x2, y2):
    rect_min_x, rect_max_x = min(x1, x2), max(x1, x2)
    rect_min_y, rect_max_y = min(y1, y2), max(y1, y2)
    
    corners = [(rect_min_x, rect_min_y), (rect_max_x, rect_min_y),
               (rect_min_x, rect_max_y), (rect_max_x, rect_max_y)]
    for x, y in corners:
        if not is_valid_tile(x, y):
            return False
    
    polygon_xs = set(x for x, y in coords if rect_min_x <= x <= rect_max_x)
    polygon_ys = set(y for x, y in coords if rect_min_y <= y <= rect_max_y)
    
    for x in polygon_xs:
        if not is_valid_tile(x, rect_min_y) or not is_valid_tile(x, rect_max_y):
            return False
        mid_y = (rect_min_y + rect_max_y) // 2
        if not is_valid_tile(x, mid_y):
            return False
    
    for y in polygon_ys:
        if not is_valid_tile(rect_min_x, y) or not is_valid_tile(rect_max_x, y):
            return False
        mid_x = (rect_min_x + rect_max_x) // 2
        if not is_valid_tile(mid_x, y):
            return False
    
    center_x = (rect_min_x + rect_max_x) // 2
    center_y = (rect_min_y + rect_max_y) // 2
    if not is_valid_tile(center_x, center_y):
        return False
    
    return True

max_area = 0
for i, (x1, y1) in enumerate(coords):
    for j in range(i + 1, len(coords)):
        x2, y2 = coords[j]
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        if area > max_area and is_rectangle_valid(x1, y1, x2, y2):
            max_area = area

print(max_area)