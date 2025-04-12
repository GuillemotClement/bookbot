def get_book_text(filePath):
  with open(filePath) as f:
    file_contents = f.read()
  return file_contents

def count_number_of_words(content):
  list_word = content.split()
  return len(list_word)

def count_cars(content, num_of_cars):
  cars = {}
  for key in content:
    lower_caractere = key.lower()
    if lower_caractere in cars:
      cars[lower_caractere] += 1
    else:
      cars[lower_caractere] = 1

  return cars