# Seu código aqui
nome=input("Qual o seu nome?")
idade=int(input("Qual a sua idade?"))
altura=float(input("Qual sua altura?"))

print("[%s]" % nome)
print("[%d]" % idade)
print("[%f]" % altura)
# Seu código aqui
frutas=["Maçã", "Pera", "Uva", "Laranja", "Banana"]
print(frutas)
frutas.pop(1)
print(frutas)

# Seu código aqui
numero=int(input("Digite um valor;"))

if numero>0:
    print("Número positivo!")
    

elif numero<0:
    print("Número negativo!")

else:
    print("Esse número é 0")

    # Seu código aqui

contagem=5
while contagem>0:
    print(contagem)
    contagem=contagem-1
    if contagem==0:
         print("Fogo!")

         # Seu código aqui
print("Digite as 5 notas!")
nota1=int(input("Digite a primeira nota:"))
nota2=int(input("Digite a segunda nota:"))
nota3=int(input("Digite a terceira nota:"))
nota4=int(input("Digite a quarta nota:"))
soma=(nota1+nota2+nota3+nota4)

for s in soma:
    s=s/2
    print(s)

    # Seu código aqui
lista=[1,2,3,4,5,6,7,8,9,10]
print("\n Números pares:")
for par in lista:
    if par %2==0:
        
        print(par)
print("\n Números impares:")
for impar in lista:
    if impar %2==1:
        
        print(impar)

        # Seu código aqui
import random
print("Você tem 3 tentativas!")
palpite=int(input("De um palpite de que número esta por vim de 1 a 10:"))
numeroAleatirio=random.randint(1,10)
tentativas=3

while tentativas>0:
    if palpite==numeroAleatirio:
        print("Acertou na mosca!")
        print("Número aleatorio:",numeroAleatirio)
        print( "Seu palpite:", palpite)
        break


    elif tentativas==0:

        print("Suas tentativas acabaram!")
        break
    else:
        print("tente novamente! Você tem:",tentativas,"Tentativas")
        print("Número aleatorio:",numeroAleatirio)
        print( "Seu palpite:", palpite)
     
        tentativas=tentativas-1
        break

    # Seu código aqui

pesoKG=float(input("Digite o seu peso em KG!"))
alturaM=float(input("Digite a altura em M!"))
nome=input("Digite o seu nome:")
idade=int(input("Qual a sua idade?"))
imc=(pesoKG)/alturaM**2
while True:
    if imc <=16:
        print("\n DADOS PESSOAIS:")
        print("Peso:",pesoKG)
        print("Altura:",alturaM)
        print("Nome:",nome)
        print("Idade:",idade)
        
        print(nome," o seu IMC é:",imc,"Classificação: Magreza grau III")
        break
    elif imc <=16.9:
        print("\n DADOS PESSOAIS:")
        print("Peso:",pesoKG)
        print("Altura:",alturaM)
        print("Nome:",nome)
        print("Idade:",idade)
        print(nome," o seu IMC é:",imc,"Classificação: Magreza grau II")
        break
    elif imc <=18.4:
        print("\n DADOS PESSOAIS:")
        print("Peso:",pesoKG)
        print("Altura:",alturaM)
        print("Nome:",nome)
        print("Idade:",idade)
        print(nome," o seu IMC é:",imc,"Classificação: Magreza grau I")
        break
    elif imc <=24.9:
        print("\n DADOS PESSOAIS:")
        print("Peso:",pesoKG)
        print("Altura:",alturaM)
        print("Nome:",nome)
        print("Idade:",idade)
        print(nome," o seu IMC é:",imc,"Classificação: Eutrofia")
        break
    elif imc <=29.9:
        print("\n DADOS PESSOAIS:")
        print("Peso:",pesoKG)
        print("Altura:",alturaM)
        print("Nome:",nome)
        print("Idade:",idade)
        print(nome," o seu IMC é:",imc,"Classificação: Pré obesidade")
        break
    elif imc <=34.9:
        print("\n DADOS PESSOAIS:")
        print("Peso:",pesoKG)
        print("Altura:",alturaM)
        print("Nome:",nome)
        print("Idade:",idade)
        print(nome," o seu IMC é:",imc,"Classificação: Obesidade modereda (grau I)")
        break
    elif imc <=39.9:
        print("\n DADOS PESSOAIS:")
        print("Peso:",pesoKG)
        print("Altura:",alturaM)
        print("Nome:",nome)
        print("Idade:",idade)
        print(nome," o seu IMC é:",imc,"Classificação: Obesidade severa (grau II)")
        break
    elif imc >=40:
        print("\n DADOS PESSOAIS:")
        print("Peso:",pesoKG)
        print("Altura:",alturaM)
        print("Nome:",nome)
        print("Idade:",idade)
        print(nome," o seu IMC é:",imc,"Obesidade muito severa (grau III)")
        break
    else:
        print("FALSE")
        continue

