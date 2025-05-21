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

# fonction pour le triage de la liste
def sort_on(dict):
    return dict["num"]

def char_list(char_dict):
    count_list = []

    for char in char_dict:
        # verifie si le nombre est alphanumerique
        if char.isalpha():
            dict = {
                "name": char,
                "num" : char_dict[char]
            }
            count_list.append(dict)

    # triage
    count_list.sort(reverse=True, key=sort_on)

    return count_list


