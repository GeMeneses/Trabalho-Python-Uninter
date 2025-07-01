#Mensagem de boas vindas:
print('Bem-vindo à Copiadora da Geovana de Meneses Moises\n')

#Função de serviço, validação e valor:
def escolha_servico():
    while True:
        print('Entre com o serviço desejado:')
        print('DIG - Digitalização')
        print('ICO - Impressão colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')
        
        servico = input('>> ').upper().strip()
        if servico not in ['DIG','ICO','IPB','FOT']:
           print('Escolha inválida, entre com o tipo de serviço novamente\n') 
        else:
            if servico == 'DIG':
                valor = 1.10
            elif servico == 'ICO':
                valor = 1.00
            elif servico == 'IPB' :
                valor = 0.40
            elif servico == 'FOT':
                valor = 0.20
            return valor, servico
          

#Função de quantidade de páginas, aplicação de desconto e uso do try/except
def num_pagina(valor_unidade):
    while True:
        try: 
            pag = int(input('Entre com o número de páginas: \n'))
            if pag > 20000 or pag <= 0:
                print('Não aceitamos tantas páginas de uma vez.\nPor favor, entre com o número de páginas novamente\n')

            else:
                if pag < 20 :
                    desconto = 0
                elif pag < 200:
                    desconto =  0.15
                elif pag < 2000:
                    desconto =  0.20
                else:
                    desconto = 0.25
                
                pag_com_desconto = pag * (1 - desconto)
                total = pag_com_desconto * valor_unidade
                return pag_com_desconto, total
        except ValueError:
            print('Valor invalido, Tente novamente\n')


#Função de adicional e uso do Try/except:
def servico_extra():
    try:
        while True:
            print('\nDeseja adicionar algum serviço: ')
            print('1 - Encadernação simples - R$ 15.00')
            print('2 - Encadernação Capa Dura - R$ 40.00')
            print('0 - Não desejo mais nada') 
            opcao = int(input('>>'))
            
            if opcao == 1:
                return 15.00
            elif opcao == 2:
                return  40.00
            elif opcao == 0:
                return 0.00
            else:
                print('Opção inválida. Escolha 0, 1 ou 2.\n')
    except ValueError:
         print('Escolha invalida. Tente novamente')

#Codigo principal        
valor_unidade, servico_escolhido = escolha_servico() #retorna o serviço e valor unitário
paginas, valor_total = num_pagina(valor_unidade) # retorna quantidade de paginas cpm desconto e valor total do serviço
valor_adicional=servico_extra() # retorna valor de serviço extra
valor_final= valor_total + valor_adicional  # retorna o valor à pagar 

#exibindo resultado
print(f'Total: R$ {valor_final:.2f} (serviço: {valor_unidade:.2f} * páginas: {paginas:.0f} + extra: {valor_adicional:.2f})')

            
            
            