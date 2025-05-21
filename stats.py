def get_number_of_words(data):
    # conversion en split
    list_words = data.split()
    # retourne le nombre de mots dans le texte
    return len(list_words)

def count_char(file):
    words = file.split()

    char_count = {}

    for word in words:
        lower_word = word.lower()

        for char in lower_word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count