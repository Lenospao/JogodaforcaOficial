import random
import time
palavras = ['banana', 'calabresa', 'piriquito', 'feijao','arroz','macarronada','pizza']
palavras_secreta = random.choice(palavras).lower()
letras_descobertas = []
tentativas = 6
jogador = 0
erros = 0

print('=-'*30)
print('\033[31m''BEM-VINDO AO JOGO DA FORCA')
print('=-'*30)
print('\033[32m BORA JOGAR ?')
jogar = input('\033[31m (SIM/NÂO)' ).strip () .upper()
print()
if jogar in ('SIM ','s','S','sim'):
    print('\033[32m Então que começe a partida!!! VOCÊ TEM APENAS 6 CHANCES PARA ACERTAR, BOA SORTE !!')
    time.sleep(3)
    print()
    print('\033[32m Estou pensando em uma palavra...\033[m')
    time.sleep(3)
    print()
    print('\033[34m''Palavra escolhida!!!\033[m')
else:
    print('\033[34m''Pó crê, me deixou chateado por não querer jogar comigo :(')
    exit()
print(f'A palavra tem {len(palavras_secreta)} letras')

def tabela(erros, palavra,letras_descobertas):
    if erros == 0:
        print()
        print("|----- ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
        print(mostra_letras_descobertas(letras_descobertas, palavra))
        print()
    
    elif erros == 1:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|      ")
        print("|      ")
        print("|      ")
        print(mostra_letras_descobertas(letras_descobertas, palavra))
        print()

    elif erros == 2:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|    | ")
        print("|    | ")
        print("|      ")
        print(mostra_letras_descobertas(letras_descobertas, palavra))
        print()

    elif erros == 3:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|    |\\ ")
        print("|    | ")
        print("|      ")
        print(mostra_letras_descobertas(letras_descobertas, palavra))
        print()

    elif erros == 4:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\\ ")
        print("|    | ")
        print("|      ")
        print(mostra_letras_descobertas(letras_descobertas, palavra))
        print()

    elif erros == 5:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\\ ")
        print("|    | ")
        print("|     \\ ")
        print(mostra_letras_descobertas(letras_descobertas, palavra))
        print()

    elif erros == 6:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\\ ")
        print("|    | ")
        print("|   / \\ ")
        print(mostra_letras_descobertas(letras_descobertas, palavra))
        print()

def mostra_letras_descobertas(letras_descobertas, palavras_secreta):
    resultado = ''
    for caracter in palavras_secreta:
        if lista_possui_letra(letras_descobertas, caracter):
           resultado += caracter
        else:
            resultado += ' _ '
    return resultado   


def pedir_letra():
    while True:
        letra = input('\033[31m Chute uma letra...\033[m')
        if len(letra) > 1:
            print('O apedeuta é só uma letra')
        else:
            return letra


def lista_possui_letra(lista, letra):
    return letra in lista

jogo_encerrou = False
while not jogo_encerrou:
    if erros == 6:
        print('você perdeu!')
    else:
        while True:
            letra = pedir_letra()
            if lista_possui_letra(letras_descobertas, letra):
                print('Você ja chutou essa letra, tente outra.')
            else:
                break

        if lista_possui_letra(palavras_secreta, letra):
            letras_descobertas.append(letra)
            print('Você acertou!!')
        else:
            erros += 1
            print('Você errou!!')

    tabela(erros, palavras_secreta, letras_descobertas)





    