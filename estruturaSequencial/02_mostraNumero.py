# Recebe um número e imprime a seguinte mensagem "O número informado foi x"

'''
Nas versões de Python acima do 2.0 todo input é reconhecido com string.
Então é necessário fazer a conversão para número para verificar se realmente o que foi digitado é um número.
fonte: <pt.stackoverflow.com/questions/87584/como-converter-uma-variável-string-para-int>
'''

'''
Para lidar com o possível ValueError de tentar converter uma string verdadeira para int,
faz-se a verificação utilizando o tratamento de exceção com a estrutura try/except -> Tenta converter para inteiro, exceto se der o ValueError na conversão
fonte: <alura.com.br/artigos/tratamento-de-excecoes-no-python> <docs.python.org/3/tutorial/errors.html>
'''

n = input('Entre com um número: ')
try:
    print(f"O número informado foi {int(n)}.")
except ValueError:
    print(f"{n} não é um número! Tente novamente.")