print(2+2)#una operacion severamente sencilla
print(2 ** 3)#una potencia normal
print (2 ** 3.)#una potencia, pero python toma el 3 como un decimal
print(2. ** 3)#lo mismo pasa con esto, agrega los ceros
print(2. ** 3.)#cuando almenos un argumento es flotante (decimal)
#el resultado tambien es decimal
#si ambos son enteros, el resultado es entero
print(6 / 3)
print(6 / 3.)#cuando hablamos de division..
print(6. / 3.)#..el resultado siempre es flotante

print( 6 // 3)
print(6 // 3.)#la excepcion del resultado flotante es cuando usamos la division entera
print(6. // 3.)#la division entera siempre redondea hacia abajo
print(-6 // 4)
print(6. // -4)# el resultado es negativo, pero no es el mismo de antes
#ya que siempre redondea al numero menor, este valor, seria -2 y -2.0

print(14 % 4) # no hacer divisiones, multiplicaciones y modulaciones entre 0
print(4 * 2 ** 3 / 8 + 1)