"""Jogo da memoria
    Grupo 1 - Pedro Rocha, Beatriz Ferreira, Gustavo Santos
"""
import random
import time
import pygame
from pygame import display

# Constantes de Configuração do jogo
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

CLOCK = pygame.time.Clock()

COLORS = {
    "black":(0, 0, 0),
    "white":(255, 255, 255),
    "red": (255, 0, 0),
    "blue": (0, 0, 153),
    "babyblue": (51, 204, 255)
}

BORDER_MARGIN = 10
BORDER_THICKNESS = 3

CARD_WIDTH = 90
CARD_HEIGHT = 50

CARD_MARGIN_BORDER = 90
CARD_MARGIN_CARD = 50

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
    valores_possiveis = range(int(inf_limit), int(sup_limit + 1))
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
    for indice in range(20):
        if in_range(pos_mouse[0], baralho[indice]["posicao"][0], baralho[indice]["posicao"][1])\
            and in_range(pos_mouse[1], baralho[indice]["posicao"][2], baralho[indice]["posicao"][3]):
            return True
    return False

def card_selected(baralho, pos_mouse):
    """Retorna a carta escolhida
    Args:
        baralho (dict): dicionário contendo todas as cartas
        pos_mouse ([type]): lista em que o primeiro elemento é a pos_x \
        e o segundo elemento é a pos_y.
    """
    for indice in range(20):
        if in_range(pos_mouse[0], baralho[indice]["posicao"][0], baralho[indice]["posicao"][1])\
            and in_range(pos_mouse[1], baralho[indice]["posicao"][2], baralho[indice]["posicao"][3]):
            return baralho[indice]

def treat_mouse_click(baralho, cartas_viradas):
    """Trata o click do mouse.
    """
    pos_mouse = pygame.mouse.get_pos()

    for indice in range(20):
        if is_inside_card(baralho, pos_mouse):
            if baralho[indice]["virada"]:
                baralho[indice]["virada"] = True
                cartas_viradas = baralho[indice]

def treat_events(baralho, cartas_viradas):
    """Trata os eventos ocorridos entre cada quadro.
    """
    if pygame.MOUSEBUTTONUP:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif pygame.mouse.get_pressed():
                print("mouse pressed")
                treat_mouse_click(baralho, cartas_viradas)
        return False

def draw_carta_down(display, baralho, coluna, linha):
    """Desenha a carta virada para baixo

    Args:
        display (pygame.surface): display da tela
        baralho (dict): dicionario contendo as cartas
        coluna (int): coluna em que a carta fica
        linha (int): linha em que a carta fica

    Returns:
        imagem(pygame.surface): imagem da carta virada para baixo
    """
    rect = pygame.Rect(
        int(linha * CARD_WIDTH + (linha - 1) * CARD_WIDTH),
        int(coluna * CARD_HEIGHT + (coluna - 1) * CARD_HEIGHT),
        int(CARD_WIDTH),
        int(CARD_HEIGHT) 
    )
    
    imagem = pygame.draw.rect(
        display,
        COLORS.get("blue"),
        rect
    )

def draw_carta_up(valor, display, baralho, coluna, linha):
    """desenha a carta virada para cima

    Args:
        valor (int): valor da carta indo de 0 a 9
        display (pygame.surface): display da tela
        baralho (dict): dicionario contendo as cartas
        coluna (int): coluna em que a carta fica
        linha (int): linha em que a carta fica

    Returns:
        imagem(pygame.surface): imagem da carta virada para cima
    """
    LINHA = linha * CARD_WIDTH + (linha - 1) * CARD_WIDTH
    COLUNA = coluna * CARD_HEIGHT + (coluna - 1) * CARD_HEIGHT

    rect = pygame.Rect(int(linha * CARD_WIDTH + (linha - 1) * CARD_WIDTH), \
            int(coluna * CARD_HEIGHT + (coluna - 1) * CARD_HEIGHT), \
            CARD_WIDTH, \
            CARD_HEIGHT 
    )

    pygame.draw.rect(
        display,
        COLORS.get("babyblue"),
        rect
    )
    font = pygame.font.SysFont(None, 50)
    #ponto central carta = 75 largura x 92.5 altura
    text = font.render(str(valor), True, COLORS.get("black"))
    display.blit(text, (int(LINHA + (CARD_WIDTH / 2 )),int(COLUNA + (CARD_HEIGHT / 2))))

