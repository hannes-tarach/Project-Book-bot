def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path) 
    word_counter = count_words(text)
    character_counter = count_char(text)
    print(f"The book contains {word_counter} number of words!")
    print(f"The book contains {character_counter} number of words!")


def get_book_text(path):
    # The with statement works with the open() function to open a file.
    with open(path) as f:
        # f.read() function reads the entire contents of the file as a string and returns it
        return f.read()


# This function takes the text from the book as a string, and returns the number of words in the string.
def count_words(text):
    words = text.split() 
    return len(words)


# Function takes text from the book as a string, and returns the number of times each character appears in the string
def count_char(text):
    characters = text.lower()
    return len(characters)

if __name__ == "__main__":
    main()

