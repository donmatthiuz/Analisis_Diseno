
class MTF ():
  def __init__(self, lista, secuencia):
    self.lista = lista
    self.secuencia = secuencia
    self.costo = 0
  
  def move_to_front(self, number):
    if number in self.lista:
      posicion = self.lista.index(number)
      valor = self.lista.pop(posicion)
      self.lista.insert(0, valor)
      print(f"Lista : {self.lista} | Numero : {number}")
      self.costo += posicion

  def forSecuence(self):
    for numero in self.secuencia:
      self.move_to_front(numero)
    print(f"Costo total {self.costo}")



move_to_front = MTF([0,1,2,3,4], [0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4])

move_to_front.forSecuence()

  

