# Prueba Práctica U1 y U2 - Calculadora Básica en Python

## Objetivo:
Completar el desarrollo de una calculadora que permite realizar operaciones básicas de manera interactiva en la consola. Este ejercicio integra conceptos de las Unidades 1 y 2.

## Descripción:
Tienes un código de una calculadora en Python parcialmente desarrollado. Algunas funciones están incompletas, y otras necesitan corrección. El objetivo es que completes el código y asegures su correcto funcionamiento siguiendo las pautas y completando los comentarios indicados en el código.

## Instrucciones:
1. **Revisa el Código Inicial**: Observa el archivo y revisa los comentarios y documentación para entender cada función y la estructura general.
   
2. **Funciones Principales a Desarrollar y Completar**:
   - **limpiar_pantalla()**: Debe limpiar la pantalla en función del sistema operativo (Windows, Linux/macOS). Implementa el manejo de excepciones adecuado.
   - **pausa()**: Pausa la ejecución con el mensaje `"\nPresione ENTER para continuar..."`.
   - **mostrar_error()**: Completa la función para manejar errores de forma profesional. Debe gestionar:
     - **IndexError**: Mostrar "\n*ERROR* Mensaje de error no definido.\n".
     - **Excepciones generales**: Captura cualquier otro tipo de excepción y muestra el mensaje "\n*ERROR* Problemas al mostrar error!\n{e}\n".
   - **es_resultado_negativo()**: Esta función verifica si el resultado de una operación debe ser negativo.
   - **multiplicar()** y **dividir()**: Completa el código de estas funciones para que realicen operaciones enteras usando sumas y restas, redondeando los números recibidos a enteros.
   - **pedir_entrada()**: Debe limpiar y convertir a minúsculas cualquier entrada de usuario.
   - **calcular_operacion()**: Realiza operaciones matemáticas específicas llamando a las funciones adecuadas.
   - **obtener_operaciones()**: Esta función debe mostrar una lista de las operaciones que el programa puede realizar.
   - **realizar_calculo()**: Implementa el cálculo secuencial, manejando adecuadamente operadores y números, guiando al usuario para introducir la información paso a paso.

3. **Condiciones Especiales**:
   - **Error Handling**: Todos los mensajes de error deben mostrarse usando `mostrar_error()`; no se permite utilizar `print()` directamente para errores.
   - **Funciones de una Sola Salida**: Asegúrate de que cada función tenga **solo una instrucción `return`**.

4. **Ejecución Principal**:
   - Corrige y completa el flujo de `main()` según lo descrito en su documentación.
   - Al ejecutar el programa en `main`, asegúrate de que funcione sin errores y siga el flujo especificado en el comentario de la función `main`.

## Evaluación:
1. **Corrección y Completitud**: Cada función debe cumplir con su objetivo y la documentación provista.
2. **Control de Errores**: Los errores deben gestionarse adecuadamente a través de `mostrar_error`.
3. **Pruebas Unitarias**: La implementación debe cumplir las pruebas para verificar su funcionalidad, especialmente para `es_resultado_negativo()`, `multiplicar()`, y `dividir()`.

## Puntos Adicionales:
- Se evaluará la claridad y la limpieza del código, así como la precisión en el uso de funciones y flujo de control.
  
**Entrega**: Subir el archivo Python completo y funcional en el sistema indicado antes de la fecha límite.