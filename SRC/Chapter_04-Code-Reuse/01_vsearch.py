def search4vowels():
    """ Display any vowel found in an asked-for word. """
    vowels = set("aeiou")
    word = input("Provide a word to search for vowels: ")
    found = vowels.intersection(set(word))
    for vowels in found:
        print(vowels)


if __name__ == "__main__":
    search4vowels()
