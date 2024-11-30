# jogo da forca

def jogo_forca():
    import random

    palavra = ("Banana", "Sapato", "Tesoura", "Macaco", "Mousse", "Tiranossauro rex")
    aleatorio = random.choice(palavra)

    pergunta = str(input("Deseja jogar?: ")).capitalize()

    if pergunta == "Sim":
        for cadaletra in aleatorio:
            print(cadaletra.replace(cadaletra, "_"), end=" ")
        resposta = str(input("insira uma letra: "))
        if resposta == aleatorio:
            print ("Nooooosa")

    else:
        print ("Tá bom.")

if __name__ == "__main__":
    jogo_forca()