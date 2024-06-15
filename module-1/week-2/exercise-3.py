def count_words(path):
    if not isinstance(path, str):
        print("path must be a string")
        return

    with open(path, 'r') as file:
        text = file.read()
    text = text.lower().replace("\n", " ").split(" ")
    result = {word: text.count(word) for word in sorted(list(set(text)))}

    return result


if __name__ == "__main__":
    path = 'module-1\week-2\data\P1_data.txt'
    print(count_words(path))
