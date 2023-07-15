# MagicPianoBot

Neste projeto, nós vamos automatizar a jogabilidade do Magic Piano. Este site disponibiliza um jogo onde ouve uma música e clica nas teclas de teclado na tela.

#### OBSERVAÇÃO: ESTE PROJETO SÓ FUNCIONA EM SISTEMAS WINDOWS. 
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

Muito importante! **NÃO** CRIE AMBIENTE VIRTUAIS PARA RODAR ESTE PROJETO! 

Para este projeto, vamos utilizar a biblioteca **pywin32** que contém um api para interação com sistema Windows. Por isso, se você criar um ambiente virtual e baixar as bibliotecas ali, a biblioteca  **pywin32** não vai conseguir acessar os recursos do Windows.

### Siga os seguintes passos:

1. Certifique-se que você selecionou a opção **Add to path** quando instalou o Python 3.

2. Estando dentro da pasta do projeto, abra o seu terminal.

Feito isso, vamos instalar as bibliotecas necessárias através do arquivo **requirements.txt**.

3. Estando dentro da pasta do projeto, rode:
```
pip install -r requirements.txt
```
Pronto! Você está apto para rodar o projeto.

***
## Possíveis problemas:


Primeiramente, entenda que a biblioteca **PyAutoGUI** foi criada para automatizações que dependem do tamanho da sua tela. Em outras palavras, se você utilizar uma tela de tamanho diferente do computador em que a aplicação foi testada, é muito provável que a aplicação quebre. No meu caso, eu dividi a tela no meio, com o editor de texto à esquerda e o navegador, à direita, então, você deve fazer o mesmo no seu computador para que a automação funcione.

Caso você tenha este tipo de problema, olhe código do fonte do programa - app.py. Os comandos que dependem do tamanho da sua tela recebem um comentário na sua linha de cima escrito: Depende do tamanho da sua tela.

 Além disso, é possível que o seu navegador padrão não mostre claramente algum item que foi localizado via imagem(print). Se isso acontecer, tente alterar o tamanho da janela do navegador ou tire outros prints e salve-os sobrescrevendo a imagem correspondente na pasta images.
