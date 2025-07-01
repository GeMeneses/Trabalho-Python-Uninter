print('Bem-vindo à Livraria da Geovana de Meneses Moises')

# Lista vazia para guardar os livros
lista_livro = []

# Variável global de ID
id_global = 0

#Função para facilitar a exibição do menu
def estetica():
    print('-'*40)

# Função para cadastrar livro
def cadastrar_livro(id):
    estetica()
    print('-' *10 + 'MENU CADASTRAR LIVRO'+'-'*10)
    estetica()
    print(f'ID do Livro: {id}')
    
    nome_livro = input('Nome do livro: ').strip()
    nome_autor = input('Nome do autor: ').strip()
    editora = input('Editora: ').strip()

    livro = {
        'id': id,
        'nome_livro': nome_livro,
        'nome_autor': nome_autor,
        'editora': editora
    }

    lista_livro.append(livro)
    print('Livro cadastrado com sucesso!')
    estetica()

# Função para consultar livros
def consultar_livro():
    while True: 
        estetica()
        print('-'*10 +'MENU CONSULTAR LIVRO' +'-'*10)
        print('1 - Consultar Todos ')
        print('2 - Consultar por Id')
        print('3 - Consultar por Autor')
        print('4 - Retornar ao menu')
        consulta_de_livro = int(input('>>'))

        if consulta_de_livro == 1: #consulta todos os livros
            if not lista_livro:
                print('Não há livros cadastrados.\n')
                estetica()
            else:
                estetica()
                for livro in lista_livro:
                    print(f"Id: {livro['id']}")
                    print(f"Nome: {livro['nome_livro']}")
                    print(f"Autor: {livro['nome_autor']}")
                    print(f"Editora: {livro['editora']}")
                    estetica()
        elif consulta_de_livro == 2: #consulta de livros por id
            try:
                consultar_id = int(input('Digite o Id do Livro Desejado: '))
                estetica()
                encontrado = False
                for livro in lista_livro: 
                    if livro['id'] == consultar_id:
                        print(f"Id: {livro['id']}")
                        print(f"Nome: {livro['nome_livro']}")
                        print(f"Autor: {livro['nome_autor']}")
                        print(f"Editora: {livro['editora']}")
                        estetica()
                        encontrado = True 
                        break
                if not encontrado:
                    print('Livro não encontrado com o id digitado. Tente novamente')
                    estetica()
            except ValueError:
                print('Entre com um número inteiro')
        elif consulta_de_livro == 3: #consulta de  livros por autor
            consultar_autor = input('Digite o nome do autor desejado: ').strip().lower()
            encontrado = False
            for livro in lista_livro:
                if livro['nome_autor'].lower() == consultar_autor:
                    print(f"Id: {livro['id']}")
                    print(f"Nome: {livro['nome_livro']}")
                    print(f"Autor: {livro['nome_autor']}")
                    print(f"Editora: {livro['editora']}")
                    estetica()
                    encontrado = True
            if not encontrado:
                print(f'Autor {consultar_autor} não encontrado')
                estetica()
        elif consulta_de_livro == 4:
            break
        else:
            print('Opção inválida. Tente novamente')
            estetica()

# Função para remover livros
def remover_livro():
    estetica()
    print('-'*10 + 'MENU REMOVER LIVRO' + '-'*10)
    estetica()
    
    if not lista_livro:
        print('Não há livros cadastrados para remover.\n') # caso não haja livros cadastrados
        return
    try: 
        remover = int(input('Digite o Id do Livro que deseja remover: '))
        encontrado = False

        for livro in lista_livro: #comando de remoção de livros
            if livro['id'] == remover:
                lista_livro.remove(livro)
                print('Livro removido com sucesso!')
                estetica()
                encontrado = True
                break
        if not encontrado:
            print(f'Nenhum livro com ID {remover} foi encontrado. Tente novamente.')
    except ValueError:
        print('Por favor, digite um Id válido.')

# Codigo principal exibindo o Menu principal
while True:
    estetica()
    print('-'*13+'MENU PRINCIPAL'+'-'*13)
    estetica()
    print('Escolha a opção desejada:')
    print('1 - Cadastrar livro')
    print('2 - Consultar livro')
    print('3 - Remover Livro')
    print('4 - Sair')
    try:
    
        opcao = int(input('>>'))
            
        if opcao == 1:
            id_global += 1
            cadastrar_livro(id_global)
            
        elif opcao == 2:
            consultar_livro()
            
        elif opcao == 3:
            remover_livro()
            
        elif opcao == 4:
            print('Saindo do sistema. Até mais!')
            break
       

    except ValueError:
        print('Entre com uma opção válida (1, 2, 3, 4)\n')
    
