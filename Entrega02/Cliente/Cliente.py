class Cliente:
    def __init__(self, nome, email, endereco, telefone):
        self.nome = nome
        self.email = email
        self.endereco = endereco
        self.telefone = telefone
    
    def __str__(self):
        return self.nome
    
    def endereco_atualizado(self, novo_endereco):
        self.endereco = novo_endereco
        print(f"Endereço de {self.nome} atualizado para: {novo_endereco}")
    
    def mostrar_dados(self):
        print(f"Nome: {self.nome}\nEmail: {self.email}\nEndereço: {self.endereco}\nTelefone: {self.telefone}")
