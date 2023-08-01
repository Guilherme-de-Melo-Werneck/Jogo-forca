import random

def jogar_forca():
    palavras = ['programação', 'algoritmo', 'desenvolvimento', 'software', 'hardware', 'banco de dados', 'cibersegurança', 'rede', 'web', 'inteligência artificial']
    palavra_secreta = random.choice(palavras)
    letras_descobertas = ['_'] * len(palavra_secreta)
    tentativas = 10
    letras_erradas = []

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra secreta. Boa sorte!")

    while True:
        print("\n")
        for letra in letras_descobertas:
            print(letra, end=" ")
        print("\n")

        letra_digitada = input("Digite uma letra: ").lower()

        if len(letra_digitada) != 1:
            print("Por favor, digite apenas uma letra.")
            continue

        if letra_digitada in letras_erradas or letra_digitada in letras_descobertas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra_digitada in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra_digitada:
                    letras_descobertas[i] = letra_digitada
        else:
            letras_erradas.append(letra_digitada)
            tentativas -= 1
            print("Letra errada. Você tem", tentativas, "tentativas restantes.")

        if '_' not in letras_descobertas:
            print("\nParabéns! Você acertou a palavra secreta:", palavra_secreta)
            break

        if tentativas == 0:
            print("\nVocê perdeu! A palavra secreta era:", palavra_secreta)
            break

jogar_forca()