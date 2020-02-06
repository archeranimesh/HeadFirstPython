def search4vowels(word):
    """ Display any vowel found in an asked-for word. """
    vowels = set("aeiou")
    found = vowels.intersection(set(word))
    return bool(found)


if __name__ == "__main__":
    word = input("Provide a word to search for vowels: ")
    print(search4vowels(word))
