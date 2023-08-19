class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = "".join(
            filter(str.isdigit, cpf)
        )  # Armazena apenas os números do CPF
        self.endereco = endereco

    def __repr__(self):
        return f"{self.nome} - {self.cpf}"


class ContaCorrente:
    sequencial = 1

    def __init__(self, agencia, usuario):
        self.agencia = agencia
        self.numero = ContaCorrente.sequencial
        ContaCorrente.sequencial += 1
        self.usuario = usuario

    def __repr__(self):
        return (
            f"Agencia: {self.agencia} - Numero: {self.numero} - Usuario: {self.usuario}"
        )


def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    cpf = input("Digite o CPF (somente números): ")
    endereco = input(
        "Digite o endereço no formato 'logradouro, numero - bairro - cidade/UF': "
    )

    # Verifica se já existe usuário com o mesmo CPF
    for user in lista_usuarios:
        if user.cpf == cpf:
            print("Usuário com esse CPF já cadastrado!")
            return
    usuario = Usuario(nome, data_nascimento, cpf, endereco)
    lista_usuarios.append(usuario)
    print("Usuário criado com sucesso!")


def criar_conta():
    cpf = input("Digite o CPF do usuário para vincular a conta: ")

    usuario_encontrado = None
    for user in lista_usuarios:
        if user.cpf == cpf:
            usuario_encontrado = user
            break

    if not usuario_encontrado:
        print("Usuário não encontrado!")
        return
    conta = ContaCorrente("0001", usuario_encontrado)
    lista_contas.append(conta)
    print("Conta criada com sucesso!")


def depositar(saldo, extrato):
    valor = float(input("Digite o valor a ser depositado: "))
    if valor < 0:
        print("Valor inválido!")
        return saldo, extrato
    saldo += valor
    extrato += f"Depósito: {valor:.2f}\n"
    return saldo, extrato


def sacar(*, saldo, extrato, numero_saques, limite, limite_saques):
    valor = float(input("Digite o valor a ser sacado: "))
    if valor < 0:
        print("Valor inválido!")
        return saldo, extrato, numero_saques
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print("Saldo insuficiente!")
    elif excedeu_limite:
        print("Limite excedido!")
    elif excedeu_saques:
        print("Limite de saques excedido!")
    else:
        saldo -= valor
        extrato += f"Saque: {valor:.2f}\n"
        numero_saques += 1
    return saldo, extrato, numero_saques


def mostrar_extrato(saldo, /, *, extrato):
    print("=" * 40)
    print("Nenhuma movimentação" if extrato == "" else extrato, end="")
    print(f"\nSaldo: {saldo:.2f}")
    print("=" * 40)


def listar_usuarios():
    if not lista_usuarios:
        print("Nenhum usuário cadastrado!")
        return
    print("\nLista de Usuários:")
    print("=" * 40)
    for usuario in lista_usuarios:
        print(usuario)
    print("=" * 40)


def listar_contas():
    if not lista_contas:
        print("Nenhuma conta cadastrada!")
        return
    print("\nLista de Contas:")
    print("=" * 40)
    for conta in lista_contas:
        print(conta)
    print("=" * 40)


def main():
    global lista_usuarios, lista_contas
    lista_usuarios = []
    lista_contas = []

    menu = """
    [u] Criar Usuário
    [c] Criar Conta Corrente
    [lu] Listar Usuários
    [lc] Listar Contas
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    Escolha uma opção: 
    """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu)

        if opcao == "u":
            criar_usuario()
        elif opcao == "c":
            criar_conta()
        elif opcao == "lu":
            listar_usuarios()
        elif opcao == "lc":
            listar_contas()
        elif opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                extrato=extrato,
                numero_saques=numero_saques,
                limite=limite,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
            mostrar_extrato(saldo, extrato=extrato)
        elif opcao == "q":
            break
        else:
            print("Opção inválida!\n\n")


if __name__ == "__main__":
    main()
