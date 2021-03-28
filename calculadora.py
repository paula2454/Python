# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************\n")
print("Selecione o número da operação desejada:\n")
print("1 = Soma")
print("2 = Subtração")
print("3 = Multiplicação")
print("4 = Divisão")

operacao = int(input("\nDigite sua opção (1/2/3/4): "))

num1 = float(input("\nDigite o primeiro número: "))
num2 = float(input("\nDigite o segundo número: "))

if operacao == 1:
	print(num1, "+", num2,"=", num1 + num2)
elif operacao == 2:
	print(num1, "-", num2,"=",num1 - num2)
elif operacao == 3:
	print(num1, "*", num2,"=",num1 * num2)
elif operacao == 4:
	print(num1, "/", num2,"=",num1/num2)
else:
	print ("Operação Invalida!")

