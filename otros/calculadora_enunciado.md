# Actividad: **Práctica Calculadora Básica en Python**

**ID actividad:** PROG-2425-PRUEBA-U1-U2

**Agrupamiento de la actividad**: Individual

---

### Descripción:

La actividad consiste en completar y corregir el desarrollo de una calculadora en Python aplicando los conceptos estudiados en las Unidades 1 y 2. La calculadora permitirá realizar operaciones aritméticas básicas y deberá cumplir con el principio de "Separación de Responsabilidades". Los estudiantes deberán leer y analizar el código provisto, corregir errores y desarrollar las partes incompletas, asegurando la gestión de excepciones.

### Objetivo:

- Leer y analizar la documentación del código para comprender su funcionamiento y aplicar correcciones o completar las partes faltantes de la aplicación.
- Planificar y desarrollar un programa interactivo en Python, estructurando las funciones de manera que cada una tenga una única responsabilidad.
- Aplicar estructuras de control condicional y bucles para resolver problemas de forma eficiente.
- Implementar el manejo de excepciones para asegurar el correcto funcionamiento del programa y prevenir errores en su ejecución.
- Ejecutar pruebas unitarias para validar el comportamiento de las funciones, comprobando que cumplen con los requerimientos establecidos.
- Depurar y revisar el código para mejorar su claridad, consistencia y funcionalidad, y asegurar una documentación adecuada.

### Trabajo a realizar:

1. **Completar las funciones** siguientes, aplicando la documentación y estructura indicadas en el código inicial:
   - **limpiar_pantalla()**: Debe limpiar la pantalla según el sistema operativo.
   - **pausa()**: Pausar la ejecución con un mensaje.
   - **mostrar_error()**: Muestra errores específicos gestionando `IndexError` y otras excepciones.
   - **es_resultado_negativo()**: Verifica si el resultado de la operación debe ser negativo.
   - **multiplicar()** y **dividir()**: Realizan operaciones usando solo sumas y restas.
   - **potencia()**: Calcula el exponente de un número usando multiplicaciones sucesivas. Soporta los operadores `**` y `exp`.
   - **calcular_operacion()**: Llama a las funciones específicas para realizar las operaciones aritméticas.
   - **realizar_calculo()**: Permite realizar operaciones en secuencia, capturando números y operadores del usuario.
   - **sumar()** y **restar()**: Desarrollo completo con documentación para funciones que reciben dos números `float` y devuelven el resultado de la suma o resta de estos.

2. **Organización del Código y Documentación**:
   - Todos los programas deben tener la función `main()` para organizar el flujo del programa.
   - Utilizar `DocStrings` para documentar cada función. Puedes usar el formato que prefieras (Google, reStructuredText, NumPy, o Epytext).

3. **Organización del Repositorio en GitHub**:
   - Colocar todos los archivos de código en la carpeta `src`.
   - Colocar las pruebas unitarias en la carpeta `tests`, nombrando cada prueba de acuerdo con el ejercicio correspondiente (por ejemplo, `test_calculadora.py`).

4. **Pruebas Unitarias**:
   - Ejecutar pruebas unitarias para verificar el correcto funcionamiento de las funciones **realizar_calculo()**, **multiplicar()**, **dividir()**, **potencia()**, y **es_resultado_negativo()**.

---

### Recursos

- [U1: Introducción a la programación en Python](https://revilofe.github.io/section1/u01/).
- [U2: Sentencias condicionales y repetitivas](https://revilofe.github.io/section1/u02/).
- Temario de clase.

---

### Evaluación y calificación

**Conlleva presentación**: NO

---

### Rúbrica de Evaluación:

| **Función**             | **Dificultad (1-5)** | **Descripción de la Dificultad**                                                                          | **0** | **1** | **2** | **3** | **4** | **5** | **Criterios de Evaluación Aplicables**                         |
|-------------------------|----------------------|----------------------------------------------------------------------------------------------------------|-------|-------|-------|-------|-------|-------|----------------------------------------------------------------|
| `limpiar_pantalla`      | 1                    | Desarrollo parcial. Control básico de errores en la función de limpieza.                                 |       |       |       |       |       |       | RA1.a, RA1.e, RA3.a                                           |
| `pausa`                 | 1                    | Desarrollo completo. Implementación de pausa mediante `input()` para detener la ejecución.               |       |       |       |       |       |       | RA1.a, RA3.a                                                 |
| `mostrar_error`         | 2                    | Implementación de gestión de excepciones y mensajes de error usando `IndexError`                         |       |       |       |       |       |       | RA1.f, RA1.g, RA3.a                                           |
| `es_resultado_negativo` | 2                    | Verifica si el resultado de una operación debe ser negativo                                              |       |       |       |       |       |       | RA1.a, RA3.d, RA3.h                                           |
| `sumar`                 | 2                    | Desarrollo completo, incluida la documentación; recibe dos números `float` y retorna la suma de ambos.   |       |       |       |       |       |       | RA1.a, RA3.g, RA3.h                                           |
| `restar`                | 2                    | Desarrollo completo, incluida la documentación; recibe dos números `float` y retorna la resta de ambos.  |       |       |       |       |       |       | RA1.a, RA3.g, RA3.h                                           |
| `multiplicar`           | 4                    | Realiza multiplicación usando sumas sucesivas y ajusta el signo para el resultado                        |       |       |       |       |       |       | RA1.e, RA3.a, RA3.d                                           |
| `dividir`               | 5                    | Realiza división usando restas sucesivas, maneja excepciones para división entre cero                    |       |       |       |       |       |       | RA1.e, RA1.f, RA3.a, RA3.d                                    |
| `potencia`              | 5                    | Calcula potencias usando multiplicaciones y ajusta el signo para el resultado                            |       |       |       |       |       |       | RA1.e, RA1.g, RA3.a, RA3.d, RA3.h                             |
| `calcular_operacion`    | 3                    | Realiza operaciones llamando a funciones específicas según el operador                                   |       |       |       |       |       |       | RA1.a, RA1.g, RA3.b                                           |
| `realizar_calculo`      | 5                    | Realiza cálculo secuencial, guiando al usuario y validando las entradas y operadores                     |       |       |       |       |       |       | RA1.d, RA1.e, RA1.f, RA1.g, RA3.a, RA3.b, RA3.e               |
| `main`                  | 4                    | Organiza el flujo principal del programa, invocando funciones y gestionando el menú de opciones          |       |       |       |       |       |       | RA1.a, RA1.g, RA3.b, RA3.e                                    |
| **Uso único de `return` en funciones** | 3                    | Controla que cada función tenga un único `return` para simplificar el flujo y la legibilidad.             |       |       |       |       |       |       | RA1.a, RA3.g                                                  |
| **Uso adecuado de constantes**       | 1                    | Controla el uso de constantes predefinidas (`MENSAJES_ERROR`, `OPERADORES`) en toda la aplicación.       |       |       |       |       |       |       | RA1.a