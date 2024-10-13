import pytest

from src.adivinar_numero_v3 import (
    evaluar_distancia, generar_pista, mostrar_pista,
    adivina_el_numero, comprobar_numero_entero, pedir_numero_usuario,
    configurar_rangos_numeros, configurar_pistas, configurar_intentos,
    genera_numero_oculto
)

###################################################################################################

@pytest.mark.parametrize(
    "numero, numero_oculto, frio, caliente, expected",
    [
        (50, 100, 30, 10, "* FRÍO, FRÍO,"),
        (85, 100, 30, 10, "* CALIENTE, CALIENTE,"),
        (99, 100, 30, 10, "* TE QUEMAS,"),
    ]
)
def test_evaluar_distancia(numero, numero_oculto, frio, caliente, expected):
    assert evaluar_distancia(numero, numero_oculto, frio, caliente) == expected

###################################################################################################

@pytest.mark.parametrize(
    "numero, numero_oculto, intentos, expected",
    [
        (50, 100, 5, "el número oculto es MAYOR... ¡te quedan 5 intentos!\n"),
        (90, 100, 3, "el número oculto es MAYOR... ¡te quedan 3 intentos!\n"),
        (98, 100, 2, "el número oculto es MAYOR... ¡te quedan 2 intentos!\n"),
        (150, 100, 1, "el número oculto es MENOR... ¡te quedan 1 intentos!\n")
    ]
)
def test_generar_pista(numero, numero_oculto, intentos, expected):
    assert generar_pista(numero, numero_oculto, intentos) == expected

###################################################################################################

@pytest.mark.parametrize(
    "numero, numero_oculto, intentos, frio, caliente, expected_output",
    [
        (50, 100, 5, 20, 10, "\n* FRÍO, FRÍO, el número oculto es MAYOR... ¡te quedan 5 intentos!\n\n"),
        (85, 100, 3, 20, 10, "\n* CALIENTE, CALIENTE, el número oculto es MAYOR... ¡te quedan 3 intentos!\n\n"),
        (98, 100, 2, 20, 10, "\n* TE QUEMAS, el número oculto es MAYOR... ¡te quedan 2 intentos!\n\n"),
        (150, 100, 1, 20, 10, "\n* FRÍO, FRÍO, el número oculto es MENOR... ¡te quedan 1 intentos!\n\n"),
    ]
)
def test_mostrar_pista(capsys, numero, numero_oculto, intentos, frio, caliente, expected_output):
    mostrar_pista(numero, numero_oculto, intentos, frio, caliente)
    captured = capsys.readouterr()
    assert captured.out == expected_output 

###################################################################################################

@pytest.mark.parametrize(
    "numero_oculto, total_intentos, frio, caliente, mock_inputs, expected_result, expected_intentos",
    [
        (100, 5, 20, 10, ['50', '75', '90', '100'], True, 4),  # Adivina en el 4º intento
        (100, 3, 20, 10, ['50', '75', '90'], False, 3),        # No adivina en los 3 intentos
        (100, 2, 20, 10, ['98', '100'], True, 2),              # Adivina en el último intento
        (100, 4, 20, 10, ['150', '140', '120', '100'], True, 4),  # Adivina en el 4º intento
    ]
)
def test_adivina_el_numero(monkeypatch, numero_oculto, total_intentos, frio, caliente, mock_inputs, expected_result, expected_intentos):
    # Simular las entradas del usuario
    inputs_iter = iter(mock_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_iter))

    # Ejecutar la función y capturar el resultado
    result, intentos_realizados = adivina_el_numero(numero_oculto, total_intentos, frio, caliente)

    # Probar si el número fue adivinado correctamente
    assert result == expected_result
    # Probar si el número de intentos realizados es el esperado
    assert intentos_realizados == expected_intentos

###################################################################################################

