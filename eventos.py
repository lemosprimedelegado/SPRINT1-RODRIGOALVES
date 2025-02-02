from datetime import datetime
import uuid
from persistencia import adicionar_concerto, adicionar_reserva, obter_concerto_por_id, obter_reservas, obter_concertos, atualizar_lugares_ocupados

def criar_concerto():
    print("\n=== Criar Concerto ===")
    nome = input("Nome do artista: ")
    local = input("Local do concerto: ")

    # Validação da data
    while True:
        data = input("Data do concerto (formato dd/mm/aaaa): ")
        try:
            data_obj = datetime.strptime(data, "%d/%m/%Y")
            if data_obj < datetime(2025, 1, 1):
                print("A data do concerto não pode ser antes de 01/01/2025!")
                continue
            data = data_obj.strftime("%d/%m/%Y")
            break
        except ValueError:
            print("Data inválida! Use o formato dd/mm/aaaa.")

    hora = input("Hora do concerto (HH:MM): ")
    capacidade = int(input("Capacidade do estabelecimento: "))
    preco_bilhete = float(input("Preço do bilhete (€): "))
    bar_disponivel = input("Bar disponível (s/n): ").lower() == "s"

    # Criar o dicionário do concerto
    concerto = {
        "id": str(uuid.uuid4()),
        "nome": nome,
        "local": local,
        "data": data,
        "hora": hora,
        "capacidade": capacidade,
        "preco_bilhete": preco_bilhete,
        "bar_disponivel": bar_disponivel,
        "lugares_ocupados": 0,
    }
    adicionar_concerto(concerto)
    print(f"Concerto '{nome}' criado com sucesso!")

def listar_concertos():
    print("\n=== Lista de Concertos ===")
    concertos = obter_concertos()
    if not concertos:
        print("Nenhum concerto disponível.")
        return
    for concerto in concertos:
        print(f"ID: {concerto['id']} | Nome: {concerto['nome']} | Local: {concerto['local']} | "
              f"Data: {concerto['data']} | Hora: {concerto['hora']} | Capacidade: {concerto['capacidade']} | "
              f"Lugares Ocupados: {concerto['lugares_ocupados']}")

def reservar_lugar():
    print("\n=== Reservar Lugar ===")
    listar_concertos()
    concerto_id = input("Insira o ID do concerto para reservar: ")

    # Verificar se o concerto existe
    concerto = obter_concerto_por_id(concerto_id)
    if not concerto:
        print("Concerto não encontrado!")
        return

    lugares = int(input("Quantos lugares deseja reservar? "))
    if concerto["lugares_ocupados"] + lugares > concerto["capacidade"]:
        print("Lugares insuficientes disponíveis!")
        return

    # Calcular preço total
    total = lugares * concerto["preco_bilhete"]

    # Criar reserva
    reserva = {
        "id": str(uuid.uuid4()),
        "concerto_id": concerto_id,
        "lugares": lugares,
        "total": total,
        "data_reserva": datetime.now().strftime("%d/%m/%Y %H:%M"),
    }
    adicionar_reserva(reserva)
    atualizar_lugares_ocupados(concerto_id, lugares)
    print(f"Reserva efetuada com sucesso! Código da reserva: {reserva['id']}")

def listar_reservas():
    print("\n=== Lista de Reservas ===")
    reservas = obter_reservas()
    if not reservas:
        print("Nenhuma reserva encontrada.")
        return
    for reserva in reservas:
        concerto = obter_concerto_por_id(reserva["concerto_id"])
        print(f"Reserva ID: {reserva['id']} | Concerto: {concerto['nome']} | Lugares: {reserva['lugares']} | "
              f"Total (€): {reserva['total']} | Data: {reserva['data_reserva']}")
