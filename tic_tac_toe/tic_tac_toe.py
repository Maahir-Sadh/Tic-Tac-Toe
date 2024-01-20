# A tic-tac-toe game made to be played in the console.
# Also has a variable board size.

class Board:
    '''
Class to set the board of Tic-Tac-Toe.

Attributes:
    size:
        Size of the board. Any positive integer.
        3x3 board by default.

    state:
        The current position of X's and O's on the board. Empty board at start of the game.

    player:
        The number of the current playing player (total number of players is 2). Not visible to user.
        default is player 0 (the one marking the O's)

Methods:
    display:
        prints the board.

    turn:
        updates the state of the game after the player chooses their square.

    win:
        checks if any player has won.

    change_player:
        passes the turn to the next player.
    '''

    # The symbols' of each player.
    player_to_symb = { 0:'O', 1:'X' }

    def __init__(self, size : int = 3, player = 0):
        assert size >= 3
        self.size = size
        self.state = [ [ ' ' for i in range(size)] for i in range(size) ]
        self.player = player

    def display(self):
        '''
        Displays the current game position on the console.
        '''

        print('  ' + ' '.join(map(str,range(1,self.size+1))))
        print()
        for i, row in enumerate(self.state):
            print(f'{i+1} ' + '|'.join(row))
            if i != self.size - 1:
                print('  ' + '-' * (2 * self.size -1))
        print()

    def turn(self, row : int, col : int):
        '''
        The current player chooses the square and this method updates the state of the game.

        row: int
            The row number chosen by the current Player.

        col: int
            The column number chosen by the current player
        '''

        assert (row in range(self.size)) and (col in range(self.size))
        if self.state[row][col] != ' ':
            return False
        else:
            self.state[row][col] = self.player_to_symb[self.player]
            return True

    def win(self):
        '''
        Lists cases of possibile victories and checks whether the win condition has been satisfied.
        '''
        from copy import deepcopy        
        win_cases = deepcopy(self.state)
        for i in range(self.size):
            win_cases.append([ self.state[j][i] for j in range(self.size) ])

        win_cases.append([ self.state[i][i] for i in range(self.size) ])
        win_cases.append([ self.state[i][-i] for i in range(self.size) ])
        
        from functools import reduce
        for case in win_cases:
            if reduce( lambda a, b: a if a == b else 'False' , case ) in 'XO':
                return True
                break
        else:
            return False

    def is_draw(self):
        '''
        Checks whether the board is completely filled, that is, whether the game ended in a draw.
        '''
        
        for row in self.state:
            if ' ' in row:
                return False
                break
        else:
            return True

    def change_player(self):
        '''
        Cycles to the next player over.
        '''

        self.player = (self.player + 1) % 2

    # End of Board class.

def gameloop(n : int = 3):
    game = Board(n)
    while True:
        game.display()
        print('Player {} \'s turn!'.format(game.player_to_symb[game.player]))
        try:
            row = int(input('Enter row number where to mark    : ')) - 1
            col = int(input('Enter column number where to mark : ')) - 1
            assert (row in range(game.size)) and (col in range(game.size))
            #redundant statement, may be optimized in the future

        except:
            print('Please enter a valid row/column number.')

        else:
            if game.turn(row,col):
                if game.win():
                    print('Player {} has won! Congratulations!\n'.format(game.player_to_symb[game.player]))
                    break
                elif game.is_draw():
                    print('This game is a draw.\n')
                    break
                else:
                    game.change_player()
            
            else:
                print('Cell is already filled! Try again. (Nice Try)')
    del game    

def main():

    while True:
        print('Welcome to Tic-Tac-Toe (Command Line Ver.) !')
        print('1. Rules')
        print('2. Play a Game.')
        print('3. Play extended board')
        print('4. Exit.')
        print()

        try:
            choice = int( input("Enter choice (1,2,3,4) :") )
            assert choice <= 4

        except:
            print('Please enter a valid choice from 1,2,3,4. \n')

        else:
            if choice == 1:
                pass
            
            elif choice == 2:
                gameloop(3)

            elif choice == 3:
                try:
                    n = int( input('Enter the board size you want to play on (between 3 and 9) : '))
                    assert n >= 3 and n <= 9
                    gameloop(n)

                except:
                    print('Please keep the size to a reasonable number between 3 and 9.\n')
                
            elif choice == 4:
                print('Thank you for coming!')
                break
            
            else:
                print('Invalid choice. Try again.')

if __name__ == '__main__':
    main()
