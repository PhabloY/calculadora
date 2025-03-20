# Calculadora em Python com PySide6

Este projeto é uma calculadora desenvolvida em Python utilizando a biblioteca PySide6 para a interface gráfica. O código está organizado em múltiplos arquivos para melhor modularização e manutenção.

## Estrutura do Projeto

- `main.py` - Arquivo principal que inicializa a aplicação.
- `main_window.py` - Configura e exibe a janela principal da calculadora.
- `buttons.py` - Gerencia os botões da interface.
- `display.py` - Controla a exibição dos números e operações digitadas.
- `info.py` - Exibe informações adicionais sobre a calculadora.
- `variables.py` - Contém variáveis globais utilizadas na aplicação.
- `styles.py` - Define os estilos da interface gráfica
- `utils.py`- Contém funções auxiliares para validações e operações gerais.

## Tecnologias Utilizadas

- Python 3+
- PySide6

## Como Instalar e Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd nome-do-repositorio
   ```
3. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Execute a calculadora:
   ```bash
   python main.py
   ```

## Estilização
O design da calculadora é definido no arquivo `styles.py`, permitindo personalização da interface gráfica.

## Funcionalidades
- Operações básicas: soma, subtração, multiplicação e divisão.
- Interface gráfica intuitiva.
- Exibição do histórico de cálculos.

## Licença
Este projeto está licenciado sob a licença MIT. Sinta-se livre para contribuir e melhorar o código! \ud83c\udf89

