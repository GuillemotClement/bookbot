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
    # affichage du content
    print(text)

main()