# Calculadora em Python
#Codigo atualizado com as clausulas de erro e exceção

print("\n******************* Python Calculator *******************\n")
print("Selecione o número da operação desejada:\n")
print("1 = Soma")
print("2 = Subtração")
print("3 = Multiplicação")
print("4 = Divisão")

while True:
	try:
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
			
	
	except:
		print("Operação Inválida! Tente novamente.")
		continue
	else:
		if operacao not in (1,2,3,4):
			print("Opção Invalida! Digite uma opção valida dentre as abaixo:")
			continue
		else:
			break

