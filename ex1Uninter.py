print ("Bem-vindo à Loja da Geovana de Meneses Moises") #Boas vindas
 

#solicitando valor do produto: 
valor_unitario = float(input("Entre com o valor do produto: ")) #
#solicitação de quantiddade:
quantidade = int(input("Entre com a quantidade do produto: ")) 

 

#calculo do valor total:

valor_total = valor_unitario * quantidade 

#acumulador de desconto:
desconto = 0  

#condições do desconto:  
if valor_total >= 2500 and valor_total < 6000:  

    desconto = valor_total * 0.04  

elif valor_total >= 6000 and valor_total < 10000: 

    desconto = valor_total * 0.07 

elif valor_total >= 10000:  

    desconto = valor_total * 0.11  

else: 

    desconto = 0  

 

#exibindo valores:  

print ("Valor SEM desconto R$:{:.2f}".format(valor_total)) 

print ("Valor COM desconto R$:{:.2f}".format (valor_total - desconto))  