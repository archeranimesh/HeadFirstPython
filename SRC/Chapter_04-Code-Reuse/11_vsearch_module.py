import vsearch


if __name__ == "__main__":
    word = input("Provide a word to search for vowels: ")
    print(vsearch.search4letters(word, "aeiou"))
