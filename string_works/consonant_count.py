


def consonant_count(word):

    c_count=0

    VOWELS="aeiou"

    for ch in word.casefold():

        if ch not in VOWELS and ch.isalpha():

            c_count+=1

    return c_count

print(consonant_count("hello123"))



# create function display_vowel_and_cosonant_count with parameter word
# print count of consonants and vowels


# pangram

# word="the qucik brown fox jumps over lazy dog"


# creata function is_pangram with one parameter word
# function should return True if word is pangram return false otherwise

