def main():
    book_path = "./books/frankenstein.txt"
    text = get_content_file(book_path)
    count_word = counter_word(text)
    count_caracter = get_number_cara(text)
    list_dict = convert_to_list_dict(count_caracter)
    list_dict.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_word} words found in the document")
    for item in list_dict:
      if get_letter(item['letter']):
        print(f"The '{item['letter']}' character was found {item['count']} times")
    print("--- End report ---")

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

# comptage des caractères du text
def get_number_cara(text):
  text = text.lower()
  number_cara = {}
  for caractere in text:
    if caractere not in number_cara:
      number_cara[caractere] = 1
    else:
      number_cara[caractere] += 1
  return number_cara

# permet de venir afficher que les lettres
def get_letter(letter):
  return letter.isalpha()

# convertion du dictionnaire en liste de dictionnaire
def convert_to_list_dict(dict):
  list_dict = []
  for item in dict:
    list_dict.append({"letter": item, "count": dict[item]})
  return list_dict

# fonction de triage du dictionnaire par nombre d'occurence (+ à -)
def sort_on(dict):
  return dict['count']


main()
