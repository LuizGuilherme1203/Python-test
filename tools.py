lista_compras = []

def adicionar_item():
    item = input("Digite o nome do item para adicionar: ")
    if item:
        lista_compras.append(item)
        print(f"'{item}' foi adicionado à lista.")
    else:
        print("Item vazio não pode ser adicionado.")

def remover_item():
    item = input("Digite o nome do item para remover: ")
    if item in lista_compras:
        lista_compras.remove(item)
        print(f"'{item}' foi removido da lista.")
    else:
        print(f"'{item}' não está na lista.")

def ver_lista():
    if lista_compras:
        print("\nLista de Compras:")
        for i, item in enumerate(lista_compras, 1):
            print(f"{i}. {item}")
    else:
        print("A lista está vazia.")

def limpar_lista():
    lista_compras.clear()
    print("A lista foi limpa.")