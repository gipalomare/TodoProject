# Define o limite do estoque
LIMITE_ESTOQUE = 100

# Define a estrutura de dados para o produto
class Produto:
    def _init_(self):
        self.nomeproduto = ""
        self.quantidade = 0
        self.preco = 0.0

# Cria uma lista para armazenar os produtos
estoque = [Produto() for _ in range(LIMITE_ESTOQUE)]
qtdProduto = 0
def adicionarproduto():
    global qtdProduto

    if qtdProduto >= LIMITE_ESTOQUE:
        print("O estoque está cheio, não é possível adicionar mais produtos.")
        return

    novoProduto = Produto()
    novoProduto.nomeproduto = input("Digite o nome do novo produto: ")
    novoProduto.quantidade = int(input("Digite a quantidade que deseja adicionar: "))
    novoProduto.preco = float(input("Digite o preço do produto: "))

    estoque[qtdProduto] = novoProduto
    qtdProduto += 1
    print("Produto adicionado")

# Função para listar os produtos em estoque
def listaProdutos():
    if qtdProduto == 0:
        print("O estoque está vazio.")
    else:
        print("Produtos em estoque:")
        for i in range(qtdProduto):
            print(f"Nome: {estoque[i].nomeproduto}, Quantidade: {estoque[i].quantidade}, Preço: R$ {estoque[i].preco:.2f}")
    print()

# Função para vender um produto
def venderProduto():
    nome = input("Digite o nome do produto que deseja vender: ")
    quantidade = int(input("Digite a quantidade que deseja vender: "))

    for i in range(qtdProduto):
        if nome == estoque[i].nomeproduto:
            if estoque[i].quantidade >= quantidade:
                estoque[i].quantidade -= quantidade
                print("Produto vendido!")
            else:
                print("Quantidade insuficiente no estoque, avise o gerente.")
            return
    print("Produto não encontrado no estoque.")

# Função para remover um produto
def removerProduto():
    nome = input("Digite o nome do produto que deseja remover: ")
    quantidade = int(input("Digite a quantidade que deseja remover: "))

    for i in range(qtdProduto):
        if nome == estoque[i].nomeproduto:
            if estoque[i].quantidade >= quantidade:
                estoque[i].quantidade -= quantidade
                print("Produto removido!")
            else:
                print("Quantidade insuficiente no estoque, avise o gerente.")
            return
    print("Produto não encontrado no estoque.")
# Classe Cliente
class Cliente:
    def __init__(self, nome, idade, email, senha):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.senha = senha

# Classe CadastroClientes
class CadastroClientes:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self, nome, idade, email, senha):
        cliente = Cliente(nome, idade, email, senha)
        self.clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")

    def fazer_login(self, email, senha):
        for cliente in self.clientes:
            if cliente.email == email and cliente.senha == senha:
                print("Login bem-sucedido. Bem-vindo,", cliente.nome)
                return
        print("Login falhou. Verifique suas credenciais.")

# Função de cadastro de usuário
def cadastrarUsuario(cadastro_clientes):
    print("Cadastro de Usuário")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    email = input("Email: ")
    senha = input("Senha: ")
    cadastro_clientes.cadastrar_cliente(nome, idade, email, senha)

# Função de login de usuário
def fazerLogin(cadastro_clientes):
    print("Login de Usuário")
    email = input("Email: ")
    senha = input("Senha: ")
    cadastro_clientes.fazer_login(email, senha)