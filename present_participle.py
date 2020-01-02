import sys

def vORc(c):
    vowels = "aeiou"
    if c.lower() in vowels:
        return True #Vowel
    else:
        return False #Consonant

def Check_word(word):
    length = len(word)
    last_char = ""
    sl_char = ""
    tl_char = ""
    n_word = ""
    exceptions = ["be", "see", "flee", "knee"]
    #
    for i,c in enumerate(word):
        if i+1 == length:
            last_char = c
        elif i+1 == length-1:
            sl_char = c
        elif i+1 == length-2:
            tl_char = c
        #
        if vORc(tl_char) == False and vORc(sl_char) == True and vORc(last_char) == False:
            n_word = word + last_char + "ing"
        elif sl_char == "i" and last_char == "e":
            n_word = word[:-2] + "ying"
        elif i+1 == length and last_char == "e":
            if word in exceptions:
                n_word = word + "ing"
            else:
                n_word = word[:-1] + "ing"
        else:
            n_word = word + "ing"
    print(word + " - " + n_word)

if len(sys.argv) > 1:
    Check_word(sys.argv[1])
else:
    Check_word(input("Enter a verb: "))
    