def draw_borders(display):
    """Desenha a borda do jogo

    Args:
        display (pygame.Surface): display da tela do jogo
    """
    rect = [
        BORDER_MARGIN, BORDER_MARGIN,
        DISPLAY_WIDTH - BORDER_MARGIN*2,
        DISPLAY_HEIGHT - BORDER_MARGIN*2,
    ]
    pygame.draw.rect(
        display,
        COLORS.get("black"),
        rect,
        BORDER_THICKNESS
    )

def pos_card(coluna, linha):
    """Define a posicao da carta no display

    Args:
        coluna (int): coluna em que a carta fica
        linha (int): linha em que a carta fica
    """
    pos = []
    pos_x_inicial = BORDER_MARGIN + CARD_MARGIN_BORDER + \
        coluna * (CARD_WIDTH + CARD_MARGIN_CARD)
    pos.append(pos_x_inicial)
    pos_x_final = pos_x_inicial + CARD_WIDTH
    pos.append(pos_x_final)
    pos_y_inicial = BORDER_MARGIN + CARD_MARGIN_BORDER + \
        linha * (CARD_HEIGHT + CARD_MARGIN_CARD)
    pos.append(pos_y_inicial)
    pos_y_final = pos_y_inicial + CARD_HEIGHT
    pos.append(pos_y_final)
    return pos

def occult_cards(cartas_viradas, baralho):
    """Oculta as cartas se necessario

    Args:
        cartas_viradas (dict): dicionario contendo as cartas viradas
        baralho (dict): dicionario contendo as cartas
    """
    if len(cartas_viradas) == 2:
        valores = []
        for indice in cartas_viradas.keys():
            valores.append(cartas_viradas[indice]["valor"])
        if valores[0] == valores[1]:
            time.sleep(1)
            for indice in cartas_viradas.keys():
                baralho[indice]["virada"] = False
                cartas_viradas = {}

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
    }
    return carta

def create_objects(display):
    """Cria os objetos do jogo

    Args:
        display (pygame.Surface): Display da tela

    Returns:
        dict: dicionario contendo todas as cartas do jogo
    """
    baralho = {}
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] * 2

    random.shuffle(numeros)

    for indice in range(20):
        carta = create_cards(numeros[indice])
        baralho[indice] = carta
        coluna = indice % 4
        if indice in range(0, 4):
            linha = 1
            baralho[indice]["posicao"] = pos_card(coluna, linha)
        elif indice in range(4, 8):
            linha = 2
            baralho[indice]["posicao"] = pos_card(coluna, linha)
        elif indice in range(8, 12):
            linha = 3
            baralho[indice]["posicao"] = pos_card(coluna, linha)
        elif indice in range(12, 16):
            linha = 4
            baralho[indice]["posicao"] = pos_card(coluna, linha)
        else:
            linha = 5
            baralho[indice]["posicao"] = pos_card(coluna, linha)

    return baralho

def render_screen(display, baralho):
    """Renderiza a tela

    Args:
        display (pygame.surface): display da tela
        baralho (dict): dicionario contendo as cartas
    """
    display.fill(COLORS.get("white"))
    draw_borders(display)

    for indice in range(20):
        valor = baralho[indice]["valor"]
        coluna = indice % 4
        if indice in range(0, 4):
            linha = 1
            if baralho[indice]["virada"] == True:
                draw_carta_up(valor, display, baralho, coluna, linha)
            else:
                draw_carta_down(display, baralho, coluna, linha)
        elif indice in range(4, 8):
            linha = 2
            if baralho[indice]["virada"] == True:
                draw_carta_up(valor, display, baralho, coluna, linha)
            else:
                draw_carta_down(display, baralho, coluna, linha)
        elif indice in range(8, 12):
            linha = 3
            if baralho[indice]["virada"] == True:
                draw_carta_up(valor, display, baralho, coluna, linha)
            else:
                draw_carta_down(display, baralho, coluna, linha)
        elif indice in range(12, 16):
            linha = 4
            if baralho[indice]["virada"] == True:
                draw_carta_up(valor, display, baralho, coluna, linha)
            else:
                draw_carta_down(display, baralho, coluna, linha)
        else:
            linha = 5
            if baralho[indice]["virada"] == True:
                draw_carta_up(valor, display, baralho, coluna, linha)
            else:
                draw_carta_down(display, baralho, coluna, linha)

    pygame.display.update()

def run_loop(display):
    """Roda o loop do jogo
    Args:
        display (pygame.surface): [display do jogo]
    """
    baralho = create_objects(display)
    cartas_viradas = {}

    while True:
        occult_cards(cartas_viradas, baralho)
        if treat_events(baralho, cartas_viradas) == True:
            break
        render_screen(display, baralho)
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
