import os

tarefas_lista = []

def main():

    while True:

        os.system("cls")
        print("Gerenciador de Tarefas\n")
        print("1. Adicionar tarefa")
        print("2. Visualzar tarefas")
        print("3. Remover tarefa")
        print("4.sair\n")
        try:
            opcao = int(input("Selecione uma opção: "))
            match opcao:
                case 1:
                    adicionar_tarefa()
                    continue
                case 2:
                    visualizar_tarefas()
                    continue
                case 3:
                    remover_tarefa()
                    continue
                case 4:
                    os.system("cls")
                    print("Saindo do programa...")
                    break
                case _:
                    print("Opção selecionada não existe!")
                    input("Digite uma tecla para tentar novamente: ")
        except ValueError:
                os.system("cls")
                print("Erro! Valor incorreto")
                input("Digite uma tecla para tentar novamente: ")




def adicionar_tarefa():
    tarefa = input("Digite o nome da tarefa: ").strip().title()
    tarefas_lista.append(tarefa)


def visualizar_tarefas():
    print(",".join(tarefas_lista))
    input("Digite uma tecla para continuar: ")


def remover_tarefa():
    tarefa = input("Digite o nome da tarefa a ser removida: ").strip().title()
    tarefas_lista.remove(tarefa)


main()
