"""This module contains all exceptions in blackjack game
"""


class InvalidInput(Exception):
    """This exception is called when user gives invalid input
    """


class Draw(Exception):
    """This exception is called when user and croupier haves the same score
    """


class Lose(Exception):
    """This exception is called when player exceeds 21 points
    """


class UserWins(Exception):
    """This exception is called when crupier exceeds 21 points
    """


class CrupierWins(Exception):
    """This exception is called when user exceeds 21 points
    """
