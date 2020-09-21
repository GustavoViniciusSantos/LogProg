"""Jogo da memoria
    Grupo 1 - Pedro Rocha, Beatriz Ferreira, Gustavo Santos
"""
import random
import pygame


# Constantes de Configuração do jogo
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 1200

CLOCK = pygame.time.Clock()

COLORS = {
    "black":(0, 0, 0),
    "white":(255, 255, 255),
    "red": (255, 0, 0)
}

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

def in_range(value, inf_limit, sup_limit):
    """Confere se um determinado valor está presente em um intervalo de dois inteiros.

    Args:
        inf_limit (int): valor inferior do intervalo
        sup_limit (int): valor superior do intervalo
    """
    valores_possiveis = range(inf_limit, sup_limit + 1)
    if value in valores_possiveis:
        return True
    return False

def is_inside_card(baralho, pos_mouse):
    """Verifica se o clique foi dentro da carta

    Args:
        baralho (dict): dicionário contendo todas as cartas
        pos_mouse (list): lista em que o primeiro elemento é a pos_x \
        e o segundo elemento é a pos_y.
    """
    for carta in baralho:
        if in_range(pos_mouse[0], carta["posicao"][0], carta["posicao"][1])\
            and in_range(pos_mouse[1], carta["posicao"][2], carta["posicao"][3]):
            return True
    return False

def card_selected(baralho, pos_mouse):
    """Retorna a carta escolhida

    Args:
        baralho (dict): dicionário contendo todas as cartas
        pos_mouse ([type]): lista em que o primeiro elemento é a pos_x \
        e o segundo elemento é a pos_y.
    """
    for carta in baralho:
        if in_range(pos_mouse[0], carta["posicao"][0], carta["posicao"][1])\
            and in_range(pos_mouse[1], carta["posicao"][2], carta["posicao"][3]):
            return baralho[carta]

def treat_mouse_click(baralho, cartas_viradas):
    """Trata o click do mouse.
    """
    pos_mouse = list(pygame.mouse.get_pos())

    for carta in baralho:
        if is_inside_card(baralho, pos_mouse):
            if not carta["virada"]:
                carta["virada"] = True
                cartas_viradas.append(card_selected(baralho, pos_mouse))

def treat_events(baralho, cartas_viradas):
    """Trata os eventos ocorridos entre cada quadro.
    """
    if not pygame.MOUSEBUTTONUP:
        return False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if pygame.mouse.get_pressed():
            treat_mouse_click(baralho, cartas_viradas)
    return False

def create_cards(valor):
    """Cria as cartas

    Args:
        valor (int): Valor para a carta, sendo um numero de 0 a 9.

    Returns:
        [dict]: Retorna um dicionario representado a carta, na forma:
        {
            "valor": número de 0 a 9,
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
    baralho = create_objects()
    cartas_viradas = []

    while True:
        if treat_events(baralho, cartas_viradas) == True:
            break
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
