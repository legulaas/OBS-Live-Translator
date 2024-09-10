# **OCR e Tradução com OBS**

Este projeto é uma aplicação em Python que utiliza OCR (Reconhecimento Óptico de Caracteres) e tradução automática para sobrepor traduções em vídeos em tempo real, integrando com o OBS Studio.]
A aplicação captura frames de um vídeo, processa o texto encontrado e adiciona a tradução diretamente sobre a imagem no OBS.

Observações: A aplicação ainda não é capaz de identificar e traduzir em tempo real. O tempo de processamento está muito alto, e depende muito do hardware em que a aplicação está rodando. 
Caso tenha sugestões de otimização para a aplicação, faça um fork e também envie um pull request.

## **Índice**

- [Instalação](#instalação)
- [Uso](#uso)
- [Arquitetura](#arquitetura)
- [Dependências](#dependências)
- [Contribuição](#contribuição)
- [Licença](#licença)

## **Instalação**

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seu_usuario/seu_repositorio.git
    ```

2. **Instale as dependências:**

    Crie um ambiente virtual e instale as bibliotecas necessárias:

    ```bash
    cd seu_repositorio
    python -m venv venv
    source venv/bin/activate  # Para Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

    Certifique-se de que o OBS Studio está instalado e configurado para aceitar conexões WebSocket.

## **Uso**

1. **Configure o OBS Studio:**
    - Certifique-se de que o plugin OBS WebSocket está instalado e ativo.
    - Ajuste o host, porta e senha no código para corresponder às configurações do OBS.
    - Crie uma fonte de IMAGEM e selecione uma imagem chamada "overlay.png" na raiz do diretório (Mesmo que ela ainda não exista, pois essa será a imagem atualizada com todas as traduções e que será aplicada).
    - Nas variáveis width e height no arquivo main.py, coloque a sua resolução de gravação do OBS.

2. **Execute o script:**

    ```bash
    python seu_script.py
    ```

3. **Controle com o teclado:**
    - **Scroll Lock:** Inicia a captura e processamento do frame atual.
    - **Pause:** Limpa os frames capturados e a sobreposição.
    - **F12:** Encerra o programa.

## **Arquitetura**

- **WebSocket OBS:** Conecta e controla o OBS Studio. (Algumas funções de inicio de stream estão configuradas mas ainda não utilizadas, use como quiser)
- **Captura de Frames:** Salva o primeiro frame do vídeo capturado.
- **OCR e Tradução:** Utiliza OCR para extrair texto e traduz para o idioma desejado.
- **Sobreposição:** Adiciona o texto traduzido sobre a imagem original.
- **Logs:** Registra eventos e erros para monitoramento e depuração.

## **Dependências**
- `easyocr`
- `deep_translator`
- `obs-websocket-py`
- `pandas`
- `opencv-python`
- `Pillow`
- `pynput`
- `glob`
- `app.ocr` (módulo personalizado para OCR)
- `app.translation` (módulo personalizado para tradução)
- `app.overlay` (módulo personalizado para sobreposição)
- `app.log` (módulo personalizado para logs)
- `app.obs` (módulo personalizado para integração com OBS)

Para instalar as dependências, use:

```bash
pip install -r requirements.txt
