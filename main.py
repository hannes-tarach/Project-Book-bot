def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path) 
    word_counter = count_words(text)
    dictionary = count_char(text)
    character_counter = sort_character_frequency(dictionary)  # Ändra?
    print(f"The book contains {word_counter} number of words!")
    for char, count in character_counter:
        print(f"The character '{char}' was found {count} times")


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
    character_frequency = {}
    
    for char in characters:  # Ensure you're iterating over 'characters', the lowercase version of the text
        if char.isalpha():   
            if char in character_frequency:
                character_frequency[char] += 1
            else:
                character_frequency[char] = 1
    return character_frequency    


def sort_character_frequency(dictionary):
    items = dictionary.items()  # List-like object of tuples (character, count)
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)  # Sorts the list of tuples by count in descending order

    return sorted_items



    


if __name__ == "__main__":
    main()

