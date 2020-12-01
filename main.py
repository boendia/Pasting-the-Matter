import discord
import asyncio
import random

client = discord.Client()


@client.event
async def on_ready():
    print('BOT ONLINE - OLÁ MUNDO')
    print("Selecione a matéria que deseja uma cola: "
          "MATEMATICA"
          "PORTUGUES"
          "HISTORIA"
          "GEOGRAFIA"
          "BIOLOGIA"
          "INGLES")
    print(client.user.name)
    print(client.user.id)
    print('-----ONLINE------')


@client.event
async def on_message(message):
    if message.content.lower().startswith('?matematica'):
        print("Selecine o tópico abaixo: "
              "FUNÇÕES"
              "FRAÇÕES")
        if message.content.lower().startswith('?funções'):
            print(" FUNÇÃO: Uma função é uma regra que relaciona cada elemento de um conjunto a um único elemento de outro."
                  " O primeiro conjunto é chamado de domínio, e o segundo, contradomínio da função."
                  "A função determina uma relação entre os elementos de dois conjuntos. Podemos defini-la utilizando uma lei de formação, "
                  "em que, para cada valor de x, temos um valor de f(x). Chamamos x de domínio e f(x) ou y de imagem da função. "
                  "A formalização matemática para a definição de função é dada por: "
                  "Seja X um conjunto com elementos de x e Y um conjunto dos elementos de y, temos que: f: x → y")

            print("TIPOS DE FUNÇÕES: "
                  "Função injetora ou injetiva"
                  "Função Sobrejetora ou sobrejetiva"
                  "Função bijetora ou bijetiva"
                  "Agora escolha a função que deseja =)")

            if message.content.lower.startswith('?Função injetora ou injetiva'):
                print("Nessa função, cada elemento do domínio (x) associa-se a um único elemento da imagem f(x). "
                      "Todavia, podem existir elementos do contradomínio que não são imagem. "
                      "Quando isso acontece, dizemos que o contradomínio e imagem são diferentes. Veja um exemplo:"
                      "Conjunto dos elementos do domínio da função: D(f) = {-1,5, +2, +8}"
                      "Conjunto dos elementos da imagem da função: Im(f) = {A, C, D}"
                      "Conjunto dos elementos do contradomínio da função: CD(f) = {A, B, C, D}")

            if message.content.lower.startswith('?Função Sobrejetora ou sobrejetiva'):
                print("Na função sobrejetiva, todos os elementos do domínio possue um elemento na imagem. "
                      "Pode acontecer de dois elementos do domínio possuírem a mesma imagem. "
                      "Nesse caso, imagem e contradomínio possuem a mesma quantidade de elementos."
                      "Conjunto dos elementos do domínio da função: D(f) = {-10, 2, 8, 25}"
                      "Conjunto dos elementos da imagem da função: Im (f) = {A, B, C}"
                      "Conjunto dos elementos do contradomínio da função: CD (f) = {A, B, C}")

            if message.content.lower.startswith('?Função bijetora ou bijetiva'):
                print("Essa função é ao mesmo tempo injetora e sobrejetora, pois, cada elemento de x relaciona-se a um único elemento de f(x). "
                      "Nessa função, não acontece de dois números distintos possuírem a mesma imagem, e o contradomínio e a imagem possuem "
                      "a mesma quantidade de elementos."
                      "Conjunto dos elementos do domínio da função: D(f) = {-12, 0, 1, 5}"
                      "Conjunto dos elementos da imagem da função: Im (f) = {A, B, C, D}"
                      "Conjunto dos elementos do contradomínio da função: CD (f) = {A, B, C, D}")



        if message.content.lower().startswith('?frações'):
            print("Na matemática, as frações correspondem a uma representação das partes de um todo. "
                  "Ela determina a divisão de partes iguais sendo que cada parte é uma fração do inteiro. "
                  "Como exemplo podemos pensar numa pizza dividida em 8 partes iguais, sendo que cada fatia corresponde a 1/8 (um oitavo) de seu total. "
                  "Se eu como 3 fatias, posso dizer que comi 3/8 (três oitavos) da pizza."
                  "Importante lembrar que nas frações, o termo superior é chamado de numerador enquanto o termo inferior é chamado de denominador.")
            print("Tipos de Frações: "
                  "Fração Própria"
                  "Fração Imprópria"
                  "Fração Aparente"
                  "Fração Mista"
                  "Você pode se interessar também por operações com frações, digitando ?operações, ou é só escolher o tipo de fração acima =)")

            if message.content.lower().startswith('?Fração Própria'):
                print("São frações em que o numerador é menor que o denominador, ou seja, representa um número menor que um inteiro. "
                      "Ex: 2/7")

            if message.content.lower().startswith('?Fração Imprópria'):
                print("São frações em que o numerador é maior, ou seja, representa um número maior que o inteiro. "
                      "Ex: 5/3")

            if message.content.lower().startswith('?Fração Aparente'):
                print("São frações em que o numerador é múltiplo ao denominador, ou seja, representa um número inteiro escrito em forma de fração. "
                      "Ex: 6/3= 2")

            if message.content.lower().startswith('?Fração Mista'):
                print("É constituída por uma parte inteira e uma fracionária representada por números mistos. "
                      "Ex: 1 2/6. (um inteiro e dois sextos)")

            if message.content.lower().startswith('?operações'):
                print("Selecione o tipo de operação abaixo que deseja: "
                      "ADIÇÃO"
                      "SUBTRAÇÃO"
                      "")



    if message.content.lower().startswith('?portugues'):
        print("Selecine o tópico abaixo: "
              "GRAMATICA"
              "LITERATURA")
        if message.content.lower().startswith('?gramatica'):

        if message.content.lower().startswith('?literatura'):

    if message.content.lower().startswith('?historia'):
        print("Selecine o tópico abaixo: "
              "BRASIL COLONIA"
              "2ª GUERRA MUNDIAL")
        if message.content.lower().startswith('?brasil colonia'):

        if message.content.lower().startswith('?2 guerra mundial'):

    if message.content.lower().startswith('?geografia'):
        print("Selecine o tópico abaixo: "
              "ESTADOS E CAPITAIS"
              "AMERICA DO SUL")
        if message.content.lower().startswith('?estados e capitais'):

        if message.content.lower().startswith('?america  do sul'):

    if message.content.lower().startswith('?biologia'):
        print("Selecine o tópico abaixo: "
              "corpo humano"
              "celulas")
        if message.content.lower().startswith('?corpo humano'):

        if message.content.lower().startswith('?celulas'):

    if message.content.lower().startswith('?ingles'):
        print("Selecine o tópico abaixo: "
              "GRAMATICA"
              "TEXTO")
        if message.content.lower().startswith('?gramatica'):

        if message.content.lower().startswith('?texto'):
client.run('68c32b2e584faf1f1b3c4855451a0a9934f5e5ab40f3c66b0f78245c44d45cd7')