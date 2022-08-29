
def finalizar():
    print("Finalizando...")


def novo_usuario():

    usuario_nome = input("Digite um novo nome de usuário:")

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
        senha = input("Digite uma senha:")
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
            break

    arquivo.close()

    if(aprovado):
        print("Login aprovado!")
        return usuario
    else:
        print("Login negado!")
        return ""

def deslogar():
    return ""

def opcoes(conta_atual):

    if(conta_atual == ""):
        op = int(input('''
Conta : ''' + conta_atual +
                   '''
Opções:
[0] - Finalizar o programa
[1] - Criar um novo usuário
[2] - Logar com usuário já existente

->:'''))
    else:
        op = 10*int(input('''
Conta : ''' + conta_atual +
                   '''
Opções:
[0] - Finalizar o programa
[1] - Sair da conta atual
->:'''))

    return op

# Main 
conta_atual = ""
arquivo_nome = "logs.txt"
menu = {0: finalizar, 1: novo_usuario, 2: logando_usuario, 10:deslogar}
op = 99

while (op != 0):
    
    op = opcoes(conta_atual)

    if(op<2):
        menu[op]()
    else:
        conta_atual = menu[op]()
