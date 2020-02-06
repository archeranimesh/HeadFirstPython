def search4vowels(word):
    """ Display any vowel found in an asked-for word. """
    vowels = set("aeiou")
    return vowels.intersection(set(word))


if __name__ == "__main__":
    word = input("Provide a word to search for vowels: ")
    print(search4vowels(word))
