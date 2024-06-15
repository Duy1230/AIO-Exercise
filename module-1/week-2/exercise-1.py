def find_max_with_window(arr, window_size):

    if not isinstance(window_size, int):
        print("Window size must be an integer")
        return None
    if not isinstance(arr, list):
        print("Input must be a list")
        return None
    for i in arr:
        if not isinstance(i, int):
            print("List elements must be integers")
            return None

    if window_size > len(arr):
        print("Invalid window size")
        return None

    result = [max(sub_array) for sub_array in [arr[i: i+window_size]
                                               for i in range(len(arr) - window_size + 1)]]
    return result


if __name__ == "__main__":
    arr = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    window_size = 3
    print(find_max_with_window(arr, window_size))
