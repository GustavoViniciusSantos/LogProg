"""Arquivo para realizarmos os testes.
"""
import pytest
import ap_1
import pygame

CLOCK = pygame.time.Clock()

IN_RANGE_PARAMS = [[5, 2, 10, True], [4, 5, 10, False]]
BARALHO_PARAMS = {
    1: {"valor": 10,
        "virada": False,
        "imagem_baixo": 0,
        "imagem_cima":0,
        "posicao": 0},

    2: {"valor": 9,
        "virada": False,
        "imagem_baixo": 0,
        "imagem_cima":0,
        "posicao": 0}
}

@pytest.mark.parametrize("value, inf_limit, sup_limit, capsys", IN_RANGE_PARAMS)
def test_in_range(value, inf_limit, sup_limit, capsys):
    retorno = ap_1.in_range(value, inf_limit, sup_limit)
    out = capsys
    assert out == retorno


@pytest.mark.parametrize()
def test_is_inside_card():

def test_create_cards():
    carta = {
        "valor": 10,
        "virada": False, # False para carta virada, True para carta mostrando o número.
        "imagem_baixo": 0,
        "imagem_cima":0,
        "posicao": 0
    }
    assert carta == ap_1.create_cards(10)