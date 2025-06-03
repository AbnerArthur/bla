from dados_eventos import eventos
from dados_participantes import participantes

def listar_eventos():
    print("\n Lista de Eventos:")
    for evento in eventos:
        print(f"- {evento['nome']} | Data: {evento['data']} | Tema: {evento['tema']}")

def listar_participantes_por_evento():
    print("\n Participantes por Evento:")
    for evento in eventos:
        print(f"\nEvento: {evento['nome']}")
        for codigo in evento['participantes']:
            participante = next((p for p in participantes if p['codigo'] == codigo), None)
            if participante:
                print(f"  - {participante['nome']} ({participante['email']})")

def buscar_participante_por_codigo():
    codigo = int(input("\n Digite o código do participante: "))
    participante = next((p for p in participantes if p['codigo'] == codigo), None)
    if participante:
        print(f"\nParticipante encontrado:")
        print(f"Nome: {participante['nome']}")
        print(f"E-mail: {participante['email']}")
        print(f"Preferências: {', '.join(participante['preferencias'])}")
    else:
        print("Participante não encontrado.")

def menu():
    while True:
        print("\n=== Sistema de Gerenciamento de Eventos ===")
        print("1. Listar eventos")
        print("2. Listar participantes por evento")
        print("3. Buscar participante por código")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_eventos()
        elif opcao == "2":
            listar_participantes_por_evento()
        elif opcao == "3":
            buscar_participante_por_codigo()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()