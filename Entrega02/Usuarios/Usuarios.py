usuarios = {}

def registrar_usuario():
    while True:
        nome = input("Digite um nome de usuário: ")
        if nome in usuarios:
            print("Nome de usuário indisponível. Tente outro!")
        else:
            senha = input("Digite uma senha: ")
            usuarios[nome] = senha
            print("Usuário cadastrado com sucesso!")
            break

def exibir_usuarios():
    if len(usuarios) > 0:
        print("Lista de usuários cadastrados:")
        for nome in usuarios.keys():
            print(f"- {nome}")
    else:
        print("Ainda não há usuários cadastrados.")

def login_usuario():
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite sua senha: ")
    
    if nome in usuarios:
        if usuarios[nome] == senha:
            print(f"Bem-vindo(a), {nome}! Login realizado com sucesso.")
        else:
            print("Senha incorreta. Tente novamente.")
    else:
        print("Usuário não encontrado.")
