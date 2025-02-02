# Listas para armazenar os concertos e reservas
concertos = []
reservas = []

def adicionar_concerto(concerto):
    concertos.append(concerto)

def adicionar_reserva(reserva):
    reservas.append(reserva)

def obter_concerto_por_id(concerto_id):
    return next((c for c in concertos if c["id"] == concerto_id), None)

def obter_reservas():
    return reservas

def obter_concertos():
    return concertos

def atualizar_lugares_ocupados(concerto_id, lugares):
    concerto = obter_concerto_por_id(concerto_id)
    if concerto:
        concerto["lugares_ocupados"] += lugares
