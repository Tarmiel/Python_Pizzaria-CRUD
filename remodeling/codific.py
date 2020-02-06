import os
import connectionDB
from connectionDB import getConnection
import menu

#importando a conexao com o banco de dados e atribuindo
connection = connectionDB.getConnection()
cursor = connection.cursor()

def logarCadastrar():
    usuarioExiste = 0
    autenticado = False
    usuarioMaster = False

    global vendedor

    if decisao =='1':
        nome = input("Usuario: ")
        senha = input("Senha: ")
        for linha in resultado:
            if nome==linha['nome'] and senha==linha['senha']:
                vendedor = nome
                if linha['nivel']==1:
                    usuarioMaster = False
                elif linha['nivel']==2:
                    usuarioMaster = True
                autenticado = True
                break
            else:
                autenticado = False
        if not autenticado:
            print("Dados incorretos!Tente Novamente")
            time.sleep(5)
            os.system('clear')
    elif decisao =='2':
        nome = input("Usuario: ")
        senha = input("Senha: ")
        for linha in resultado:
            if nome==linha['nome']:
                usuarioExiste = 1
        if usuarioExiste == 1:
            print("Usuario existente, tente novamente.")
            time.sleep(3)
            os.system('clear')
        elif usuarioExiste == 0:
            try:
                cursor.execute('insert into cadastros (nome, senha, nivel) values(%s, %s, %s)', (nome,senha, 1))
                getConnection.conexao.commit()
                print("Usuario cadastrado com sucesso.")
                time.sleep(3)
                os.system('clear')
            except:
                print("Erro ao cadastrar no banco de dados. Tente Novamente")
                time.sleep(3)
                os.system('clear')
            finally:
                print("......")
    return autenticado,usuarioMaster
def cadastrarProduto():
    nome = input("Nome do produto: ")
    ingrediente = input("Nome do ingrediente: ")
    grupo = input("Grupo: ")
    preco = float(input("Preço: "))

    try:
        cursor.execute('insert into produtos (nome, ingredientes, grupo,preco ) values(%s, %s, %s,%s)', (nome,ingrediente,grupo,preco))
        conexao.commit()
        print("Produto cadastrado com sucesso.")
        time.sleep(3)
        os.system('clear')
    except:
        print("Erro ao cadastrar no banco de dados. Tente Novamente")
        time.sleep(3)
        os.system('clear')
def listarProdutos():
    produtos = []
    try:
        cursor.execute('select * from produtos')
        produtosCadastrados = cursor.fetchall()

    except:
        print("Erro ao consultar no banco de dados. Tente Novamente")
        time.sleep(3)
        os.system('clear')

    for i in produtosCadastrados:
        produtos.append(i)
    if len(produtos) !=0:
        for i in range(0,len(produtos)):
            print(produtos[i])
    else:
        print("Nenhum produto cadastrado.")
        time.sleep(3)
        os.system('clear')
def excluirProdutos():
    idDeletar = int(input("Digite o ID referente ao produto que deseja deletar ->> "))

    try:
        cursor.execute('delete from produtos where id = {}'.format(idDeletar))
        print("Deletado com sucesso!")
    except:
        print("Erro ao excluir no banco de dados.")
        time.sleep(3)
        os.system('clear')
def anotarPedidos():
    listaDosProdutos = []
    try:
        cursor.execute('select * from produtos')
        listaProdutos = cursor.fetchall()
    except:
        print("Erro ao conectar-se ao banco de dados.")


    os.system('clear')
    for i in listaProdutos:
        listaDosProdutos.append(i)
    if len(listaDosProdutos) !=0:
        for i in range(0,len(listaDosProdutos)):
            print("Codigo = "+str(i)+" - "+str(listaDosProdutos[i]))
    else:
        print("Nenhum produto cadastrado.")

    pedido= int(input("Digite o primeiro Indice do produto referente ao pedido: "))
    local = input("Local de entrega? ")
    observacao = input("Observação? ")
    data = input("Data no formato mes-ano: ")

    try:
        cursor.execute('insert into pedidos(nome,ingredientes,grupo,localEntrega,observacoes,data,vendedor) values (%s,%s,%s,%s,%s,%s,%s)',(listaDosProdutos[pedido]['nome'],listaDosProdutos[pedido]['ingredientes'],listaDosProdutos[pedido]['grupo'],local,observacao,data,vendedor))
        conexao.commit()
        print("Pedido feito com sucesso.")
    except:
        print("Erro ao conectar-se ao banco de dados.")

    time.sleep(2)
    os.system('clear')
