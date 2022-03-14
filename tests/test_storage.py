"""This module tests storage module
"""
from ..core.storage import Card, Deck


def test_card_gen():
    """Checks card generator
    """
    cards = set(Deck().card_gen())
    assert len(cards) == 52


def test_card_str():
    """Checks str method of Card class
    """
    verb = str(Card('Clubs', 1))
    assert verb == 'c: Clubs s: Ace'
    verb = str(Card('Clubs', 2))
    assert verb == 'c: Clubs s: 2'


def test_card_eq():
    """Checks eq method of Card class
    """
    card1 = Card('Clubs', 1)
    card2 = Card('Clubs', 1)
    assert card1 == card2
    card2 = Card('Clubs', 2)
    assert card1 != card2

def test_deck():
    """Checks add_cards method of Deck class
    """
    deck = Deck()
    deck.add_cards(*list(deck.card_gen()))
    assert len(deck.cards) == 52


def test_deck_setup():
    """Ckecks setup deck method of Deck class
    """
    deck = Deck()
    deck.setup()
    assert len(deck.cards) == 52


def test_deck_add_cards():
    """Checks add_cards method of Deck class
    """
    deck = Deck()
    card = Card('Clubs', 1)
    deck.add_cards(card)
    assert  card in deck.cards


def test_card_hash():
    """Checks hash method of Card class
    """
    card1 = Card('Clubs', 1)
    card2 = Card('Clubs', 1)
    assert hash(card1) == hash(card2)


def test_deck_distribution():
    """Checks distribution method of Deck class
    """
    deck = Deck()
    deck.setup()
    card = deck.card_distribution()
    assert card not in deck.cards
