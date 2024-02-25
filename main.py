import csv

contatos = []
ordem_contatos = []
contato = {}

def main():
    carregar_contatos()
    inicio()

def inicio():
    print("#### YouContact ####")
    print()
    print("1 - Visualizar contatos.")
    print("2 - Pesquisar contato.")
    print("3 - Adicionar novo contato.")
    print("4 - Salvar lista de contatos.")
    print("5 - Editar contato.")
    print("6 - Deletar contato.")
    print("0 - Sair")
    print()

    while True:
        try:
            resposta = int(input())
            if resposta == 0:
                return(0)
                break
            elif resposta == 1:
                visu_contatos() 
                input("Enter - Inicio")
                inicio()
                break
            elif resposta == 2:
                pesq_contato()
                input("Enter - Inicio")
                inicio()
                break
            elif resposta == 3:
                add_contato()
                inicio()
                break
            elif resposta == 4:
                salvar_contatos()
                inicio()
                break
            elif resposta == 5:
                edit_contato()
                inicio()
                break
            elif resposta == 6:
                del_contato()
                inicio()
                break
            else:
                print("Digite uma opção válida.")
        except ValueError:
            print("Digite um número válido.")


def carregar_contatos():
    try:
        with open("db/contatos.csv", "r") as arquivo:
            dados = csv.DictReader(arquivo)
            for linha in dados:    
                contatos.append({"nome": linha["nome"], "numero": linha["numero"]})
    except FileNotFoundError:
        with open("db/contatos.csv", "w", newline='') as arquivo:
            escritor_csv = csv.DictWriter(arquivo, fieldnames=["nome", "numero"])
            escritor_csv.writeheader()
            for contato in contatos:
                escritor_csv.writerow(contato)

def salvar_contatos():
    with open("db/contatos.csv", "w", newline='') as arquivo:
        escritor_csv = csv.DictWriter(arquivo, fieldnames=["nome", "numero"])
        escritor_csv.writeheader()
        for contato in contatos:
            escritor_csv.writerow(contato)
    print()
    print("Contatos salvos com sucesso.")
    print()
           

def visu_contatos():
    print()
    print("Contatos:")
    print()
    for contato in contatos:
        print(f"{contato['nome']}: {contato['numero']}")
    print()

def add_contato():
    contato = {}
    contato["nome"] = input("Nome do contato: ")
    contato["numero"] = input("Número do contato: ")
    contatos.append(contato)
    print()
    print("Contato adicionado com sucesso.")
    print()

def del_contato():
    achou, contatos_encontrados = pesq_contato()
    if achou:
        escolha = int(input("Dígito do contato: "))
        try:
            if escolha >= 1 and escolha <= len(contatos_encontrados):
                contato_deletar = contatos_encontrados[escolha - 1]
                contatos.remove(contato_deletar)
                print()
                print("Contato deletado com sucesso.")
                print()

        except ValueError:
            print("Dígito do contato inválido.")

    else:
        return

def pesq_contato():
    termo_pesquisa = input("Pesquisar contato: ").lower()
    contatos_encontrados = []

    for contato in contatos:
        if termo_pesquisa in contato["nome"].lower() or termo_pesquisa in contato["numero"]:
            contatos_encontrados.append(contato)

    if contatos_encontrados:
        print()
        print("Contatos encontrados:")
        print()
        num_ordem = 0
        for contato in contatos_encontrados:
            num_ordem += 1
            contato_ordem = {"ID": num_ordem, "nome": contato["nome"], "numero": contato["numero"]}
            ordem_contatos.append(contato_ordem)
            print(f"{num_ordem} - {contato['nome']}: {contato['numero']}")
        return True, contatos_encontrados
    else:
        print()
        print("Nenhum contato encontrado.")
        print()
        return False, []

def edit_contato():
    achou, contatos_encontrados = pesq_contato()
    if achou:
        escolha = input("Dígito do contato: ")
        try:
            escolha = int(escolha)
            if escolha >= 1 and escolha <= len(contatos_encontrados):
                contato_editar = contatos_encontrados[escolha - 1]
                print()
                print("1 - Editar contato.")
                print("2 - Editar somente o nome.")
                print("3 - Editar somente o numero.")
                print("0 - Voltar ao inicio.")
                print()
                resposta = int(input("Escolha uma opção: "))
                if resposta == 1:
                    contato_editar["nome"] = input("Novo nome do contato: ")
                    contato_editar["numero"] = input("Novo número do contato: ")
                    print()
                    print("Contato editado com sucesso.")
                    print()
                elif resposta == 2:
                    contato_editar["nome"] = input("Novo nome do contato: ")
                    print()
                    print("Contato editado com sucesso.")
                    print()
                elif resposta == 3:
                    contato_editar["numero"] = input("Novo número do contato: ")
                    print()
                    print("Contato editado com sucesso.")
                    print()
                elif resposta == 0:
                    return
                else:
                    print()
                    print("Opção inválida.")
                    print()
            else:
                print("Dígito do contato inválido.")
        except ValueError:
            print("Dígito do contato inválido.")
    else:
        return

if __name__ == "__main__":
    main()