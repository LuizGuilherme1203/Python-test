from tools import * 
def menu():
    print("====== Lista de Compras ======")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Limpar lista")
    print("0 - Sair")
    print("==============================")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_item()
        elif opcao == "2":
            remover_item()
        elif opcao == "3":
            ver_lista()
        elif opcao == "4":
            limpar_lista()
        elif opcao == "0":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()
