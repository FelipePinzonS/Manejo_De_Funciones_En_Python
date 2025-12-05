# Manejo de funciones en Python

## Nombre: Felipe Pinzon Segura
## Marticula: 2530495
## Grupo: IM 1-2

# Resumen Ejecutivo
"""
Una función en Python es un bloque reutilizable de código que realiza una tarea
específica y que se define utilizando la palabra clave def. Gracias a las
funciones, es posible organizar mejor el código, evitar repeticiones y hacer
los programas más modulares y fáciles de mantener.

Los parámetros son variables que una función recibe para trabajar con ellas,
mientras que los argumentos son los valores reales enviados cuando la función
es llamada. Utilizar funciones permite una separación más clara de la lógica,
facilitando la lectura, pruebas y depuración.

El uso de valores de retorno (return) hace posible que las funciones entreguen
resultados a otras partes del programa, permitiendo cálculos más complejos y una
mayor flexibilidad.

Este documento muestra seis problemas que ilustran: definición de funciones,
parámetros obligatorios y opcionales, valores de retorno, funciones puras,
procesamiento de listas y cálculos matemáticos.
"""

# Principles & Good Practices (short list)
"""
- Preferir funciones pequeñas con una sola responsabilidad.
- Evitar repetición de código usando funciones reutilizables.
- Utilizar nombres descriptivos (por ejemplo: calculate_area).
- Validar entradas dentro de las funciones cuando aplique.
- Usar return en lugar de imprimir desde la función para mayor flexibilidad.
- Separar la lógica del programa en funciones para mejor organización.
"""

# PROBLEM 1: Rectangle area and perimeter
"""
Description: Defines two functions to calculate area and perimeter of a rectangle.
 The main code reads dimensions, calls the functions, and displays results.

Inputs:
- width (float)
- height (float)

Outputs:
- "Area:" <area_value>
- "Perimeter:" <perimeter_value>

Validations:
- width > 0
- height > 0
- Otherwise show "Error: invalid input"

Test cases:
1) Normal: width = 5.0, height = 3.0 → Area: 15.0, Perimeter: 16.0
2) Border: width = 0.1, height = 0.1 → Area: 0.01, Perimeter: 0.4
3) Error: width = -5.0, height = 3.0 → "Error: invalid input"
"""

def calculate_area(width, height):
    """Calculate area of a rectangle."""
    return width * height

def calculate_perimeter(width, height):
    """Calculate perimeter of a rectangle."""
    return 2 * (width + height)

def problemone():
    print("\n PROBLEM 1: Rectangle area and perimeter")
    
    try:
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
    except ValueError:
        print("Error: invalid input")
        return
    
    if width <= 0 or height <= 0:
        print("Error: invalid input")
        return
    
    area = calculate_area(width, height)
    perimeter = calculate_perimeter(width, height)
    
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")


# PROBLEM 2: Grade classifier (function with return string)

"""

Description: Defines a function that receives a numerical score (0-100) and 
 returns a letter grade category (A, B, C, D, F).

Inputs:
- score (float or int)

Outputs:
- "Score:" <score>
- "Category:" <grade_letter>

Validations:
- 0 <= score <= 100
- Otherwise show "Error: invalid input"

Test cases:
1) Normal: score = 85 → Category: B
2) Border: score = 90 → Category: A
3) Error: score = 105 → "Error: invalid input"
"""

def classify_grade(score):
    """Classify numerical score into letter grade category."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def problemtwo():
    print("\n=== PROBLEM 2: Grade classifier ===")
    
    try:
        score = float(input("Enter score (0-100): "))
    except ValueError:
        print("Error: invalid input")
        return
    
    if score < 0 or score > 100:
        print("Error: invalid input")
        return
    
    category = classify_grade(score)
    print(f"Score: {score}")
    print(f"Category: {category}")


# PROBLEM 3: List statistics function (min, max, average)

"""
Description: Defines a function that receives a list of numbers and returns
 a dictionary with minimum, maximum, and average values.

Inputs:
- numbers_text (string; e.g., "10,20,30")

