import random
import string
import requests

class Tools:
    @staticmethod
    def add_two_numbers(a: int, b: int) -> int:
        """
        Suma dos números.
        """
        return a + b

    @staticmethod
    def generate_random_number(min_value: int, max_value: int) -> int:
        """
        Genera un número aleatorio dentro de un rango dado.
        """
        return random.randint(min_value, max_value)

    @staticmethod
    def random_quote() -> str:
        """
        Devuelve una cita aleatoria.
        """
        quotes = [
            "La vida es lo que pasa mientras estás ocupado haciendo otros planes. - John Lennon",
            "El único modo de hacer un gran trabajo es amar lo que haces. - Steve Jobs",
            "El futuro pertenece a quienes creen en la belleza de sus sueños. - Eleanor Roosevelt",
            "La felicidad no es algo hecho. Viene de tus propias acciones. - Dalai Lama"
        ]
        return random.choice(quotes)

    @staticmethod
    def word_count(text: str) -> int:
        """
        Cuenta el número de palabras en un texto.
        """
        return len(text.split())

    @staticmethod
    def convert_temperature(value: float, unit_from: str, unit_to: str) -> float:
        """
        Convierte una temperatura de una unidad a otra.
        """
        if unit_from == "C":
            if unit_to == "F":
                return value * 9/5 + 32
            elif unit_to == "K":
                return value + 273.15
        elif unit_from == "F":
            if unit_to == "C":
                return (value - 32) * 5/9
            elif unit_to == "K":
                return (value - 32) * 5/9 + 273.15
        elif unit_from == "K":
            if unit_to == "C":
                return value - 273.15
            elif unit_to == "F":
                return (value - 273.15) * 9/5 + 32
        return value

    @staticmethod
    def generate_password(length: int) -> str:
        """
        Genera una contraseña aleatoria.
        """
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    @staticmethod
    def generate_anagram(word: str) -> str:
        """
        Genera un anagrama aleatorio de una palabra.
        """
        word_list = list(word)
        random.shuffle(word_list)
        return ''.join(word_list)

    @staticmethod
    def calculate_factorial(number: int) -> int:
        """
        Calcula el factorial de un número.
        """
        if number == 0:
            return 1
        return number * Tools.calculate_factorial(number - 1)
    
    @staticmethod
    def generate_fibonacci(n: int) -> list:
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        """
        fibonacci_sequence = [0, 1]
        for i in range(2, n):
            fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
        return fibonacci_sequence
    
    @staticmethod
    def calculate_sum_of_squares(numbers: list) -> float:
        """
        Calcula la suma de los cuadrados de una lista de números.
        """
        return sum([number ** 2 for number in numbers])
    
    @staticmethod
    def make_request(method: str, url: str, params: dict = None, data: dict = None) -> str:
        """
        Realiza una solicitud HTTP usando el método especificado.
        
        Args:
            method (str): El método HTTP (GET, POST, etc.)
            url (str): La URL a la que hacer la solicitud.
            params (dict, opcional): Parámetros de la consulta (para GET).
            data (dict, opcional): Datos a enviar (para POST).
        
        Returns:
            str: El cuerpo de la respuesta en formato de texto.
        """
        try:
            # Realizar la solicitud según el método especificado
            response = requests.request(method, url, params=params, data=data)
            
            # Comprobar si la solicitud fue exitosa
            if response.status_code == 200:
                return response.text
            else:
                return f"Error: {response.status_code} - {response.text}"
        except requests.exceptions.RequestException as e:
            return f"Error en la solicitud: {e}"