def listarPedidos():
    pedidos = []
    decisao = 0
    while decisao != 2:
        pedidos.clear()
        try:
            cursor.execute('select * from pedidos')
            listaPedidos = cursor.fetchall()
        except:
            print("Erro ao conectar-se ao banco de dados.")

        os.system('clear')
        for i in listaPedidos:
            pedidos.append(i)
        if len(pedidos) !=0:
            for i in range(0,len(pedidos)):
                print(pedidos[i])
        else:
            print("Nenhum pedido feito.")
            break

        decisao = int(input("1 - Encerrar Pedido , 2 - Voltar ao inicio ->>"))
        if decisao == 1:
            iddeletar = int(input("Digite o ID do pedido para encerrar: "))


            #armazena o nome do produto
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select nome,grupo from pedidos where id = {}'.format(iddeletar))
                    armazena = cursor.fetchall()
                    print("...")
            except:
                print("Erro ao conectar-se ao banco de dados.")
            armazenaNome = armazena[0]['nome']
            armazenaGrupo = armazena[0]['grupo']

            #pega o preço do produto
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from produtos where nome = %s',(armazenaNome))
                    precoAlimento = cursor.fetchall()
                    print("...")
            except:
                print("Erro ao conectar-se ao banco de dados/precos.")
            armazenaPrec = precoAlimento[0]['preco']

            #insere na tabela estatistica
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('insert into estatisticaVendido(nome,grupo,preco,vendedor) values (%s,%s,%s,%s)',(armazenaNome,armazenaGrupo,armazenaPrec,vendedor))
                    conexao.commit()
            except:
                print("Erro ao conectar-se ao banco de dados.")

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('delete from pedidos where id = {}'.format(iddeletar))
                    conexao.commit()
                    print("Pedido encerrado.")
            except:
                print("Erro ao conectar-se ao banco de dados.")

            time.sleep(3)
            os.system('clear')
        elif decisao == 2:
            break
def listarVendedores():
    perfis = []
    while True:
        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from cadastros')
                perfisCadastrados = cursor.fetchall()
        except:
            print("Erro ao conectar-se ao banco de dados")
            break
        os.system('clear')
        for i in perfisCadastrados:
            perfis.append(i)
        if len(perfis) >=2:
            for i in range(1,len(perfis)):
                print(perfis[i])
            deletaPerfil = int(input("1 - Remover Perfil,2 - Voltar ao inicio : "))
            if deletaPerfil == 1:
                escolhaPerfil = int(input("Digite o ID do perfil -> "))
                try:
                    cursor.execute('delete from cadastros where id = {}'.format(escolhaPerfil))
                    conexao.commit()
                    print("Removido com sucesso!")
                except:
                    print("Erro ao acessar o banco de dados.")
            elif escolhaPerfil == 2:
                break
        else:
            print("Não há perfis cadastrados.")
            time.sleep(2)
            break
    os.system('clear')
