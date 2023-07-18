from quartos import Quartos
from reservas import Reservas

quartos = Quartos()
reservas = Reservas()

while True:
    opcao = int(input("[0] Sair\n[1] Reservar quarto\n[2] Ver quartos reservados\n[3] Adicionar quarto\n[4] Remover quarto\n[5] Ver quartos\n: "))
    if opcao == 0:
        break
    
    elif opcao == 1:
        while True:
            for quarto in quartos.VerQuartos():
                print("Número do quarto:", quarto["numero_quarto"])
            try:
                numero_quarto = int(input("Quarto a ser reservado: "))
                break
            except ValueError:
                print("Valor inválido")
        while True:
            try:
                dias = int(input(f"Dias que o quarto {numero_quarto} será reservado: "))
                break
            except ValueError:
                print("Valor inválido!")
        print(reservas.ReservarQuarto(numero_quarto, dias))
    
    elif opcao == 2:
        for reserva in reservas.VerReservas():
            print(f"Quarto {reserva['numero_quarto']}")
    
    elif opcao == 3:
        while True:
            try:
                numero_quarto = int(input("Número do quarto: "))
                break
            except ValueError:
                print("Valor inválido!")
        while True:
            try:
                tamanho_quarto = float(input("Tamanho quarto (m²): "))
                break
            except ValueError:
                print("Valor inválido!")
        while True:
            try:
                diaria_preco = float(input("Preço da diária: ").replace(",", "."))
                break
            except ValueError:
                print("Valor inválido!")
        print(quartos.AdicionarQuarto(numero_quarto=numero_quarto, tamanho_quarto=tamanho_quarto, diaria_preco=diaria_preco))
    
    elif opcao == 4:
        while True:
            for quarto in quartos.VerQuartos():
                print(f"Quarto {quarto['numero_quarto']}")
            try:
                numero_quarto = int(input("Quarto que deseja remover: "))
                break
            except ValueError:
                print("Valor inválido!")
        print(quartos.RemoverQuarto(numero_quarto))
    
    elif opcao == 5:
        for quarto in quartos.VerQuartos():
            print(f"Quarto {quarto['numero_quarto']}\n\tTamanho: {quarto['tamanho_quarto']}\n\tPreço da diária: R${str(quarto['diaria_preco']).replace('.', ',')}")