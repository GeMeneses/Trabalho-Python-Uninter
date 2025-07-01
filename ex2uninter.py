#Exibindo boas vindas e cardápio:
print('Bem-vindo a Loja Gelados da Geovana de Meneses Moises')
print(17*'-'+'Cardápio'+17*'-')
print(42 * '-')
print(3*'-'+ '|tamanho| Cupuaçu (CP) | Açaí (AC) |' + 3 * '-')
print(3*'-'+ '|   P   |   R$ 9.00    |  R$11.00  |' + 3 * '-')
print(3*'-'+ '|   M   |   R$ 14.00   |  R$16.00  |' + 3 * '-')
print(3*'-'+ '|   G   |   R$ 18.00   |  R$20.00  |' + 3 * '-')

total = 0 #Variavel que irá acumular o valor total dos pedidos

while True: #iniciando loop


#Validando sabor:
    while True:
        sabor = str(input('\nEntre com o sabor desejado (AC/CP): ')).upper().strip()
       
        if (sabor not in ['AC', 'CP']):
            print('Sabor inválido. Tente novamente\n')
        else:
            break
#Validando tamanho:      
    while True: 
        tamanho = str(input('Entre com o tamanho desejado (P/M/G): ')).upper().strip()
        if (tamanho not in ['P', 'M', 'G']):
            print('Tamanho inválido. Tente novamente\n')
        else:
            break 

    preco_item = 0 #variavel de valor do item

#Condições do Açaí:
    if sabor == 'AC':
        if tamanho == 'P':
            preco_item = 11
            total += preco_item
            print('Você pediu um Açaí no tamanho P: R$ {:.2f}'.format(preco_item))
        elif tamanho == 'M':
            preco_item = 16
            total += preco_item
            print('Você pediu um Açaí no tamanho M: R$ {:.2f}'.format(preco_item))
        elif tamanho == 'G':
            preco_item = 20
            total += preco_item
            print('Você pediu um Açaí no tamanho G: R$ {:.2f}'.format(preco_item))

   
#Condições do Cupuaçu:
    elif sabor == 'CP':
        if tamanho == 'P':
            preco_item = 9.00
            total += preco_item
            print('Você pediu um Cupuaçu no tamanho P: R$ {:.2f}'.format(preco_item))
        elif tamanho == 'M':
            preco_item = 14.00
            total += preco_item
            print('Você pediu um Cupuaçu no tamanho M: R$ {:.2f}'.format(preco_item))
        elif tamanho == 'G':
            preco_item = 18
            total += preco_item
            print('Você pediu um Cupuaçu no tamanho G: R$ {:.2f}'.format(preco_item))

    #Veridicando se cliente deseja pedir mais:      
    pedir_mais = str(input('\nDeseja pedir mais alguma coisa? (S/N) ')).upper().strip()
    if pedir_mais == 'N': 
        break 
    elif pedir_mais =='S':
        continue 
#Exibindo valor total a pagar:
print('\nO valor total a ser pago é: R$ {:.2f}'.format(total))