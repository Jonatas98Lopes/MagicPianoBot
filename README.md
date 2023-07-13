# MagicPianoBot

Neste projeto, nós vamos automatizar a jogabilidade do Magic Piano. Este site disponibiliza um jogo onde ouve uma música e clica nas teclas de teclado na tela.

***

## Vídeo de apresentação do projeto e primeiros passos:

Assista ao vídeo de funcionamento do projeto [clicando aqui!](https://www.linkedin.com/feed/update/urn:li:activity:7085377563530862592/).
***
## Descrição das instruções:

1. Obter as coordenadas da tela onde vamos clicar.

2. Acessar o site do jogo [Magic Piano](https://sandbox.gameforge.com/en-US/littlegames/magic-piano-tiles/)

3. Localizar o botão "Play" e clicar nele.

4. Localizar e clicar no botão "Start".

REPETIR O PROCESSO ATÉ QUE O USUÁRIO A BARRA DE ESPAÇO NO TECLADO.

  5. Verifica cada coordenada da tela informada. 

  SE A DETERMINADA POSIÇÃO DA TELA ESTIVER PRETA:
    
    6. Clicar na tela.

***

## Como rodar o código? 

Assim que clonar este código, sugiro que você crie um ambiente virtual isolando os arquivos que estão no seu computador do diretório do projeto.

### Criando ambiente virtual com Python:
1. Certifique-se que você selecionou a opção Add to path quando instalou o Python 3.

2. Estando dentro da pasta do projeto, abra o seu terminal:

3. Caso esteja no Windows, rode o comando abaixo e aguarde a criação:
```
python -m venv nome_do_ambiente_virtual
```
**nome_do_ambiente_virtual**: Defina o nome do seu ambiente virtual.

4. Caso esteja no Linux ou Mac, rode o comando abaixo e aguarde a criação:
```
python3 -m venv nome_do_ambiente_virtual
```
**nome_do_ambiente_virtual**: Defina o nome do seu ambiente virtual.

5. Ative o ambiente virtual através do seu terminal:
No caso do Windows, rode:
```
nome_do_ambiente_virtual\Scripts\activate
```
**nome_do_ambiente_virtual**: Coloque o nome que definiu na criação do ambiente virtual.

No caso do Linux ou Mac, rode:
```
source nome_do_ambiente_virtual\bin\activate
```
**nome_do_ambiente_virtual**: Coloque o nome que definiu na criação do ambiente virtual.

Feito isso, vamos instalar as bibliotecas necessárias através do arquivo **requirements.txt**:
No Windows, estando dentro da pasta do projeto e com o ambiente virtual ativado, rode:
```
pip install -r requirements.txt
```
No Linux ou MAC, estando dentro da pasta do projeto e com o ambiente virtual ativado, rode:
```
pip3 install -r requirements.txt
```
Pronto! Você está apto para rodar o projeto.

***
## Possíveis problemas:


Primeiramente, entenda que a biblioteca **PyAutoGUI** foi criada para automatizações que dependem do tamanho da sua tela. Em outras palavras, se você utilizar uma tela de tamanho diferente do computador em que a aplicação foi testada, é muito provável que a aplicação quebre. No meu caso, eu dividi a tela no meio, com o editor de texto à esquerda e o navegador, à direita, então, você deve fazer o mesmo no seu computador para que a automação funcione.

Caso você tenha este tipo de problema, olhe código do fonte do programa - app.py. Os comandos que dependem do tamanho da sua tela recebem um comentário na sua linha de cima escrito: Depende do tamanho da sua tela.

 Além disso, é possível que o seu navegador padrão não mostre claramente algum item que foi localizado via imagem(print). Se isso acontecer, tente alterar o tamanho da janela do navegador ou tire outros prints e salve-os sobrescrevendo a imagem correspondente na pasta images.