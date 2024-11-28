# Ollama Conversational Tools Project

This project utilizes the Ollama library to create an interactive chatbot that can perform various tasks using Python functions as tools. The chatbot can maintain a conversation and respond to user queries using mathematical functions, random number generation, quote generation, and more.

## Features

- **Addition Function**: Performs addition of two numbers.
- **HTTP Request**: Fetches the content of a webpage using the `requests` library.

## Requirements

- **Python**: Ensure you have Python installed on your machine.
- **Ollama**: This project requires the Ollama library, which must be running locally. Follow the [official installation guide](https://ollama.com/docs/getting-started) to set it up.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/nicopanozo/ollama-functions-as-tools
   cd ollama-functions-as-tools
2. Install the required Python package:

    ```bash
    pip install -U ollama
3. Ensure Ollama is running locally.

## Usage
1. Make sure you have ollama running locally.

2. Open a terminal and navigate to the project directory.

3. Run the main script (you may need to adjust the filename if you saved it differently):

    ```bash
    python main.py
4. Interact with the chatbot by typing your queries, such as:

- "What is 10 + 20?"
- "Busca la página principal de Ollama"

## Structure
- main.py: The main script that handles user interaction and processes tool calls.
- tools.py: Contains the function definitions for all the tools available in the chatbot.
- requirements.txt: Lists the required Python packages for the project.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing
Contributions are welcome! If you have suggestions or improvements, please feel free to fork the repository and submit a pull request.

## Acknowledgments
Thanks to the Ollama team for providing an excellent platform for building conversational agents.
shell