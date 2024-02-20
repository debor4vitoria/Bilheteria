import os
os.system("cls")

idade = int(input("digite sua idade: "))

if idade < 4 or idade > 60 and idade >= 1:
    print(" ingresso gratuito\n")
elif idade >= 4 and idade < 18:
    print ("ingresso 20reais\n")
else:
    print("ingresso 30reais\n")
