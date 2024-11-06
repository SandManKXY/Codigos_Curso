class Cliente:
    def __init__(self, RG_cliente, nome):
        self.RG_cliente = RG_cliente
        self.nome = nome
        self.produto_locado = None

class Veiculo:
    def __init__(self, id_veiculo, modelo, ano, cor, chassi, tipo_combustivel, marca, preco_por_dia):
        self.id_veiculo = id_veiculo
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.chassi = chassi
        self.tipo_combustivel = tipo_combustivel
        self.marca = marca
        self.preco_por_dia = preco_por_dia
        self.locatario = None

clientes = []
veiculos = []

def encontrar_cliente(RG_cliente):
    return next((c for c in clientes if c.RG_cliente == RG_cliente), None)

def encontrar_veiculo(id_veiculo):
    return next((v for v in veiculos if v.id_veiculo == id_veiculo), None)

def adicionar_cliente():
    RG_cliente = int(input("RG do cliente: "))
    nome = input("Nome do cliente: ")
    clientes.append(Cliente(RG_cliente, nome))
    print(f"Cliente {nome} adicionado!")

def adicionar_veiculo():
    id_veiculo = int(input("ID do veículo: "))
    modelo = input("Modelo: ")
    ano = input("Ano: ")
    cor = input("Cor: ")
    chassi = input("Chassi (VIN): ")
    tipo_combustivel = input("Tipo de combustível: ")
    marca = input("Marca: ")
    preco_por_dia = float(input("Preço por dia: "))
    veiculos.append(Veiculo(id_veiculo, modelo, ano, cor, chassi, tipo_combustivel, marca, preco_por_dia))
    print(f"Veículo {modelo} adicionado!")

def excluir_cliente():
    RG_cliente = int(input("ID do cliente a ser excluído: "))
    cliente = encontrar_cliente(RG_cliente)
    if cliente and cliente.produto_locado is None:
        clientes.remove(cliente)
        print(f"Cliente {cliente.nome} excluído!")
    else:
        print("Cliente não encontrado ou está com um veículo alugado.")

def excluir_veiculo():
    id_veiculo = int(input("ID do veículo a ser excluído: "))
    veiculo = encontrar_veiculo(id_veiculo)
    if veiculo and veiculo.locatario is None:
        veiculos.remove(veiculo)
        print(f"Veículo {veiculo.modelo} excluído!")
    else:
        print("Veículo não encontrado ou está alugado.")

def alugar_veiculo():
    RG_cliente = int(input("ID do cliente que deseja alugar um veículo: "))
    cliente = encontrar_cliente(RG_cliente)
    if not cliente or cliente.produto_locado:
        print("Cliente não encontrado ou já possui um veículo alugado.")
        return
    
    id_veiculo = int(input("ID do veículo a ser alugado: "))
    veiculo = encontrar_veiculo(id_veiculo)
    if not veiculo or veiculo.locatario:
        print("Veículo não encontrado ou já está alugado.")
        return
    
    cliente.produto_locado = veiculo
    veiculo.locatario = cliente
    print(f"{cliente.nome} alugou o veículo {veiculo.modelo}.")

def devolver_veiculo():
    RG_cliente = int(input("ID do cliente que deseja devolver o veículo: "))
    cliente = encontrar_cliente(RG_cliente)
    if not cliente or not cliente.produto_locado:
        print("Cliente não encontrado ou não possui um veículo alugado.")
        return
    
    veiculo = cliente.produto_locado
    cliente.produto_locado = None
    veiculo.locatario = None
    print(f"{cliente.nome} devolveu o veículo {veiculo.modelo}.")

def menu():
    while True:
        print("\n--- LOCALIZA ---")
        print("1. Adicionar Cliente")
        print("2. Excluir Cliente")
        print("3. Adicionar Veículo")
        print("4. Excluir Veículo")
        print("5. Alugar Veículo")
        print("6. Devolver Veículo")
        print("7. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            adicionar_cliente()
        elif escolha == "2":
            excluir_cliente()
        elif escolha == "3":
            adicionar_veiculo()
        elif escolha == "4":
            excluir_veiculo()
        elif escolha == "5":
            alugar_veiculo()
        elif escolha == "6":
            devolver_veiculo()
        elif escolha == "7":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Iniciar o menu
menu()
