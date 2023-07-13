import pyautogui as pg
import webbrowser
from time import sleep
import win32api, win32con
import keyboard

def click(x, y):
    """
    Utiliza o seu mouse para dar um clique na tela.

    Esta função aceita apenas 2 argumentos: x: coordenada x da tela. y: coordenada y da tela.
    """
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


pg.alert(text='O programa será iniciado. Quando quiser parar a execução, clique na tecla "space"', title='Informação:', button='Ok?')

def localizar_ponto(x, y):
    """
    Localiza a posição da sua tela através da coordenadas x e y da mesma.

    Esta função aceita apenas 2 argumentos: x: coordenada x da tela. y: coordenada y da tela.
    """
    ponto = pg.pixelMatchesColor(x, y, (0,0,0))
    if ponto:
        click(x, y)


# Depende do tamanho da sua tela.
pontos_verificados = [
    (1136,250), (1054,250), (973,250), (887,250)]

webbrowser.open('https://sandbox.gameforge.com/en-US/littlegames/magic-piano-tiles/')
sleep(8)

# Depende do tamanho da sua tela.
pg.click(1015,489, duration=1.5)
sleep(5)

# Depende do tamanho da sua tela.
iniciar = pg.locateCenterOnScreen('./images/start.png')
# Depende do tamanho da sua tela.
pg.click(iniciar[0], iniciar[1], duration=1.5)
sleep(3)


while not keyboard.is_pressed('space'):
    for ponto in pontos_verificados:
        localizar_ponto(ponto[0], ponto[1])

pg.alert(text='Você interrompeu o funcionamento da aplicação!', title='Encerramento de execução:', button='Ok?')