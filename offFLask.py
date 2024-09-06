
while True:
    entrada = input("Digite uma lista de 5 números separados por espaço: ")
    lista = entrada.split() 
    
    if len(lista) != 5:
        print("A lista deve ter 5 números. Tente novamente.")
    else:
        try:
            lista = [int(num) for num in lista]
            print("A lista de números é:", lista)
            break 
        except ValueError:
            print("Todos os elementos devem ser números inteiros. Tente novamente.")

def obter_numero_valido(mensagem, lista):
    while True:
        try:
            numero = int(input(mensagem))
            if numero in lista:
                return numero
            else:
                print("O número digitado não está na lista. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

primeiro_num = obter_numero_valido("Digite o primeiro número para trocar da lista: ", lista)


segundo_num = obter_numero_valido("Digite o segundo número para trocar da lista: ", lista)

indice_primeiro = lista.index(primeiro_num)
indice_segundo = lista.index(segundo_num)

lista[indice_primeiro], lista[indice_segundo] = lista[indice_segundo], lista[indice_primeiro]

print("Lista após a troca:", lista)