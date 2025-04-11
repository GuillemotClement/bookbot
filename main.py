def get_book_text(filePath):
  with open(filePath) as f:
    file_contents = f.read()
  return file_contents

def count_number_of_words(content):
  list_word = content.split()
  return len(list_word)

def main():
  content_book = get_book_text('./books/frankenstein.txt') 
  num_words = count_number_of_words(content_book)
  print(f"{num_words} words found in the document")

main()