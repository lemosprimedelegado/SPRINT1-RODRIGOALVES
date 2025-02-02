import uuid
from datetime import datetime
from eventos import criar_concerto, listar_concertos, reservar_lugar, listar_reservas

def main():
    while True:
        print("\n=== Sistema de Gestão de Concertos ===")
        print("1. Criar Concerto")
        print("2. Listar Concertos")
        print("3. Reservar Lugar")
        print("4. Listar Reservas")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_concerto()
        elif opcao == "2":
            listar_concertos()
        elif opcao == "3":
            reservar_lugar()
        elif opcao == "4":
            listar_reservas()
        elif opcao == "5":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
