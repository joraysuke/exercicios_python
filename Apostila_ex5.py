
def soma_dos_digitos (string):
    inteiros = [int(s) for s in string if s.isdigit()]
    return sum(inteiros)

numero = input('Digite um número: ')
resultado = soma_dos_digitos(numero)
print(f'A soma dos numeros é: {resultado}')
