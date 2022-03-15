"""This module tests players module
"""
from core.players import User, Croupier
from core.storage import Card


def test_add_cards():
    """Checks add_cards of Player class
    """
    user = User()
    card = Card('Clubs', 1)
    user.add_cards(card)
    assert len(user.cards) == 1
    assert card in user.cards


def test_score_calculate():
    """Checks the score_calculate method of the Player class in a few cases
    """
    user = User()
    card = Card('Clubs', 1)
    user.add_cards(card, card)
    assert user.score == 21
    user = User()
    user.add_cards(Card('Clubs', 1), Card('Clubs', 11))
    assert user.score == 21
    user = User()
    user.add_cards(Card('Clubs', 1), Card('Clubs', 7), Card('Clubs', 2))
    assert user.score == 20
    user = User()
    user.add_cards(Card('Clubs', 2), Card('Clubs', 7), Card('Clubs', 1))
    assert user.score == 10


def test_game_init():
    """Checks game init method of the Croupier class
    """
    croupier = Croupier()
    cards = croupier.game_init()
    assert len(croupier.cards) == 2
    assert len(cards) == 2
    assert set(cards) != set(croupier.cards)
