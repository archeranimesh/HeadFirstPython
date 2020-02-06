def search4vowels(phrase: str) -> set:
    """ Display any vowel found in an asked-for phrase. """
    vowels = set("aeiou")
    found = vowels.intersection(set(phrase))
    for vowels in found:
        print(vowels)


if __name__ == "__main__":
    word = input("Provide a word to search for vowels: ")
    search4vowels(word)
