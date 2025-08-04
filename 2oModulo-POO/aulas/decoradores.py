# decoradores em python são bem parecidos com annotations no spring
# decoradores são funções que modificam o comportamento de outras funções sem mudar o código original da função 

def meu_decorador(func):
  def wrapper(): # envolvendo a função
    print("modificando a função antes de chamar (método)")
    func() # chamando a função original
    print("modificando a função depois de chamar (método)")
    
  return wrapper # retorna a função "modificada"
  
@meu_decorador # decorador sendo chamado para essa função 
def funcao_que_vai_ser_modificada():
  print("Essa função será modificada")

funcao_que_vai_ser_modificada()

print("\n\n\n")
# FAZENDO ATRAVÉS DE CLASSES ==========

class MinhaClasseDecoradora:
  def __init__(self,func):
    self.func = func

  def __call__(self): # tipo o wrapper, um método padrão 
    print("Chamada antes da funcao (classe)")
    self.func()
    print("Chamada depois da funcao (classe)")


@MinhaClasseDecoradora
def segunda_funcao():
  print("segunda funcao que também vai ser modificada")


segunda_funcao()