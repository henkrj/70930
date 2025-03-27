class Listagem:
    def __init__(self, elementos):
        self.elementos = elementos

    def __getitem__(self, index):
        return self.elementos[index]  # Permite acessar como lista

    def __setitem__(self, index, value):
        self.elementos[index] = value  # Permite modificar como lista

    def __len__(self):
        return len(self.elementos)  # Permite usar len(obj)
    
    def __str__(self):
        return f'Esta lista tem {len(self.elementos)} elementos.\nSão eles:\n{self.elementos}'
    
def criar_classe (x):
    resultado = Listagem(x)
    return resultado


