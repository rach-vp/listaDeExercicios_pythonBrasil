# Recebe dois e imprime a soma dos dois

n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')

try:
    n1 = int(n1)
    n2 = int(n2)
    print (f"{n1} + {n2} = {n1 + n2}")
except ValueError:
    if (type(n1) == str): #quer dizer que n2 foi convertido para int sem problemas
        print(f"{n1} não é um número!. Tente novamente.")
    elif (type(n2) == str): #quer dizer que n1 foi convertido para int sem problemas
        print(f"{n2} não é um número!. Tente novamente.")
    else:
        print(f"{n1} e {n2} não são números! Tente novamente")