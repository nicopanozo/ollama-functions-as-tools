import ollama
import requests
from tools import Tools

class OllamaInteraction:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.conversation_history = []
        self.available_functions = {
            'add_two_numbers': Tools.add_two_numbers,
            'request': requests.request
        }

    def interact_with_model(self, user_input: str):
        # Añadir el mensaje del usuario al historial
        self.conversation_history.append({'role': 'user', 'content': user_input})

        # Hacer la consulta al modelo
        response = ollama.chat(
            model=self.model_name,
            messages=self.conversation_history,
            tools=list(self.available_functions.values())  # Herramientas disponibles
        )

        # Procesar las llamadas a las herramientas
        for tool in response.message.tool_calls or []:
            function_to_call = self.available_functions.get(tool.function.name)
            if function_to_call:
                # Verificamos si la función es 'request' y la manejamos correctamente
                if tool.function.name == 'request':
                    # Extraemos los argumentos de la herramienta 'request'
                    arguments = tool.function.arguments
                    result = requests.request(
                        method=arguments['method'],
                        url=arguments['url'],
                        params=arguments.get('params'),
                        data=arguments.get('data')
                    )
                    print(f"Resultado de la solicitud: {result.text}")
                else:
                    result = function_to_call(**tool.function.arguments)
                    print(f"Resultado de {tool.function.name}: {result}")
            else:
                print(f"Función no encontrada: {tool.function.name}")

        # Agregar la respuesta del modelo al historial
        self.conversation_history.append({'role': 'assistant', 'content': response.message.content})

# Crear la interacción con el modelo
ollama_interaction = OllamaInteraction(model_name='llama3.2:3b')

# Ejemplo de interacción
ollama_interaction.interact_with_model('¿Cuál es 10 + 20?')
ollama_interaction.interact_with_model('Busca la página principal de Ollama')
