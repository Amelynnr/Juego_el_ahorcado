import random

def getWord():
    with open("./data.txt","r",encoding='utf-8') as words:
        word = random.choice(words.readlines())
        return word.strip()
        

def convertWord():
    global secret_word
    global showed_word
    secret_word = getWord()
    showed_word = ["-" for letter in secret_word]

    print("La palabra incognita", " ".join(showed_word), "corresponde a", secret_word)

def play():

    while "-" in showed_word:
        letter = input("ingresa una letra porfavor: ")
        for i in range(len(secret_word)):
            if letter == secret_word[i]:
                showed_word[i] = secret_word[i]
            else:
                continue
        
        print(" ".join(showed_word))
        play()
        

def template():

    hangman = """

    ¡Se bienvenido a HANGMAN! mi propia versión de como salvar
    a un incauto de la horca. 

     _ _ _ _ _ _ _ _ _ 
            |      \ |
            |       \|
           __~       |
          (°_°)      |
           ---       |
           /|\       |
            |        |
            |        |
           / \       |
    _ _ _=======_ _ _|
                     |     
                     |
        """

    print(hangman)


def main():
    template()
    convertWord()
    play()

if __name__ == "__main__":
    main()