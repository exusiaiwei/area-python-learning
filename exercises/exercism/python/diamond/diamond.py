ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def rows(letter):
    letter = letter.upper()
    for i in ALPHABET:
        if letter == ALPHABET[i]:
            len1 = i
        line1 = "·" * i + letter + "·" * i
