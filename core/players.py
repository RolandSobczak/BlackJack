"""This module is responsible for representation players in blackjack

Raises:
    Lose: When player exceeds 21 points
    CrupierWins: When user exceeds 21 points
    UserWins: When croupier exceeds 21 points
"""
from abc import ABC
from .storage import Deck
from .exceptions import Lose, UserWins, CrupierWins


class Player(ABC):
    """This class represents player in game. It's an abstract class
    """
    def __init__(self):
        """This method initialize Player instance
        """
        self.score = 0
        self._cards = []

    def add_cards(self, *args) -> list:
        """This method adds card to player hand

        Raises:
            Lose: When player exceeds 21 points

        Returns:
            list: Cards in players hand
        """
        self._cards += list(args)
        self._score_calculate()
        if self.score > 21:
            raise Lose('You lose!')
        return self._cards

    @property
    def cards(self) -> list:
        """Retuns all cards in players hand

        Returns:
            list: cards in players hand
        """
        return self._cards

    def _score_calculate(self) -> int:
        """This method calucaltes players score

        Returns:
            int: Players score
        """
        if len(self.cards) == 2 and sum([card.symbol for card in self._cards]) == 2:
            self.score = 21
        else:
            self.score = sum(
                [11 if card.value == 1 and index < 2 else card.value \
                 for index, card in enumerate(self._cards)]
            )
        return self.score


class User(Player):
    """This class represents user in game

    Args:
        Player (class): Inherited class
    """
    def __init__(self):
        """This method initialize User instance
        """
        super().__init__()
        self.passed = False

    def add_cards(self, *args, **kwargs):
        """This method overwrite original method in player to change exception

        Raises:
            CrupierWins: When user exceeds 21 points
        """
        try:
            super().add_cards(*args, **kwargs)
        except Lose as lose:
            raise CrupierWins('You lose!') from lose



class Croupier(Player):
    """This class represents user in game

    Args:
        Player (class): Inherited class
    """
    def __init__(self):
        """This method initialize Croupier instance
        """
        super().__init__()
        self.deck = Deck()
        self.deck.setup()

    def game_init(self) -> list:
        """Croupier deals 2 cards himself and returns 2

        Returns:
            list: Start deck
        """
        cards = []
        for _ in range(2):
            cards.append(self.deck.card_distribution())
            self.add_cards(self.deck.card_distribution())
        return cards

    def add_cards(self, *args, **kwargs):
        """This method overwrite original method in player to change exception

        Raises:
            UserWins: When croupier exceeds 21 points
        """
        try:
            super().add_cards(*args, **kwargs)
        except Lose as lose:
            raise UserWins('You wins') from lose
