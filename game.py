"""This module is the blackjack game

Raises:
    InvalidInput: when user gives invalid input
    Draw: when user and croupier haves the same score
    CrupierWins: when user exceeds 21 points
"""
from core.players import User, Croupier
from core.exceptions import InvalidInput, Draw, CrupierWins


class Game:
    """This class represents blackjack game
    """
    def __init__(self):
        """This method initializes Game class instance
        """
        self.user = User()
        self.croupier = Croupier()

    def hit(self):
        """This method is called when user hits a card
        """
        self.user.add_cards(self.croupier.deck.card_distribution())

    def user_passed(self):
        """This method is called when user passes the game
        """
        self.user.passed = True
        print(f'Croupier cards: {"; ".join([str(card) for card in self.croupier.cards])}')


    def game_start(self):
        """This method is the main part of the game

        Raises:
            InvalidInput: when user gives invalid input
            Draw: when user and croupier haves the same score
            CrupierWins: when user exceeds 21 points
        """
        choices = {
            '1': self.hit,
            '2': self.user_passed
        }
        self.user.cards.clear()
        self.croupier.cards.clear()
        self.croupier.deck.setup()
        self.user.add_cards(*self.croupier.game_init())
        print('New game!')
        try:
            while not self.user.passed:
                print(f'Your cards: {"; ".join([str(card) for card in self.user.cards])}')
                print(f'Your score: {self.user.score}')
                print(f'Croupiers first card: {self.croupier.cards[0]}')
                print('Your turn:\n\t(1) hit\n\t(2) pass')
                choice = input('Your choice?(1/2): ')

                if (action := choices.get(choice)):
                    action()
                else:
                    raise InvalidInput('Input is incorrect!'
                                       ' Please choose one of the available option')

            while self.croupier.score < self.user.score:
                self.croupier.add_cards(self.croupier.deck.card_distribution())
                print(f'Croupier cards: {"; ".join([str(card) for card in self.croupier.cards])}')

            if self.croupier.score == self.user.score:
                raise Draw('Draw')

            if self.croupier.score > self.user.score and self.croupier.score <= 21:
                raise CrupierWins('You lose')


        except Exception as exception:
            print(exception)

if __name__ == '__main__':
    Game().game_start()
