# jogo da forca


def jogo_forca(pontuacao=0):
    import random

    palavra = ("Banana", "Sapato", "Tesoura", "Macaco", "Mousse", "Tiranossauro rex")
    aleatorio = random.choice(palavra)

    pergunta = str(input("Deseja jogar?: ")).capitalize()

    if pergunta == "Sim":
        for cadaletra in aleatorio:
            print(cadaletra.replace(cadaletra, "_"), end=" ")

        print()

        while True:
            resposta = str(input("insira uma letra: "))
            if resposta in aleatorio:
                print (aleatorio.replace(resposta, cadaletra))




    else:
        print ("Tá bom.")

if __name__ == "__main__":
    jogo_forca()

