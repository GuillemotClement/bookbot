from stats import get_number_of_words, get_chars_dict

def get_book_text(filepath):
    # ouvre le fichier
    with open(filepath) as f:
        # retourne le contenu du fichier
        return f.read()



def main():
    # definition du path vers le document
    book_path = "./books/frankenstein.txt"
    # recuperation du content
    text = get_book_text(book_path)
    # appelle de la fonction pour retourner le nombre de mots du texte
    num_words = get_number_of_words(text)
    # appelle de la fonction qui stats les characteres
    char_dict = get_chars_dict(text)

    print(f"{num_words} words found in the document")
    print(char_dict)

main()