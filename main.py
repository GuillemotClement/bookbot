# importations des fonctions du fichier stats
# stats est le nom du fichier contenant les fonctions.
from stats import get_book_text, count_number_of_words


def main():
  content_book = get_book_text('./books/frankenstein.txt') 
  num_words = count_number_of_words(content_book)
  print(f"{num_words} words found in the document")

main()