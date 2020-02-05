import defs
import conexao
import os

def menuApp():
    while not autentico:
        while True:
            i = ['1','2']
            decisao = input("1 - Logar , 2 - Cadastrar ->>  ")
            if decisao in i:
                os.system('clear')
                break
            else:
                continue
        try:
            cursor.execute('select * from cadastros')
            resultado = cursor.fetchall()
        except:
            print("Erro ao conectar-se ao banco de dados.")

        autentico,usuarioSupremo = logarCadastrar()

    if autentico:
        print("Logado com sucesso.")
        if usuarioSupremo == True:
            decisaoUsuario = 1

            while decisaoUsuario != 0:
                decisaoUsuario = int(input(" 0 - Sair, 1 - Cadastro, 2 - Listar Produtos, 3 - Anotar Pedido, 4 - Conferir Pedidos, 5 - Contas de Acesso, 6 - Gerar Estatisticas  ->> "))
                if decisaoUsuario == 1:
                    cadastrarProduto()
                elif decisaoUsuario == 2:
                    listarProdutos()
                    decisaoDeleta = int(input(" 1 - Deletar Produto, 2 - Voltar ao Inicio ->> "))
                    if decisaoDeleta == 1:
                        excluirProdutos()
                        os.system('clear')
                elif decisaoUsuario == 3:
                    anotarPedidos()
                elif decisaoUsuario == 4:
                    listarPedidos()
                elif decisaoUsuario == 5:
                    listarVendedores()
                elif decisaoUsuario == 6:
                    gerarEstatistica()
        else:
            decisaoUsuario = 1
            while decisaoUsuario != 0:
                decisaoUsuario = int(input(" 0 - Sair, 1 - Cadastro, 2 - Listar Produtos, 3 - Anotar Pedido, 4 - Conferir Pedidos ->> "))
                if decisaoUsuario == 1:
                    cadastrarProduto()
                elif decisaoUsuario == 2:
                    listarProdutos()
                elif decisaoUsuario == 3:
                    anotarPedidos()
                elif decisaoUsuario == 4:
                    listarPedidos()
    cursor.close()
    conexao.close()
