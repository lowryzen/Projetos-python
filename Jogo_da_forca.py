#jogo da forca

def jogo_forca():
    import random

    palavra = ("Banana", "Sapato","Tesoura", "Macaco", "Mousse", "Tiranossauro rex")
    aleatorio = random.choice(palavra)

    pergunta = str(input("Deseja jogar?: ")).capitalize()
    resposta= str(input("321"))

    if pergunta == ("Sim"): 
        for cadaletra in aleatorio:
            print (cadaletra.replace(cadaletra, "_"), end=" ")
            
    else:
        None


if __name__ == "__main__":
    jogo_forca()
    
    