Outputs:
- "Min:" <min_value>
- "Max:" <max_value>
- "Average:" <average_value>

Validations:
- numbers_text not empty after strip()
- Resulting list not empty
- All elements convertible to numbers
- Otherwise show "Error: invalid input"

Test cases:
1) Normal: "10,20,30" → Min: 10, Max: 30, Average: 20.0
2) Border: "5" → Min: 5, Max: 5, Average: 5.0
3) Error: "10,abc,30" → "Error: invalid input"
"""

def summarize_numbers(numbers_list):
    """Calculate statistics for a list of numbers."""
    return {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }

def problemthree():
    print("\n=== PROBLEM 3: List statistics function ===")
    
    numbers_text = input("Enter numbers separated by commas: ").strip()
    
    if not numbers_text:
        print("Error: invalid input")
        return
    
    number_strings = numbers_text.split(',')
    numbers = []
    
    for num_str in number_strings:
        try:
            number = float(num_str.strip())
            numbers.append(number)
        except ValueError:
            print("Error: invalid input")
            return
    
    if len(numbers) == 0:
        print("Error: invalid input")
        return
    
    stats = summarize_numbers(numbers)
    
    print(f"Min: {stats['min']}")
    print(f"Max: {stats['max']}")
    print(f"Average: {stats['average']:.2f}")


# PROBLEM 4: Apply discount list (pure function)

"""
Description: Defines a function that applies discount to a list of prices and
 returns a new list without modifying the original.

Inputs:
- prices_text (string; e.g., "100,200,300")
- discount_rate (float, between 0 and 1)

Outputs:
- "Original prices:" <original_list>
- "Discounted prices:" <discounted_list>

Validations:
- prices_text not empty and resulting list not empty
- All prices > 0
- 0 <= discount_rate <= 1
- Otherwise show "Error: invalid input"

Test cases:
1) Normal: prices="100,200,300", discount=0.1 → Discounted: [90,180,270]
2) Border: prices="50", discount=0.0 → Discounted: [50]
3) Error: prices="100,200", discount=1.5 → "Error: invalid input"
"""

def apply_discount(prices_list, discount_rate):
    """Apply discount to list of prices and return new list."""
    discounted_prices = []
    for price in prices_list:
        discounted_price = price * (1 - discount_rate)
        discounted_prices.append(discounted_price)
    return discounted_prices

def problemfour():
    print("\n PROBLEM 4: Apply discount list ")
    
    prices_text = input("Enter prices separated by commas: ").strip()
    
    if not prices_text:
        print("Error: invalid input")
        return
    
    try:
        discount_rate = float(input("Enter discount rate (0-1): "))
    except ValueError:
        print("Error: invalid input")
        return
    
    price_strings = prices_text.split(',')
    original_prices = []
    
    for price_str in price_strings:
        try:
            price = float(price_str.strip())
            if price <= 0:
                print("Error: invalid input")
                return
            original_prices.append(price)
        except ValueError:
            print("Error: invalid input")
            return
    
    if len(original_prices) == 0:
        print("Error: invalid input")
        return
    
    if discount_rate < 0 or discount_rate > 1:
        print("Error: invalid input")
        return
    
    discounted_prices = apply_discount(original_prices, discount_rate)
    
    print(f"Original prices: {original_prices}")
    print(f"Discounted prices: {[round(price, 2) for price in discounted_prices]}")


# PROBLEM 5: Greeting function with default parameters

"""

Description: Defines a function that creates greeting messages with optional title.
 Demonstrates positional and named arguments.

Inputs:
- name (string)
- title (string, optional)

Outputs:
- "Greeting:" <greeting_message>

Validations:
- name not empty after strip()
- title can be empty, but if not, also normalized with strip()

