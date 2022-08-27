

arquivo_nome = "logs.txt"

# Criação e checagem de novo usuário


def novo_usuario():

    usuario_nome = input("Digite um novo nome de usuário: ")

    arquivo = open(arquivo_nome, "r")
    linhas = arquivo.readlines()
    novo = True

    for linha in linhas:
        if (usuario_nome == linha.strip().split(":")[0]):
            print("Usuário já existe!")
            novo = False
            break

    arquivo.close()

    if (novo):
        senha = input("Digite uma senha: ")
        arquivo = open(arquivo_nome, "a")
        arquivo.write(usuario_nome + ":" + senha + "\n")
        print("Usuário %s criado." % usuario_nome)

    arquivo.close()

def teste():
    print("Funcionando...")
### Main

x = {1:novo_usuario,2:teste}

x[2]()

print("Finalizando...")
