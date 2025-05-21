def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "./books/frankenstein.txt"
    data = get_book_text(book_path)
    print(data)

main()