Test cases:
1) Normal: name="Gerardo", title="Dr." → "Hello, Dr. Gerardo!"
2) Border: name="Evan", title="" → "Hello, Evan!"
3) Error: name="   " → "Error: invalid input"
"""

def greet(name, title=""):
    """Generate greeting message with optional title."""
    name = name.strip()
    title = title.strip()
    
    if title:
        full_name = f"{title} {name}"
    else:
        full_name = name
    
    return f"Hello, {full_name}!"

def problemfive():
    print("\n PROBLEM 5: Greeting function with default parameters")
    
    name = input("Enter name: ").strip()
    if not name:
        print("Error: invalid input")
        return
    
    title = input("Enter title (optional): ").strip()
    
    # Demonstrate different ways to call the function
    if title:
        # Using named arguments
        message1 = greet(name=name, title=title)
        # Using positional arguments
        message2 = greet(name, title)
    else:
        # Using only required argument
        message1 = greet(name)
        message2 = greet(name=name)
    
    print(f"Greeting: {message1}")
    print(f"Alternative call: {message2}")


# PROBLEM 6: Factorial function (iterative or recursive)

"""
Description: Defines a function to calculate factorial of a number using
iterative approach (chosen for better performance with large numbers).

Inputs:
- n (int)

Outputs:
- "n:" <n>
- "Factorial:" <factorial_value>

Validations:
- n is integer
- n >= 0
- n <= 20 (to prevent extremely large numbers)
- Otherwise show "Error: invalid input"

Test cases:
1) Normal: n = 5 → Factorial: 120
2) Border: n = 0 → Factorial: 1
3) Error: n = -5 → "Error: invalid input"
"""

def factorial(n):
    """Calculate factorial of n using iterative approach."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def problemsix():
    print("\n PROBLEM 6: Factorial function")
    
    try:
        n = int(input("Enter n (0-20): "))
    except ValueError:
        print("Error: invalid input")
        return
    
    if n < 0 or n > 20:
        print("Error: invalid input")
        return
    
    result = factorial(n)
    print(f"n: {n}")
    print(f"Factorial: {result}")

# RESULTADOS

problemone()
problemtwo()
problemthree()
problemfour()
problemfive()
problemsix()


# CONCLUSIONES
"""
Las funciones son fundamentales para organizar y reutilizar código, ya que encapsulan
tareas específicas en unidades modulares. Esto reduce la duplicación de código y hace
 que los programas sean más fáciles de mantener y depurar.

Devolver valores con sentencias return ofrece mayor flexibilidad que imprimir
directamente, ya que los valores retornados pueden usarse en cálculos posteriores,
almacenarse en variables o pasarse a otras funciones.

Los parámetros y valores por defecto hacen que las funciones sean más adaptables a
diferentes casos de uso sin requerir múltiples definiciones de funciones. Esta 
flexibilidad fue particularmente evidente en la función de saludo con parámetro de título opcional.

Encapsular lógica en funciones resultó más beneficioso para cálculos repetitivos
(como estadísticas y descuentos) y lógica de validación compleja. Esta separación
hizo que el código principal fuera más limpio y legible.

La distinción entre lógica principal y funciones auxiliares quedó clara: la
lógica principal maneja el flujo del programa y E/S, mientras que las funciones
auxiliares se centran en tareas computacionales específicas. Esta separación
de responsabilidades mejora la organización del código y la capacidad de prueba.

El uso de funciones puras (sin efectos secundarios) como en el problema de descuentos 
facilita el razonamiento sobre el código y previene errores relacionados
con modificaciones inesperadas de estado.
"""

# REFERENCIAS
"""
1) Python - Defining Functions: 
   URL: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
2) Real Python - Python Functions: The Ultimate Guide:
   URL: https://realpython.com/defining-your-own-python-function/
3) GeeksforGeeks - Functions in Python:
   URL: https://www.geeksforgeeks.org/functions-in-python/ 
4) PEP 8 -- Style Guide for Python Code:
   URL: https://www.python.org/dev/peps/pep-0008/#function-names
5) Stack Overflow - What is a pure function?:
   URL: https://stackoverflow.com/questions/4728073/what-is-a-pure-function
"""

# REPOSITORIO DE GITHUB
"""
    URL: https://github.com/FelipePinzonS/Manejo_De_Funciones_En_Python.git
"""