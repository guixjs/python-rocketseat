class Animal:
  def __init__(self, nome):
    self.nome = nome
  def emitirSom(self,):
    pass

class Cachorro(Animal):
  def emitirSom(self):
    return "latido"
  
class Gato(Animal):
  def emitirSom(self):
    return "miado"

cachorro = Cachorro("princesa")
gatinho = Gato("peludo")
print(cachorro.nome)
print(gatinho.nome)


# ENCAPSULAMENTO
class ContaBancaria():
  def __init__(self,saldo):
    self.__saldo = saldo # Para criar um atributo "private" adiciona o "__" 
  
  def sacar(self, valor):
    if valor > 0 and valor < self.__saldo:
      self.__saldo -= valor

  def depositar(self,valor):
    if valor > 0:
      self.__saldo += valor

  def consultar_saldo(self):
    return self.__saldo


conta = ContaBancaria(1000)

print(f"O saldo inicial é {conta.consultar_saldo()}")
conta.depositar(100)
print(f"O saldo depois de depositar é {conta.consultar_saldo()}")
conta.sacar(300)
print(f"O saldo depois de sacar é {conta.consultar_saldo()}")

print("\nAbstração")
from abc import ABC, abstractmethod

class Veiculo(ABC):

  @abstractmethod
  def ligar(self):
    pass
  @abstractmethod
  def desligar(self):
    pass


class Carro(Veiculo):
  def __init__(self):
    pass
  def ligar(self):
    return "Carro ligou"
  def desligar(self):
    return "carro desligou"
  
carro_automatico = Carro()

print(carro_automatico.ligar())
print(carro_automatico.desligar())