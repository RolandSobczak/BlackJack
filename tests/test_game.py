"""This module tests game module"""
from game import Game
from pytest import raises
from core.exceptions import UserWins, CrupierWins, Draw
from core.storage import Card


def test_user_passed():
    """Checks if user passed after user_passed method is called"""
    game = Game()
    game.user_passed()
    assert game.user.passed


def test_hit():
    """Checks if user takes one more card after hit method is called"""
    game = Game()
    game.hit()
    assert len(game.user.cards) == 1


def test_croupier_hit():
    """Checks if croupier plays until haves bigger score than user"""
    with raises(UserWins) as message:
        game = Game()
        game._setup()
        game.user.score = 22
        game._croupier_turn()
        assert message != 'You wins'

def test_user_hit():
    """Checks if CrupierWins exception is called when user exceed 21 points"""
    with raises(CrupierWins) as message:
        game = Game()
        game.user.add_cards(Card('Clubs', 1), Card('Clubs', 1))
        game.hit()
        assert message != 'You lose!'

def test_check_result():
    """Checks if correct Exceptions are called when result is Draw or Lose"""
    with raises(Draw) as message:
        game = Game()
        game.user.add_cards(Card('Clubs', 1), Card('Clubs', 1))
        game.croupier.add_cards(Card('Clubs', 1), Card('Clubs', 1))
        game._check_result()
        assert message != 'Draw'

    with raises(CrupierWins) as message:
        game = Game()
        game.user.add_cards(Card('Clubs', 1), Card('Clubs', 2))
        game.croupier.add_cards(Card('Clubs', 1), Card('Clubs', 1))
        game._check_result()
        assert message != 'You lose!'

def test_setup():
    """Checks if user and croupier haves 2 cards after setup"""
    game = Game()
    game._setup()
    assert len(game.user.cards) == 2
    assert len(game.croupier.cards) == 2
    assert set(game.user.cards) != set(game.croupier.cards)
