⛅ Aplicativo de Clima com Python e Streamlit

Este é um projeto simples que consome a API do OpenWeather para exibir a temperatura e a sensação térmica de uma cidade digitada pelo usuário. O aplicativo foi desenvolvido em Python utilizando o Streamlit para criar uma interface interativa.

🌟 Funcionalidades

Busca a temperatura e a sensação térmica de qualquer cidade.

Exibe um ícone correspondente à condição climática.

Interface simples e interativa com Streamlit.

Tratamento de erros para casos como "cidade não encontrada" ou falha na requisição.

🔧 Tecnologias Utilizadas

Python

Streamlit (para a interface)

Requests (para consumir a API)

API OpenWeather

🛠️ Como Executar o Projeto

1. Clone o repositório

    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio

2. Crie um ambiente virtual e ative

    python -m venv venv  # Criando o ambiente virtual
    # No Windows:
    venv\Scripts\activate
    # No Linux/Mac:
    source venv/bin/activate

3. Instale as dependências

    pip install -r requirements.txt

4. Crie um arquivo .env para armazenar sua chave de API

Crie um arquivo .env na raiz do projeto e adicione sua chave da API OpenWeather:

API_KEY=coloque_sua_chave_aqui

5. Execute a aplicação

    streamlit run app.py

🌍 Como Funciona?

O usuário digita o nome da cidade desejada.

A aplicação faz uma requisição à API do OpenWeather.

Os dados são tratados e exibidos na tela.

Se houver erro (exemplo: cidade inexistente), uma mensagem apropriada é mostrada.

📖 O que Aprendi com Este Projeto?

Consumo de APIs em Python usando a biblioteca requests.

Manipulação de JSON para extrair e tratar informações da API.

Criação de uma interface interativa com Streamlit.

Tratamento de erros para tornar a aplicação mais robusta.

Uso do .gitignore para esconder credenciais sensíveis.

Versionamento de código com Git e GitHub.

👨‍💻 Autor

Túlio Sarto

Sinta-se à vontade para contribuir ou entrar em contato! 🚀

