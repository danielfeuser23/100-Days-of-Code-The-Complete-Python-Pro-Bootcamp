'''
Dia 1

Band Name Generator

print() ----> Imprime algo.
print("Hello World!")
>>>Hello World!

\n Serve para pular a linha no print
print("Hello World!\nHello World!")
>>>Hello World!
>>>Hello World!

Variáveis ----> Servem para armazenar informações/valores.
nome = "Daniel"
print(nome)
>>>Daniel

input() ----> Serve para pedir uma informação ao usuário.
nome = input("Qual seu nome?")
print("Olá",nome+"!")
>>>Qual seu nome?
>>>Daniel
>>>Olá Daniel!

len() ----> Serve para contar a quantidade de letras na palavra.
nome = "Daniel"
print(len(nome))
>>>6

Exercício
'''
print("Bem vindo ao gerador de nome de banda.")
cidade = input("Qual cidade você nasceu?\n")
pet = input("Qual o nome do seu pet?\n")
print("O nome da sua banda poderia ser",cidade,pet)
