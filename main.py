# importations des fonctions du fichier stats
# stats est le nom du fichier contenant les fonctions.
from stats import get_book_text, count_number_of_words, count_cars, get_reports
import sys

def main():
  cmd = sys.argv # recuperation des argument depuis le terminal 

  # si le path du livre n'est pas fournis on quitte le programme
  if len(cmd) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)    

  book = cmd[1] # recuperation du livre a analyser dans la commande CLI

  content_book = get_book_text(book) # recuperation du contenu du livre analyser

  num_words = count_number_of_words(content_book) # comptage du nombre de mots

  dict_caract = count_cars(content_book) # comptate des caractere du livre

  get_reports(dict_caract, num_words, book) # genere le rapport dans le terminal

main()