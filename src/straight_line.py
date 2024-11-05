def on_straight_line(points):
    # the points are in a straight line if slopes are the same
    # and same for y
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]

    denominator1 = x2 - x1
    denominator2 = x3 - x2

    if denominator1 == 0:
        denominator1 = 1
    if denominator2 == 0:
        denominator2 = 1

    m1 = (y2 - y1) / denominator1
    m2 = (y3 - y2) / denominator2

    return m1 == m2
    # need to account for them being the same


if __name__ == "__main__":
    print(on_straight_line([[0, 1], [1, 2], [2, 3]]))