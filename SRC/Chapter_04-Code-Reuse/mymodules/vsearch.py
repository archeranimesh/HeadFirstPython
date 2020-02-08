def search4letters(phrase: str, letters: str) -> set:
    """ Retuns a set of the letters found in phrase. """
    return set(letters).intersection(set(phrase))


def search4vowels(phrase: str) -> str:
    """ Return any vowels found in a supplied phrase. """
    vowels = set("aeiou")
    return vowels.intersection(set(phrase))


if __name__ == "__main__":
    word = input("Provide a word to search for vowels: ")
    print(search4letters(word, "aeiou"))
