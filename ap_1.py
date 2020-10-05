"""Jogo da memoria
    Grupo 1 - Pedro Rocha, Beatriz Ferreira, Gustavo Santos
"""
import random
import time
import pygame
from pygame import display

# Constantes de Configuração do jogo
DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 800

CLOCK = pygame.time.Clock()

COLORS = {
    "black":(0, 0, 0),
    "white":(255, 255, 255),
    "red": (255, 0, 0),
    "blue": (0, 0, 153),
    "babyblue": (51, 204, 255)
}

BORDER_MARGIN = 1
BORDER_THICKNESS = 3

CARD_MARGIN_WIDTH = 5
CARD_MARGIN_HEIGHT = 5

CARD_WIDTH = 131.25
CARD_HEIGTH = 148

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
    pos_mouse = list(pygame.mouse.get_pos())

    for indice in range(20):
        if is_inside_card(baralho, pos_mouse):
            if baralho[indice]["virada"]:
                baralho[indice]["virada"] = True
                cartas_viradas = baralho[indice]

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
        int(coluna * CARD_HEIGTH + (coluna - 1) * CARD_HEIGTH),
        int(CARD_WIDTH),
        int(CARD_HEIGTH) 
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
    COLUNA = coluna * CARD_HEIGTH + (coluna - 1) * CARD_HEIGTH

    rect = pygame.Rect(int(linha * CARD_WIDTH + (linha - 1) * CARD_WIDTH), \
            int(coluna * CARD_HEIGTH + (coluna - 1) * CARD_HEIGTH), \
            CARD_WIDTH, \
            CARD_HEIGTH 
    )

    pygame.draw.rect(
        display,
        COLORS.get("babyblue"),
        rect
    )
    font = pygame.font.SysFont(None, 50)
    #ponto central carta = 75 largura x 92.5 altura
    text = font.render(str(valor), True, COLORS.get("black"))
    display.blit(text, (int(LINHA + (CARD_WIDTH / 2 )),int(COLUNA + (CARD_HEIGTH / 2))))

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
    pos_x = coluna * CARD_MARGIN_WIDTH + (coluna - 1) * int(CARD_WIDTH)
    pos.append(pos_x)
    pos_x_final = pos_x + CARD_WIDTH
    pos.append(pos_x_final)
    pos_y = linha * CARD_MARGIN_HEIGHT + (linha - 1) * CARD_HEIGTH
    pos.append(pos_y)
    pos_y_final = pos_y + CARD_HEIGTH
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
        if indice in range(0, 5):
            linha = 1
            if coluna == 0:
                coluna = 4
                baralho[indice]["posicao"] = pos_card(coluna, linha)
            baralho[indice]["posicao"] = pos_card(coluna, linha)
        elif indice in range(5, 9):
            linha = 2
            if coluna == 0:
                coluna = 4
                baralho[indice]["posicao"] = pos_card(coluna, linha)
            baralho[indice]["posicao"] = pos_card(coluna, linha)
        elif indice in (9, 13):
            linha = 3
            if coluna == 0:
                coluna = 4
                baralho[indice]["posicao"] = pos_card(coluna, linha)
            baralho[indice]["posicao"] = pos_card(coluna, linha)
        elif indice in (13, 17):
            linha = 4
            if coluna == 0:
                coluna = 4
                baralho[indice]["posicao"] = pos_card(coluna, linha)
            baralho[indice]["posicao"] = pos_card(coluna, linha)
        else:
            linha = 5
            if coluna == 0:
                coluna = 4
                baralho[indice]["posicao"] = pos_card(coluna, linha)
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
        if indice in range(0, 5):
            linha = 1
            if baralho[indice]["virada"] == True:
                draw_carta_up(valor, display, baralho, coluna, linha)
            else:
                draw_carta_down(display, baralho, coluna, linha)
        elif indice in range(5, 9):
            linha = 2
            if baralho[indice]["virada"] == True:
                draw_carta_up(valor, display, baralho, coluna, linha)
            else:
                draw_carta_down(display, baralho, coluna, linha)
        elif indice in (9, 13):
            linha = 3
            if baralho[indice]["virada"] == True:
                draw_carta_up(valor, display, baralho, coluna, linha)
            else:
                draw_carta_down(display, baralho, coluna, linha)
        elif indice in (13, 17):
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
