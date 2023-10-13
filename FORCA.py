import random
loop = True
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def boneco(chances):
    if chances == 6:
        return f'___'
    if chances == 5:
        return f'___\n   O'
    if chances == 4:
        return f'___\n   O \n   |'
    if chances == 3:
        return f'___\n   O \n  /|'
    if chances == 2:
        return f'___\n   O \n  /|\ '
    if chances == 1:
        return f'___\n   O \n  /|\\\n  / '
    if chances == 0:
        return f'___\n   O \n  /|\\\n  /\ '
while loop:
    print('===============JOGO DA FORCA===============')
    frutas = ['MORANGO', 'ABACAXI', 'MAMAO', 'PERA', 'UVA', 'MANGA']
    objetos = ['FACA', 'TESOURA', 'LAPIS', 'PORTA']
    transporte = ['CARRO', 'AVIAO', 'TREM', 'NAVIO']
    paises = ['BRASIL', 'VENEZUELA', 'ESPANHA', 'INGLATERRA', 'COLOMBIA']
    todasAsPalavras = frutas + objetos + transporte + paises
    palavra = random.choice(todasAsPalavras)
    if palavra in frutas:
        dica = 'Dica: é uma fruta.'
    if palavra in objetos:
        dica = 'Dica: é um objeto.'
    if palavra in transporte:
        dica = 'Dica: é um meio de transporte.'
    if palavra in paises:
        dica = 'Dica: é um país.'
    chances = 6
    acertos = []
    erros = []
    def palavraOculta(palavra, acertos):
        resultado = ''
        for letra in palavra:
            if letra in acertos:
                resultado += letra + ' '
            else:
                resultado += '_ '
        return resultado
    while chances > 0:
        print(dica)
        print(f'{palavraOculta(palavra, acertos)}')
        print(f'Letras erradas: {", ".join(erros)}')
        while True:
            tentativa = input('• Digite uma letra: ').upper()
            c = 0
            for x in tentativa:
                if x not in alfabeto:
                    c += 2
                c += 1
            if c > 1:
                print('Você digitou mais de uma letra ou um caractere inválido. Tente novamente!')
            elif tentativa in acertos or tentativa in erros:
                print(f'A letra {tentativa} já foi digitada, tente novamente!')
            else:
                break
        if tentativa in palavra:
            acertos.append(tentativa)
            if all(letra in acertos for letra in palavra):
                print(f'Parabéns, você ganhou! A palavra era: {palavra}.')
                break
        else:
            erros.append(tentativa)
            chances -= 1
            print(f'Letra incorreta.')
        print(boneco(chances))
    if chances == 0:
        print(f'Você perdeu! A palavra era: {palavra}.')
    questao = input('Deseja jogar novamente? (s/n): ')
    if questao.lower() == 'n':
        loop = False
    print('Programa finalizado! Obrigado por jogar.')