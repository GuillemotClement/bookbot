def main():
    text = get_content_file("./books/frankenstein.txt")
    print(text)

def get_content_file(path):
  with open(path) as f:
      return f.read()


main()
