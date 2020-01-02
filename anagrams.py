import sys

def Check_Anagram(w, w2):
    if len(w) == len(w2):
        if sorted(w) == sorted(w2):
            return True
        else:
            return False

def Search(c_word):
    anag = ""
    #
    file = open(sys.argv[1], "r")
    #
    for i,word in enumerate(file):
        if c_word == word:
            break
        #
        if c_word[:-1] not in anag:
            anag = c_word[:-1] + ": "
        #
        if Check_Anagram(c_word, word) == True:
            anag += word[:-1] + ", "
    print(anag[:-2])
    file.close()

if len(sys.argv) > 1:
    file = open(sys.argv[1], "r")
    for i, word in enumerate(file):
        Search(word)
    file.close()