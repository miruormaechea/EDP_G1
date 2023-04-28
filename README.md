
# EDP_G1

Codigo para el trabajo practico de la Materia Estructuras de Datos y Programacion - ITBA

  

## Feedback Ian

  
- Esta muy bueno eso del mail valido, es más, hay un paquete que se llama validate mail que verifica que realmente existe y se puede enviar un mail.
	- Obviamente no usen eso. Lo digo de dato curioso nomas.

- Creo que ya lo habían implementado antes pero lo borraron. Intenten usar switch statements ya que hace el código más legible

- Como ya saben usar diccionarios les diria que cuando generen el txt, usen JSON. Entonces a la hora de buscar la contraseña solo tienen que hacer usuarios.get(nombre_de_usuario) y verificar que lo que devuelva sea la contraseña que buscan ustedes.

- Si van a usar csv les diría que utilicen los headers. Esto les va a permitir usar csv.DictReader() para obtener una lista de diccionarios, así no tienen que llamar a lista[1]. Es mucho más legible lista.get('nombres')

- Tambien les permitiria agregar una funcion en Cliente que devuelva un diccionario con todos los elementos importantes.

- Están guardando el cliente en Tienda.lista_clientes pero nunca lo declaran. Python llama a una función que no existe y tira error

- Tampoco está muy bueno usar esas variables para estos casos, ya que el software que crean se podría usar para múltiples tiendas

	- Si bien es solo para esta tienda, esta bueno generalizarlo para que despues puedan adaptar el codigo a otros proyectos.

- Sobre los pedidos esta bueno eso de repetir pedido. Lo que si, en vez de poner 1 para volver a pedir y preguntar por el numero despues, ofreceria al usuario seleccionar el pedido que quiere repetir y si no pone nada asuman que quiere volver al menu.

- No hagan una lista global de pedidos, guardenla en la tienda por lo mismo que dije antes.

- Se podria hacer que el usuario mismo guarde su lista de pedidos, asi pasan de una velocidad de consulta de O(N) a un O(1) ya que no tienen que escanear la lista completa cada vez que corren la lista de pedidos.

- Les recomendaría usar pickles para guardar el objeto tienda. Pickle guarda el objeto como viene de la memoria a un archivo binario

	- Esto les permite hacer que la tienda tenga una lista de objetos de clientes y que los clientes tengan su lista de objetos de pedidos sin necesidad de hacer un json/csv todo complicado

- Esta bueno eso que usen funciones para que el menú no sea muy grande, lo hace más fácil de saber qué pasa.

- Estaría bueno que lo lleven un paso más y que hagan un archivo con cada una de las clases así no tienen bloques grandes de texto en el medio para buscar algo en particular.

  

### Arreglar


- Hay un error en el código para crear usuarios. Esta mal indentado y va a guardar el usuario y contraseña casi infinitas veces.

- La información que le piden al usuario cuando generan la cuenta se pierde cuando cierran el programa.

- Intenten usar direcciones relativas, no absolutas. El programa me crasheo al intentar generar el usuario

	- En caso de que no exista un archivo, genérenlo

- En algunas partes del código usan elif para hacer lo que efectivamente es un else.

- Cuando quieren ver si le pasaron un dato pueden hacer if dato:.

	- Ojo con esto si se puede pasar un dato numérico ya que tanto None como 0 va a dar falso

	- Porque hacerlo entonces? Personalmente se lee más fácil.