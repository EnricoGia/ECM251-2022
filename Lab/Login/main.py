

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


def logando_usuario():

    usuario = input("Digite o usuário:")
    senha = input("Digite a senha:")

    arquivo = open(arquivo_nome, "r")
    login = (usuario + ":" + senha + "\n")

    linhas = arquivo.readlines()

    aprovado = False

    for linha in linhas:
        if (linha == login):
            aprovado = True

    mensagem = "aprovado." if aprovado else "negado."

    print("Login " + mensagem)

    arquivo.close()


# Main

arquivo_nome = "logs.txt"
menu = {1: novo_usuario, 2: logando_usuario}

op = int(input('''
Opções:
[1] - Criar um novo usuário
[2] - Logar com usuário ja existente

->:'''))




menu[op]()

print("Finalizando...")
