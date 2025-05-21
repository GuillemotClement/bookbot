def get_number_of_words(data):
    # conversion en split
    list_words = data.split()
    # retourne le nombre de mots dans le texte
    return len(list_words)

def get_chars_dict(text):
    # preparation du dictionnaire
    chars = {}
    # parcours les character du text passer
    for c in text:
        # conversion en minuscule
        lowered = c.lower()
        # ajout dans le dictionnaire
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    # retourne le dictionnaire
    return chars
