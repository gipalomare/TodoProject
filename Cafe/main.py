from funcoescafe import *
def main():
    cadastro_clientes = CadastroClientes()

    while True:
        print(" ============================== ")
        print("|| Café Desistente          ||")
        print("|| 1. Cadastro de Usuário   ||")
        print("|| 2. Login de Usuário      ||")
        print("|| 3. Adicionar produto     ||")
        print("|| 4. Exibir estoque        ||")
        print("|| 5. Vender produto        ||")
        print("|| 6. Remover produto       ||")
        print("|| 7. Sair                  ||")
        print(" ============================== ")
        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            cadastrarUsuario(cadastro_clientes)
        elif escolha == 2:
            fazerLogin(cadastro_clientes)
        elif escolha == 3:
            adicionarproduto()
        elif escolha == 4:
            listaProdutos()
        elif escolha == 5:
            venderProduto()
            listaProdutos()
        elif escolha == 6:
            removerProduto()
        elif escolha == 7:
            print("Fechando o programa.")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()