def gerarEstatistica():
    nomeProdutos = []
    nomeProdutos.clear()
    nomeVendedor = []
    nomeVendedor.clear()
    try:
        cursor.execute('select * from produtos')
        produtos = cursor.fetchall()
    except:
        print("Erro ao conectar-se ao banco de dados.")

    try:
        cursor.execute('select * from estatisticaVendido')
        vendido = cursor.fetchall()
    except:
        print("Erro ao conectar-se ao banco de dados.")

    estado = int(input("0 - Sair, 1 - Pesquisar por Nome, 2 - Pesquisar por Grupo, 3 - Vendedores ->> "))
    if estado == 1:
        decisao3 = int(input(" 1 - para pesquisar por dinheiro, 2 - quantidade unitaria ->> "))
        if decisao3 == 1:
            for i in produtos:
                nomeProdutos.append(i['nome'])

            valores = []
            valores.clear()

            for h in range(0,len(nomeProdutos)):
                somaValor = -1
                for i in vendido:
                    if i['nome'] == nomeProdutos[h]:
                        somaValor += i['preco']
                if somaValor == -1:
                    valores.append(0)
                elif somaValor > 0:
                    valores.append(somaValor+1)

            plt.plot(nomeProdutos,valores)
            plt.ylabel('Quantidade Vendida em Reais')
            plt.xlabel('Produtos')
            plt.show()
        if decisao3 == 2:
            grupoUnico = []
            grupoUnico.clear()
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from produtos')
                    grupo = cursor.fetchall()
            except:
                print("Erro ao conectar-se ao banco de dados.")

            try:
                cursor.execute('select * from estatisticaVendido')
                vendidosGrupo = cursor.fetchall()
            except:
                print("Erro ao conectar-se ao banco de dados.")
            for i in grupo:
                grupoUnico.append(i['nome'])


            qntFinal = []
            qntFinal.clear()

            for h in range(0,len(grupoUnico)):
                qntUnitaria = 0
                for i in vendidosGrupo:
                    if grupoUnico[h] == i['nome']:
                        qntUnitaria +=1
                qntFinal.append(qntUnitaria)

            plt.plot(grupoUnico,qntFinal)
            plt.ylabel('Quantidade Unitaria')
            plt.xlabel('Produtos')
            plt.show()
    elif estado == 2:
        decisao4 = int(input(" 1 - para pesquisar por dinheiro, 2 - quantidade unitaria ->> "))
        if decisao4 == 1:
            for i in produtos:
                nomeProdutos.append(i['grupo'])

            valores = []
            valores.clear()

            for h in range(0,len(nomeProdutos)):
                somaValor = -1
                for i in vendido:
                    if i['grupo'] == nomeProdutos[h]:
                        somaValor += i['preco']
                if somaValor == -1:
                    valores.append(0)
                elif somaValor > 0:
                    valores.append(somaValor+1)

            plt.plot(nomeProdutos,valores)
            plt.ylabel('Quantidade Vendida em Reais')
            plt.xlabel('Produtos')
            plt.show()
        if decisao4 == 2:
            grupoUnico = []
            grupoUnico.clear()
            try:
                cursor.execute('select * from produtos')
                grupo = cursor.fetchall()
            except:
                print("Erro ao conectar-se ao banco de dados.")

            try:
                cursor.execute('select * from estatisticaVendido')
                vendidosGrupo = cursor.fetchall()
            except:
                print("Erro ao conectar-se ao banco de dados.")
            for i in grupo:
                grupoUnico.append(i['grupo'])


            qntFinal = []
            qntFinal.clear()

            for h in range(0,len(grupoUnico)):
                qntUnitaria = 0
                for i in vendidosGrupo:
                    if grupoUnico[h] == i['grupo']:
                        qntUnitaria +=1
                qntFinal.append(qntUnitaria)

            plt.plot(grupoUnico,qntFinal)
            plt.ylabel('Quantidade Unitaria')
            plt.xlabel('Produtos')
            plt.show()
    elif estado == 3:
        for i in vendido:
            nomeVendedor.append(i['vendedor'])

            valores = []
            valores.clear()

            for h in range(0,len(nomeVendedor)):
                somaValor = -1
                for i in vendido:
                    if i['vendedor'] == nomeVendedor[h]:
                        somaValor += i['preco']
                if somaValor == -1:
                    valores.append(0)
                elif somaValor > 0:
                    valores.append(somaValor+1)

        plt.plot(nomeVendedor,valores)
        plt.ylabel('Quantidade Vendida em reais por vendedor')
        plt.xlabel('Vendedores')
        plt.show()
