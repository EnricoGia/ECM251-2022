

arquivo_nome = "logs.txt"


### Criação e checagem de novo usuário

arquivo = open(arquivo_nome, "r")

usuario_nome = input("Digite um novo nome de usuário: ")

linhas = arquivo.readlines()

novo = True

for linha in linhas:
    if (usuario_nome == linha.strip()):
        print("Usuário já existe!")
        novo = False
        break

arquivo.close()

if (novo):
    arquivo = open(arquivo_nome, "a")
    arquivo.write(usuario_nome + " \n")
    print("Usuário %s criado." % usuario_nome)


print("Finalizando...")
arquivo.close()
