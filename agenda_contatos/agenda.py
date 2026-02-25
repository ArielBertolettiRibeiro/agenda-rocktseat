
def menu():
    print("1. Adicionar contato.")
    print("2. Editar contato.")
    print("3. Exibir contatos.")
    print("4. Marcar contato como favorito.")
    print("5. Procurar um contato.")
    print("6. Remover contato.")
    print("7. Listar contatos favoritos.")
    print("8. Sair do sistema.")
    return


agenda = []

def add_contact():

    name = input("Nome: ")
    phone = input("Telefone: ")
    email = input("E-mail: ")

    if not valida_phone(phone):
        print("Telefone já cadastrado!")
        return

    if not valida_email(email):
        print("Email já cadastrado!")
        return
    
    contato = {
        "name" : name,
        "phone" : phone,
        "email" : email,
        "favorite" : False
    }

    print("Contato adicionado com sucesso!\n")
    agenda.append(contato)

def valida_email(email):
    for item in agenda:
        if item["email"] == email:
            return False
        
    return True

def valida_phone(phone):
    for  item in agenda:
        if item["phone"] == phone:
            return False
        
    return True

def updated_contact(name):

    for cont in agenda:
        if cont["name"].lower() == name.lower():
            print("ACHEI")
            
            new_name = input("Novo nome (enter para manter): ")
            new_phone = input("Novo telefone (enter para manter): ")
            new_email = input("Novo email (enter para manter): ")

            if new_name:
                cont["name"] = new_name

            if new_phone:
                if not valida_phone(new_phone):
                    print("Telefone já cadastrado.")
                    return
                cont["phone"] = new_phone

            if new_email:
                if not valida_email(new_email):
                    print("Email já existe.")
                    return
                cont["email"] = new_email

            print("Contanto atualizado com sucesso!\n")
            return
        
    print("Contato não encontrado")
    return

def list_contact():
    print("Contantos: ")
    print(agenda)

def check_with_favorite(name):

    for item in agenda:
        if item["name"].lower() == name.lower():
            item["favorite"] = True
            print("Contato marcado como favorito.")
            return True
        
    print("Contato não encontrado.")
    return False

def remove_contact(name):
    for index, item in enumerate(agenda):
        if item["name"].lower() == name.lower():
            agenda.pop(index)
            print("Item removido!")
            return True
        
    print("Item não encontrado!")
    return False

def list_favorite_contact():
    
    found = False 

    for item in agenda:
        if item["favorite"]:
            print(item)
            found = True

    if not found:
        print("Nenhum item encontrado.")   

def get_contact(name):
    for contato in agenda:
        if contato["name"].lower() == name.lower():
            print(f"Contanto encontrado {contato}")
            return True
    
    print("Contato não encontrado!")
    return False
        
while True:

    menu()

    option = input("Escolha uma opção: ")
    match option:
        case "1":
            add_contact()
        case "2":
            name_contato = input("Digite o contato que deseja alterar: ")
            updated_contact(name_contato)
        case "3":
            list_contact()
        case "4":
            contato = input("Adicionar contato aos favoritos: ")
            check_with_favorite(contato)
        case "5":
            contato = input("Digite o contato que deseja buscar: ")
            get_contact(contato)
        case "6":
            contato = input("Digite o contato que deseja remover: ")
            remove_contact(contato)
        case "7":
            print("Contantos favoritados: ")
            list_favorite_contact()
        case "8":
            break

print("Programa finalizado!")