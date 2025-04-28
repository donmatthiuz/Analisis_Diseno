# Parcial 2 Analisis de Algoritmos

[Link al Repositorio](https://github.com/donmatthiuz/Analisis_Diseno/tree/parcial2)

## Integrantes

- Mathew Cordero Aquino [22982]


## Instrucciones

- Debe realizar este examen de forma individual.

-Debe entregar la respuesta a las preguntas planteadas acompa ̃nada de un an ́alisis riguroso y
explicaci ́on pertinente, i.e., no se aceptar ́an respuestas sin procedimiento ni explicaci ́on y la
nota ser ́a autom ́aticamente de cero puntos.

- Entregue un PDF con la resoluci ́on para su parcial y adem ́as grabe un video de no m ́as de
5 minutos de longitud en donde muestre la ejecuci ́on de los programas planteados en cada
problema que usted realice. S ́ubalo a YouTube como no listado e incl ́uyalo en su PDF de
respuestas.

- Duraci ́on: este examen se encontrar ́a habilitado para su realizaci ́on desde el [Fecha Inicial]
hasta el [Fecha Final], por lo que podr ́a realizarlo a su conveniencia en los tiempos que mejor
se ajusten a su intinerario. Solo podr ́a subir sus respuestas una vez, as ́ı que est ́e seguro de las
mismas.

- Este parcial contiene m ́ultiples problemas, con diferente valoraci ́on de puntos. Elija aquella
combinaci ́on de problemas que lo lleve a un punteo completo. Si elije problemas extra, se
tomar ́an como puntos extra que puede utilizar en otras entregas. Se har ́a una regla de tres
con base en la puntuaci ́on total del parcial en puntos netos para definir cu ́antos puntos netos
extra tendr ́a.

- Buena suerte y recuerde que Diosito lo/la est ́a viendo


## Problemas

### 2.2 Problema 2 [40 puntos]

Dada una matriz cuadrada de 0’s y 1’s, calcule el tama˜no de la cruz (s´ımbolo de suma +) m´as grande
formada por 1’s.

Inpu t :

```
g ri d = [
[ 1 , 0 , 1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 ] ,
[ 1 , 0 , 1 , 0 , 1 , 1 , 1 , 0 , 1 , 1 ] ,
[ 1 , 1 , 1 , 0 , 1 , 1 , 0 , 1 , 0 , 1 ] ,
[ 0 , 0 , 0 , 0 , 1 , 0 , 0 , 1 , 0 , 0 ] ,
[ 1 , 1 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 1 ] ,
[ 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 ] ,
[ 1 , 0 , 0 , 0 , 1 , 0 , 0 , 1 , 0 , 1 ] ,
[ 1 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 1 , 1 ] ,
[ 1 , 1 , 0 , 0 , 1 , 0 , 1 , 0 , 0 , 1 ] ,
[ 1 , 0 , 1 , 1 , 1 , 1 , 0 , 1 , 0 , 0 ]
]
```


Output : 17
E x pli c a ci o n : La c r u z ( simb ol o de suma +) mas grande de 1 s s e e n c u e n t r a
aba jo , t e ni e n d o un tamano de 1 7.

![alt text](image.png)

Inpu t :

```
g ri d = [
[ 1 , 1 , 1 , 1 , 1 , 1 ] ,
[ 1 , 0 , 1 , 1 , 0 , 1 ] ,
[ 0 , 1 , 1 , 0 , 0 , 1 ] ,
[ 1 , 1 , 1 , 1 , 1 , 1 ] ,
[ 1 , 0 , 0 , 1 , 0 , 1 ] ,
[ 1 , 0 , 1 , 1 , 0 , 0 ]
]
```


Output : 0
Explicación: No se puede construir una cruz (+) más grande usando los 1s.


- Coloque un enlace a un GitHub Gist privado con la soluci´on. Recuerde que debe crear
tambi´en un video en d´onde muestre la ejecuci´on de su c´odigo. Use como prueba el input
proporcionado. (30 puntos).



- Encuentre el tiempo de complejidad para este algoritmo. Recuerde, deje su procedimiento.
(10 puntos)

```{algoritmo}
n = len(matriz)


left = [[0]*n for _ in range(n)]
right = [[0]*n for _ in range(n)]
top = [[0]*n for _ in range(n)]
bottom = [[0]*n for _ in range(n)]


for i in range(n):
    for j in range(n):
        if matriz[i][j] == 1:
            left[i][j] = (left[i][j-1] if j > 0 else 0) + 1
            top[i][j] = (top[i-1][j] if i > 0 else 0) + 1

# Llenar right y bottom
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if matriz[i][j] == 1:
            right[i][j] = (right[i][j+1] if j < n-1 else 0) + 1
            bottom[i][j] = (bottom[i+1][j] if i < n-1 else 0) + 1

# Encontrar la cruz más grande
max_cross = 0
for i in range(n):
    for j in range(n):
        if matriz[i][j] == 1:
            size = min(left[i][j], right[i][j], top[i][j], bottom[i][j])
            if size >=2:
              max_cross = max(max_cross, 4 * (size - 1) + 1)  # cada brazo más el centro

return max_cross
```
