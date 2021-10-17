1) Crea una semilla random para repetir los resultados y corroborarlos
2) genera un array de 3 numeros si no hay argumento y en el caso de haberlo genera una lista de ints con esos argumentos
3) Inicia un contador de tiempo para el programa entero
4) Crea un nuevo event loop llamando a la funcion main a traves de run
5) La funcion main llama de forma asincrona con gather a la funcion chain de acuerdo al numero de argumentos dado y esperara hasta que retornen un resultado
6) Cada tarea(segun el numero de args) ejecutara la funcion primera y espera su resultado
7) La funcion primera dormira por un tiempo random y retorna un string como su resultado
8) El control retorna a la funcion chain la cual llamara a la funcion segunda y espera su resultado. Se debe aclarar que esto se realizara de forma asincrona por lo cual de acuerdo al tiempo random, terminaran en diferente orden y la funcion segunda de cada tarea sera llamada en diferente orden. 
Debido a que la funcion main es la unica tarea que debe esperar el resultado de las demas, ya que fue llamada utilizando gather, la cual toma los resultados de las subtareas, cada subtarea chain no espera a las demas, por lo que una de esta podria terminar su ejecucion antes de que una de las otras termine la primera tarea.
9) La funcion segunda espera otro tiempo random y devuelve un string como resultado
10) Cada tarea chain imprime su resultado de forma asincrona y termina
11) Una vez que cada tarea chain termina, la funcion main puede continuar, donde calculara el tiempo total de ejecucuion y lo mostrara por pantalla
