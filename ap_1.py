"""Jogo da memoria
    Grupo 1 - Pedro Rocha, Beatriz Ferreira, Gustavo Santos
"""
import random
import pygame
import time

# Constantes de Configuração do jogo
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 1200

CLOCK =  pygame.time.Clock()

def start_game():
    """Inicializa o jogo
    """
    pygame.init()
    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Jogo da memoria!")

    return display

def end_game():
    """Finaliza o jogo.
    """
    print("Saindo do jogo!!!")
    pygame.quit()

def set_frame_rate(fps):
    """Define a velocidade de execução do jogo.

    Args:
        fps (int): Define o fps do jogo
    """
    CLOCK.tick(fps)

def treat_events():
    """Trata os eventos ocorridos entre cada quadro.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    
    return False


def create_cards(valor):
    """Cria as cartas

    Args:
        valor (int): Valor para a carta, sendo um numero de 0 a 9.

    Returns:
        [dict]: Retorna um dicionario representado a carta, na forma:
        {
            "valor": 0,
            "virada: Valor booleano, para representar se a carta esta virada ou nao.
            False -> baixo, True-> cima
            "imagem_baixo": A imagem da carta virada para baixo
            "imagem_cima": A imagem da carta virada para cima
            "posicao": posicao da imagem no display
        }
    """
    carta = {
        "valor": valor,
        "virada": False, # False para carta virada, True para carta mostrando o número.
        "imagem_baixo": 0,
        "imagem_cima":0,
        "posicao": 0
    }
    return carta

def create_objects():
    """Cria os objetos do jogo
    """
    baralho = {}
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] * 2
    

    random.shuffle(numeros)

    for indice in range(20):
        carta = create_cards(numeros[indice])
        baralho[indice] = carta

    return baralho


def run_loop(display):
    """Roda o loop do jogo

    Args:
        display (pygame.surface): [display do jogo]
    """
    objects = create_objects()
    cartas_viradas = []

    while True:

        set_frame_rate(60)

def main():
    """Ponto de entrada do jogo
    """
    # Inicializar o jogo
    display = start_game()
    # Rodar o jogo
    run_loop(display)
    # Encerrar o jogo


if __name__ == "__main__":
    main()
