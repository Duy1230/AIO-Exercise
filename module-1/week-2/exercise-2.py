def count_words(text):
    if not isinstance(text, str):
        print("text must be a string")
        return

    words = list(text)
    unique_words = set(words)

    apperances = {word: words.count(word) for word in unique_words}

    return apperances


if __name__ == "__main__":
    text = input("Input text: ")
    print(count_words(text))
