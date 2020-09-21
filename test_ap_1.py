"""Arquivo para realizarmos os testes.
"""
import pytest
import ap_1

def test_create_cards():
    carta = {
        "valor": 10,
        "virada": False, # False para carta virada, True para carta mostrando o número.
        "imagem_baixo": 0,
        "imagem_cima":0,
        "posicao": 0
    }
    assert carta == ap_1.create_cards(10)