@pytest.mark.parametrize(
    "valor, expected",
    [
        ("100", True),
        ("-50", True),
        ("abc", False),
        ("12.5", False),
        ("", False),
    ]
)
def test_comprobar_numero_entero(valor, expected):
    assert comprobar_numero_entero(valor) == expected

###################################################################################################

@pytest.mark.parametrize(
    "minimo, maximo",
    [
        (0, 100),
        (-100, 0),
        (50, 150),
    ]
)
def test_genera_numero_oculto(minimo, maximo):
    numero_oculto = genera_numero_oculto(minimo, maximo)
    assert minimo <= numero_oculto <= maximo

###################################################################################################

@pytest.mark.parametrize(
    "frio, caliente, expected",
    [
        (30, 10, True),
        (50, 25, True),
    ]
)
def test_configurar_pistas(frio, caliente, expected):
    result = frio > caliente
    assert result == expected

###################################################################################################

@pytest.mark.parametrize(
    "mock_inputs, expected",
    [
        (['  10'], 10),            # Entrada válida con espacios
        (['-5'], -5),              # Número negativo válido
        (['0'], 0),                # Número cero
        (['abc', '10'], 10),       # Entrada no válida seguida de entrada válida
        (['', '100'], 100),        # Entrada vacía seguida de número válido
    ]
)
def test_pedir_numero_usuario(mock_inputs, expected, monkeypatch):
    # Simular múltiples entradas del usuario usando monkeypatch
    inputs_iter = iter(mock_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_iter))
    
    # Llamar a la función y comparar el resultado con lo esperado
    assert pedir_numero_usuario("Introduce un número: ") == expected

###################################################################################################

@pytest.mark.parametrize(
    "mock_inputs, expected",
    [
        (['0', '200'], (0, 200)),        # Rango válido con diferencia de 100
        (['100', '500'], (100, 500)),    # Otro rango válido
        (['50', '50', '50', '200'], (50, 200)),  # Caso inválido (misma entrada dos veces) seguido de entrada válida
        (['0', '50', '0', '150'], (0, 150)),     # Caso inválido (diferencia menor a 100) seguido de entrada válida
    ]
)
def test_configurar_rangos_numeros(mock_inputs, expected, monkeypatch):
    # Simular entradas para mínimo y máximo
    inputs_iter = iter(mock_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_iter))
    
    # Probar si el rango es configurado correctamente
    assert configurar_rangos_numeros() == expected

###################################################################################################

@pytest.mark.parametrize(
    "mock_inputs, minimo, maximo, expected",
    [
        (['20', '10'], 0, 100, (20, 10)),    # Pistas válidas: frío > caliente y dentro del rango
        (['30', '15'], 1, 200, (30, 15)),  # Otro set válido dentro del rango
        (['10', '10', '25', '5'], 0, 100, (25, 5)),  # Caso inválido (frío y caliente iguales) seguido de entrada válida
        (['60', '70', '50', '10'], 0, 100, (50, 10)),  # Caso inválido (frío < caliente) seguido de entrada válida
    ]
)
def test_configurar_pistas(mock_inputs, minimo, maximo, expected, monkeypatch):
    # Simular entradas para frío y caliente
    inputs_iter = iter(mock_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_iter))
    
    # Probar si las pistas son configuradas correctamente
    assert configurar_pistas(minimo, maximo) == expected

###################################################################################################

@pytest.mark.parametrize(
    "mock_input, expected",
    [
        (['5'], 5),    # Intentos válidos
        (['10'], 10),  # Otro valor válido
        (['-1', '7'], 7),    # Caso inválido (número negativo) seguido de entrada válida
        (['0', '20'], 20), # Caso inválido (entrada no numérica) seguido de entrada válida
    ]
)
def test_configurar_intentos(mock_input, expected, monkeypatch):
    # Simular la entrada para el número de intentos
    inputs_iter = iter(mock_input)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_iter))
    
    # Probar si los intentos son configurados correctamente
    assert configurar_intentos() == expected
