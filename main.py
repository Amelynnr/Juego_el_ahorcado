import random

def getWord():

    with open("./data.txt","r",encoding='utf-8') as words:
        word = words.readlines()[random.randrange(171)]
        print(word)

def template():
    print("""
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
    """)

def main():
    template()
    getWord()
    

if __name__ == "__main__":
    main()