def get_book_text(filePath):
  with open(filePath) as f:
    file_contents = f.read()
  return file_contents

def count_number_of_words(content):
  list_word = content.split()
  return len(list_word)

def count_cars(content):
  cars = {}
  for key in content:
    lower_caractere = key.lower()
    if lower_caractere.isalpha():
      if lower_caractere in cars:
        cars[lower_caractere] += 1
      else:
        cars[lower_caractere] = 1
  return cars

def get_reports(count_rapport, count_of_char, path_to_book):
  # triage du rapport du plus grand nombre d'occurence au plus petit
  # count_rapport.items() -> convertis le dictionnaire en tuple
  # key=lambda .. creer une fonction anonyme pour le triage
  sorted_item = sorted(count_rapport.items(), key=lambda item: item[1], reverse=True)

  print("============= BOOKBOT =============")
  print(f"Analyzing book found at {path_to_book}")
  print("------------- Word Count ----------")
  print(f"Found {count_of_char} total words")
  print("-------------- Character Count ----")
  for char, count in sorted_item:
    print(f"{char}: {count}")
  print("============= END =================")