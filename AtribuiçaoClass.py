class Carro:
    def __init__(self, marca,modelo):
        self.marca = marca
        self.modelo = modelo
    def dirigir(self):
        print(f"Estou dirigindo um carro {self.modelo} da marca {self.marca}")

carro_cls = Carro

meu_carro = carro_cls("Subaru","STI Impreza")
meu_carro.dirigir()