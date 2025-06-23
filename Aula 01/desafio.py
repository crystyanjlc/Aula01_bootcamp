#Desafio
#Escreva um programa em Python que solicita ao usuário para digitar seu nome, 
# o valor do seu salário mensal e o valor do bônus que recebeu. 
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando 
# o valor do salário em comparação com o bônus recebido.

constante = 1000

a = input("Informe o seu nome:")
b = float(input("Informe o valor do seu salário mensal:"))
c = float(input("Informe o percentual de reajuste recebido:"))
d =  constante + b * c

print("Seja bem vindo " + a)
print(f"Seu salário é -  {b} . Em atingindo suas metas irá receber - {c}  de reajuste, ficando o total em -  {d}" )