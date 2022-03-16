"""
This module is responsible for representation data in blackjack module
"""
from random import shuffle
from .exceptions import InvalidColor


COLORS = {
    'Clubs' : '\u2663',
    'Diamonds': '\u2666',
    'Hearts': '\u2665',
    'Spades': '\u2660',
}

class Card:
    """
    This class represents one card
    """
    def __init__(self, color: str, symbol: int):
        """This method initialize Card instance

        Args:
            color (str): Color of the card.
            It must one of the: 'Spades', 'Hearts', 'Clubs', 'Diamonds'
            symbol (int): Symbol of the card, must be in the range 1-13.
            Symbols: 1 - Ace, 11 - Jack, 12 - Qeen, 13 - King
        """
        if (color_symbol := COLORS.get(color)):
            self.color = color_symbol
        else:
            raise InvalidColor('Wrong value')

        self.symbol = symbol
        self.value = self.symbol if self.symbol < 11 else 10


    def __str__(self) -> str:
        """This method is responsible of text representation of the card

        Returns:
            str: text representation of the card
        """
        verb = {
            '1': 'Ace',
            '11': 'Jack',
            '12': 'Queen',
            '13': 'King'
        }

        if (symbol := verb.get(str(self.symbol))):
            return f'c: {self.color} s: {symbol}'
        return f'c: {self.color} s: {self.symbol}'


    def __eq__(self, other) -> bool:
        """This method compare instances of the Card class

        Args:
            other (Card): Other instance of Card class

        Returns:
            bool: True if color and symbol of the card and other card are the same else False
        """
        return all([
            self.color == other.color,
            self.symbol == other.symbol,
        ])


    def __hash__(self) -> int:
        """This method hashs Card instance
        Returns:
            int: Hash of a card instance
        """
        return hash((self.color, self.symbol))

class Deck:
    """
    This class represents deck in game
    """
    def __init__(self):
        """
        This method initialize instance of the Deck class
        """
        self.cards = []

    def shuffle(self) -> list:
        """This method shuffles cards in self.cards

        Returns:
            list: All cards in deck
        """
        shuffle(self.cards)
        return self.cards

    def add_cards(self, *args: Card) -> list:
        """This method adds cards to deck

        Arguments:
            args {Card}: instances of the Card class which will have added to deck

        Returns:
            list: Cards in deck
        """
        self.cards += list(args)
        return self.cards


    def setup(self) -> list:
        """This method prepares cards and shuffles it

        Returns:
            list: Cards in deck
        """
        self.cards = list(Deck.card_gen())
        self.shuffle()
        return self.cards


    def card_distribution(self) -> Card:
        """This method takes last card from the deck

        Returns:
            Card: Last card in deck
        """
        return self.cards.pop(-1)


    @staticmethod
    def card_gen() -> Card:
        """This method generate card sequences from 52 cards deck

        Yields:
            Card: Instance of the Card class
        """
        for color in COLORS:
            for symbol in range(1, 14):
                yield Card(color, symbol)
