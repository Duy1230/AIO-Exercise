def calculate_substitution_cost(source, target, sub_cost):
    if (source == target):
        return 0
    return sub_cost


def levenstein_distance(source, target, del_cost=1, ins_cost=1, sub_cost=1):
    if not isinstance(s1, str):
        print("s1 must be a string")
        return
    if not isinstance(s2, str):
        print("s2 must be a string")
        return

    len_source = len(source)
    len_target = len(target)

    words_source = list(source)
    words_target = list(target)

    # Create and initialize matrix
    matrix = [[0] * (len_target + 1) for _ in range(len_source + 1)]
    for i in range(len_source + 1):
        matrix[i][0] = i * del_cost
    for j in range(len_target + 1):
        matrix[0][j] = j * ins_cost

    for row in range(1, len_source + 1):
        for col in range(1, len_target + 1):
            val_1 = matrix[row-1][col] + del_cost
            val_2 = matrix[row][col-1] + ins_cost
            val_3 = matrix[row - 1][col - 1] + calculate_substitution_cost(
                words_source[row - 1], words_target[col - 1], sub_cost)

            matrix[row][col] = min(val_1, val_2, val_3)

    return matrix[len_source][len_target]


if __name__ == "__main__":
    s1 = 'hola'
    s2 = 'hello'
    print(levenstein_distance(s1, s2))
