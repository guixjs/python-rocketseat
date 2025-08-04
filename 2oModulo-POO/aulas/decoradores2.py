# @classmethod - um decorador que informa que aquele método é só da classe, não da instância
# @staticmethod - um decorador que informa que aquele método é da classe mas não recebe referência da classe

class Carro:
  def __init__(self, modelo, marca, ano):
    self.modelo = modelo;
    self.marca = marca;
    self.ano = ano;
  
  @classmethod # metodo da classe, nao precisa de instancia, precisa do parametro cls
  def criar_carro(cls, configuracao):
    modelo,marca,ano = configuracao_do_carro.split(",")
    return cls(modelo,marca,int(ano))


configuracao_do_carro = "Renegade,Jeep,2025"


carro = Carro.criar_carro(configuracao_do_carro)

print(f"Marca do carro: {carro.marca}")
print(f"Modelo do carro: {carro.modelo}")
print(f"Ano do carro: {carro.ano}")