def main():
    # ajout du path dans une variable
    book_path = "./books/frankenstein.txt"
    # on stocke le text dans une variable
    text = get_content_file(book_path)
    # on appelle la fonction pour récupérer le nombre de mot dans le text
    count_word = counter_word(text)
    # affichage du nombre de mots
    print("The book have",count_word, " words")

# la fonction permet de récupérer le contenu d'un fichier passé en argument
def get_content_file(path):
  with open(path) as f:
      return f.read()

# la fonction permet de faire le décompte des mots dans un fichier passé en argument
def counter_word(text):
  # on convertis le texte en liste
  list_word = text.split()
  # on retourne la longueur de la liste contenant les mots du text
  return len(list_word)


main()
