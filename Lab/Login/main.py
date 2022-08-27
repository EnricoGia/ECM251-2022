

arquivo_nome = "logs.txt"


# Criação e checagem de novo usuário

arquivo = open(arquivo_nome, "r")

usuario_nome = input("Digite um novo nome de usuário: ")

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
###
print("Finalizando...")
