def main():
    book_path = "./books/frankenstein.txt"
    text = get_content_file(book_path)
    print(text)

def get_content_file(path):
  with open(path) as f:
      return f.read()


main()
