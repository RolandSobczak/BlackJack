"""This module tests game module"""
from game import Game


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