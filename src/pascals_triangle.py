def generate(num_rows):
    triangle = []
    for row_num in range(num_rows):
        # Initializing the row all to 1, but except for the beginning and the end,
        # the others will be changed to their actual values
        row = [1] * (row_num + 1)
        # How can you fill (change from 1 to their actual values) the values in the middle?
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
        triangle.append(row)

    print(triangle)
    return triangle


if __name__ == '__main__':
    generate(3)