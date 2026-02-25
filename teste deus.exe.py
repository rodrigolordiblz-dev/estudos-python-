# deus.exe - O código que tudo pode
class Deus:
    def __init__(self):
        self.universo = {}

    def criar(self, coisa):
        self.universo[coisa] = "existente"
        print(f"{coisa} foi criada.")

    def destruir(self, coisa):
        if coisa in self.universo:
            del self.universo[coisa]
            print(f"{coisa} foi destruída.")
        else:
            print(f"{coisa} não existe.")

    def milagres(self):
        print("Impossível? Apenas uma questão de lógica divina.")


# Executando
deus = Deus()
deus.criar("luz")
deus.criar("vida")
deus.milagres()
