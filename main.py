# importations des fonctions du fichier stats
# stats est le nom du fichier contenant les fonctions.
from stats import get_book_text, count_number_of_words, count_cars


def main():
  book = "./books/frankenstein.txt"
  content_book = get_book_text(book) 
  num_words = count_number_of_words(content_book)
  dict_caract = count_cars(content_book, num_words)
  print(dict_caract)
main()