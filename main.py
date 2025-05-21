from stats import get_number_of_words, get_chars_dict, char_list
import sys

def get_book_text(filepath):
    # ouvre le fichier
    with open(filepath) as f:
        # retourne le contenu du fichier
        return f.read()

def print_rapport(book_path, num_words, list_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for count in list_count:
        print(f"{count["name"]}: {count["num"]}")

    print("============= END ===============")


def main():
    input = sys.argv

    if len(input) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = input[1]



    # definition du path vers le document
    # book_path = "./books/frankenstein.txt"
    # # recuperation du content
    text = get_book_text(book_path)
    # # appelle de la fonction pour retourner le nombre de mots du texte
    num_words = get_number_of_words(text)
    # # appelle de la fonction qui stats les characteres
    char_dict = get_chars_dict(text)
    # # recuperation de la liste de decompte des charactere
    list = char_list(char_dict)
    #
    print_rapport(book_path, num_words, list)

main()