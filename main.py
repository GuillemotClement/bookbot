from stats import get_number_of_words

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
    count_words = get_number_of_words(text)

    print(f"{count_words} words found in the document")

main()