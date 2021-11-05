import random

def getWord():
    with open("./data.txt","r",encoding='utf-8') as words:
        word = random.choice(words.readlines())
        return word.strip()

def convertWord():
    secret_word = getWord()
    showed_word = ["-" for letter in secret_word]
    showed_word = " ".join(showed_word)

    print("La palabra incognita", showed_word, " corresponde a", secret_word)

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
                     |  
        """

    print(hangman)

def main():
    template()
    convertWord()

if __name__ == "__main__":
    main()