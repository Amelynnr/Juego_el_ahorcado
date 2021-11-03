import random

def getWord():
    with open("./data.txt","r",encoding='utf-8') as words:
        word = random.choice(words.readlines())
        print(word)


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
    getWord()


if __name__ == "__main__":
    main()