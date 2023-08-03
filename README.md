# Matrix

El programa muestra una animación de caracteres que caen en cascada, similar al código verde visto en la película "The Matrix". Los caracteres se generan aleatoriamente y descienden verticalmente por la pantalla en columnas. Se utiliza una fuente personalizada llamada "Matrix Code NFI" para crear la estética digital y futurista del efecto.

El tamaño de la ventana y la fuente del texto están configurados para crear el efecto deseado. Los caracteres se borran y se desvanecen mientras caen para lograr el efecto de movimiento fluido y enigmático.

El programa se ejecuta en un bucle principal, donde se actualiza la posición de los caracteres en cada columna y se pinta en la pantalla. La animación continúa hasta que el usuario cierra la ventana.

Este código crea un interesante efecto de caída de caracteres en cascada inspirado en "The Matrix" y brinda al usuario algunas opciones de personalización en cuanto al color y la velocidad de la animación. Es importante tener en cuenta que para ejecutar este programa, es necesario tener instalada la fuente "Matrix Code NFI" en el sistema.

Se da soporte para pantalla completa presionando la tecla f, durante su ejecución, otras opciones de personalización durante la ejecución son:

        f        para alternar entre pantalla completa o ventana
        q        para salir
        +        para aumentar la velocidad
        -        para disminuir la velocidad
        r,g,b,a  para cambiar color r:Rojo, g:Verde, b:Azul, a:Ambar
       


El programa permite algunas opciones configurables al iniciarse mediante argumentos en la línea de comandos:

      -c:       Permite especificar el color de los caracteres. Por defecto, es verde.
      -v:       Permite ajustar la velocidad de la animación en fotogramas por segundo (FPS). Por defecto, es 15 FPS.
      -f        Inicia pantalla completa, para quitar la pantalla completa presionar f"

Ejemplo:

      matrix
Efecto matrix con caracteres color VERDE y velocidad de 15 FPS
![Descripción de la imagen](/imgMatrix.png)



      matrix -c "#ff7e00" 5 -v 10

Efecto matrix con caracteres color AMBAR y velocidad de 10 FPS
![Descripción de la imagen](/imgMatrix2.png)

