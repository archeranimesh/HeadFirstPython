def search4letters(phrase: str, letters: str) -> set:
    """ Retuns a set of the letters found in phrase. """
    return set(letters).intersection(set(phrase))


if __name__ == "__main__":
    word = input("Provide a word to search for vowels: ")
    # invoked using a positional arguments
    print(search4letters(word, "aeiou"))
    # invoked using keyword arguments.
    print(search4letters(letters="aeiou", phrase=word))
