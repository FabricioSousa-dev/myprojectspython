import time
import random
import emoji

f1 = input("Nome do filme: ")
f2 = input("Nome do segundo filme: ")
f3 = input("Nome do terceiro filme: ")
f4 = input("Nome do quarto filme: ")

opcoes = [f1,f2,f3,f4]

print("Os filmes são {}".format(opcoes))

print("Rufem os tambores.......")
time.sleep(4)

roleta = random.choice(opcoes)

print("O filme escolhido foi {}".format(roleta))

