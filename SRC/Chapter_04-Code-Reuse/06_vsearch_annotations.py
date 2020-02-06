def search4vowels(word: str) -> set:
    """ Display any vowel found in an asked-for word. """
    vowels = set("aeiou")
    found = vowels.intersection(set(word))
    for vowels in found:
        print(vowels)


if __name__ == "__main__":
    word = input("Provide a word to search for vowels: ")
    search4vowels(word)
