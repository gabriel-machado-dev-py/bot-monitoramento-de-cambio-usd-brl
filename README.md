# Bot Monitorador de câmbio USD -> BRL

```
O bot é capaz de pegar a cotação atual do dolar para o real de maneira rápida e efeciente sem precisar abrir o navegador
```

## Sobre o projeto

Este projeto foi desenvolvidado para pegar a cotação atual do dolar(USD) -> real(BRL) afim de informar ao usuário o seu valor na data presente, e
com os dados, criando um arquivo Word(docx) e em seguida transformando-o para um arquivo PDF

## Estrutura das pastas

- **app.py** # Código-fonte principal da aplicação
- **requirements.txt** # Todas as tecnologias utilizadas no projeto
- **setup.py** # código que transforma o arquivo `app.py` em executável
- **app.log** # Informa os acontecimentos no programa, como: passo a passo da aplicação e também erros que podem ocorrer.

## Tecnologias utilizadas

- **Python**: Linguagem de programação principal.
- **Selenium**: Utilizado para automação de navegação web e extração de dados.
- **python-docx**: Biblioteca para criação e manipulação de documentos Word.
- **docx2pdf**: Biblioteca para conversão de documentos Word para PDF.
- **FPDF**: Biblioteca para geração de PDFs.

## Pré-requisitos

- Python 3.x instalado
- Google Chrome instalado
- ChromeDriver compatível com a versão do Chrome instalada

## Funcionalidades

- **Extração dos dados da cotação**: O bot acessa um site de finanças e extrai a cotação atual do dólar.
- **Criação de um arquivo Word**: Com os dados extraídos, o bot gera um documento Word formatado.
- **Conversão para PDF**: O documento Word é convertido em um arquivo PDF.

## Como rodar localmente

Clone este repositório

```
git clone https://github.com/gabriel-machado-dev-py/bot-monitoramento-de-cambio-usd-brl.git
```

Instale as dependências

```
pip install -r requirements.txt
```

Iniciando a aplicação

````
python/python3(mac/linux) app.py
````

Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Projeto Link: https://github.com/gabriel-machado-dev-py/bot-monitoramento-de-cambio-usd-brl

```

```
