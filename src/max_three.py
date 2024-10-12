def max_three(input):
    largest_triplet = 1
    for i in range(len(input) - 2):
        for j in range(1, len(input) - 1):
            for k in range(2, len(input)):
                product = input[i] * input[j] * input[k]
                print(f"product: {product}")
                if product > largest_triplet:
                    largest_triplet = product
    return largest_triplet


if __name__ == '__main__':
    input1 = [1, 3, 4, 5]
    # input2 = [−4, −2, 3, 5]
    input3 = [-5, 5, 2, 1]
    print(input3)
    print(max_three(input3))