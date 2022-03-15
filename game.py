"""This module is the blackjack game

Raises:
    InvalidInput: when user gives invalid input
    Draw: when user and croupier haves the same score
    CrupierWins: when user exceeds 21 points
"""
from core.players import User, Croupier
from core.exceptions import InvalidInput, Draw, CrupierWins, UserWins


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

    @property
    def stats(self) -> str:
        """Generates output for user

        Returns:
            str: Output for user
        """
        return f'Your cards: {"; ".join([str(card) for card in self.user.cards])}\n' \
        f'Your score: {self.user.score}\n' \
        f'Croupiers first card: {self.croupier.cards[0]}'


    def _user_turn(self):
        """Called when user have to make choice

        Raises:
            InvalidInput: Raises when user gives invalid input
        """
        choices = {
            '1': self.hit,
            '2': self.user_passed
        }
        while not self.user.passed:
            print(self.stats)
            print('Your turn:\n\t(1) hit\n\t(2) pass')
            choice = input('Your choice?(1/2): ')

            if (action := choices.get(choice)):
                action()
            else:
                raise InvalidInput('Input is incorrect!'
                                   ' Please choose one of the available option')


    def _croupier_turn(self):
        """This method is responsible for croupier choices
        """
        while self.croupier.score < self.user.score:
            self.croupier.add_cards(self.croupier.deck.card_distribution())
            print(f'Croupier cards: {"; ".join([str(card) for card in self.croupier.cards])}')


    def _check_result(self):
        """Raises correct exception in case when no players exceed max score"""
        if self.croupier.score == self.user.score:
            raise Draw('Draw')

        if self.croupier.score > self.user.score and self.croupier.score <= 21:
            raise CrupierWins('You lose')


    def game_start(self):
        """Called when game's reviving
        """
        try:
            self._user_turn()
        except InvalidInput as exception:
            print(exception)
            self.game_start()

        self._croupier_turn()
        self._check_result()


    def _setup(self) -> list:
        """Setups initial game state

        Returns:
            list: croupiers deck
        """
        self.user.cards.clear()
        self.croupier.cards.clear()
        self.croupier.deck.setup()
        self.user.add_cards(*self.croupier.game_init())
        return self.croupier.deck


    def new_game_start(self):
        """This method is the main part of the game

        Raises:
            InvalidInput: when user gives invalid input
            Draw: when user and croupier haves the same score
            CrupierWins: when user exceeds 21 points
        """
        self._setup()
        print('New game!')
        try:
            self.game_start()

        except Draw as exception:
            print(exception)

        except CrupierWins as exception:
            print(exception)

        except UserWins as exception:
            print(exception)

        except KeyboardInterrupt:
            print('\nEnd\nthanks for game')

if __name__ == '__main__':
    Game().new_game_start()
