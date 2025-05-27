
class MTF_Algoritms ():
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
      self.costo += posicion + 1

  def i_move_to_front(self, number):
    if number in self.lista:
      posicion = self.lista.index(number)
      next = posicion - 1 + posicion
      elementos = self.secuencia[posicion:next]
      if number in elementos:
        valor = self.lista.pop(posicion)
        self.lista.insert(0, valor)
      print(f"Lista : {self.lista} | Numero : {number}")
      self.costo += posicion + 1

  def forSecuence(self, algoritmo= "MTF"):
    self.costo = 0
    for numero in self.secuencia:
      if algoritmo == "MTF":
        self.move_to_front(numero)
      elif algoritmo == "IMTF":
        self.i_move_to_front(numero)
    print(f"Costo total {self.costo}")



move_to_front = MTF_Algoritms([1,2,3], [3 ,2, 1, 3,2])
move_to_front.forSecuence(algoritmo= "MTF")
move_to_front.forSecuence(algoritmo= "IMTF")

  

