
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





# Problema 1:
print("\nProblema 1:")
print("\nMTF:")
move_to_front = MTF_Algoritms([0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4])
move_to_front.forSecuence(algoritmo= "MTF")
costo_mtf_1 = move_to_front.costo

print("\nIMTF:")
move_to_front_imtf = MTF_Algoritms([0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4])
move_to_front_imtf.forSecuence(algoritmo= "IMTF")
costo_imtf_1 = move_to_front_imtf.costo

# Problema 2:
print("\nProblema 2:")
print("\nMTF:")
move_to_front = MTF_Algoritms([0, 1, 2, 3, 4], [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4])
move_to_front.forSecuence(algoritmo= "MTF")
costo_mtf_2 = move_to_front.costo

print("\nIMTF:")
move_to_front_imtf = MTF_Algoritms([0, 1, 2, 3, 4], [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4])
move_to_front_imtf.forSecuence(algoritmo= "IMTF")
costo_imtf_2 = move_to_front_imtf.costo


# Problema 3:
print("\nProblema 3:")
print("\nMTF:")
move_to_front = MTF_Algoritms([0, 1, 2, 3, 4], [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0,0])
move_to_front.forSecuence(algoritmo= "MTF")
costo_mtf_3 = move_to_front.costo

print("\nIMTF:")
move_to_front_imtf = MTF_Algoritms([0, 1, 2, 3, 4], [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0,0])
move_to_front_imtf.forSecuence(algoritmo= "IMTF")
costo_imtf_3 = move_to_front_imtf.costo


# Problema 4:
print("\nProblema 4:")

print("MTF:")
move_to_front = MTF_Algoritms([0, 1, 2, 3, 4], [4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0])
move_to_front.forSecuence(algoritmo= "MTF")
costo_mtf_4 = move_to_front.costo

print("\nIMTF:")
move_to_front_imtf = MTF_Algoritms([0, 1, 2, 3, 4], [4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0])
move_to_front_imtf.forSecuence(algoritmo= "IMTF")
costo_imtf_4 = move_to_front_imtf.costo


# Problema 5:
print("\nProblema 5:")

print("MTF:")
move_to_front = MTF_Algoritms([0, 1, 2, 3, 4], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
move_to_front.forSecuence(algoritmo= "MTF")
costo_mtf_5 = move_to_front.costo

print("\nIMTF:")
move_to_front_imtf = MTF_Algoritms([0, 1, 2, 3, 4], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
move_to_front_imtf.forSecuence(algoritmo= "IMTF")
costo_imtf_5 = move_to_front_imtf.costo


# Ejercicio 5 parte 2

print("MTF:")
move_to_front = MTF_Algoritms([0, 1, 2, 3, 4], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
move_to_front.forSecuence(algoritmo= "MTF")
costo_mtf_5_2 = move_to_front.costo

print("\nIMTF:")
move_to_front_imtf = MTF_Algoritms([0, 1, 2, 3, 4], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
move_to_front_imtf.forSecuence(algoritmo= "IMTF")
costo_imtf_5_2 = move_to_front_imtf.costo



print("\nResumen de resultados:")
print(f"{'Problema':<10} | {'MTF':<10} | {'IMTF':<10}")
print("-" * 35)
print(f"{'1':<10} | {costo_mtf_1:<10} | {costo_imtf_1:<10}")
print(f"{'2':<10} | {costo_mtf_2:<10} | {costo_imtf_2:<10}")
print(f"{'3':<10} | {costo_mtf_3:<10} | {costo_imtf_3:<10}")
print(f"{'4':<10} | {costo_mtf_4:<10} | {costo_imtf_4:<10}")
print(f"{'5.1':<10} | {costo_mtf_5:<10} | {costo_imtf_5:<10}")
print(f"{'5.2':<10} | {costo_mtf_5_2:<10} | {costo_imtf_5_2:<10}")
