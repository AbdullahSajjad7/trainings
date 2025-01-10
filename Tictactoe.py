import json

class TicTacToe:
    def __init__(self, record_path):
        pass
        self.board = [['#','#','#'],['#','#','#'],['#','#','#']]
        self.player = True
        self.turns = 0
        self.record_path = record_path
        self.players_wins = {"Player1": 0, "Player2": 0}

    def show_board(self):
        print("-----------")
        for row in self.board:
            for box in row:
                print('', box, ' ', end='')
            print('')
        print("-----------")

    def switch_player(self):
        self.player = True if self.player == False else False

    def _place_symbol(self, x, y):
        x = int(x)
        y = int(y)
        if x not in [1,2,3] or y not in [1,2,3] or self.board[x-1][y-1] != '#':
            print("Cannot place symbol there")
            return False
        if self.player:
            self.board[x-1][y-1] = 'X'
        else:
            self.board[x-1][y-1] = '0'
        return True
    
    def ask_symbol(self):
        if self.player:
            print("Player 1 Turn")
        else:
            print("Player 2 Turn")
        x, y = input("Enter Row and Column: ").split()
        correct_input = self._place_symbol(x,y)
        while correct_input == False:
            x, y = input("Enter Row and Column again: ").split()
            correct_input = self._place_symbol(x,y)
    
    def _check_row_for_winner(self, symbol, n):
        if self.board[n][0] == self.board[n][1] and self.board[n][0] ==  self.board[n][2] and self.board[n][0] == symbol:
            return True
        return False
    
    def _check_col_for_winner(self, symbol, n):
        if self.board[0][n] == self.board[1][n] and self.board[0][n] ==  self.board[2][n] and self.board[0][n] == symbol:
            return True
        return False
    
    def _check_diagonal_for_winner(self, symbol):
        if self.board[0][0] == self.board[1][1] and self.board[1][1] ==  self.board[2][2] and self.board[0][0] == symbol:
            return True
        if self.board[0][2] == self.board[1][1] and self.board[1][1] ==  self.board[2][0] and self.board[0][2] == symbol:
            return True
        return False

    def _check_winner(self, symbol):
        if(self.turns == 9):
            return True, '#'
        winner_decided = False
        for i in range(3):
            winner_decided = self._check_row_for_winner(symbol, i)
            if winner_decided:
                return True, symbol
        for i in range(3):
            winner_decided = self._check_col_for_winner(symbol, i)
            if winner_decided:
                return True, symbol
        winner_decided = self._check_diagonal_for_winner(symbol)
        return winner_decided, symbol
    
    def _reset_game(self):
        self.board = [['#','#','#'],['#','#','#'],['#','#','#']]
        self.player = True
        self.turns = 0

    def fetch_records(self):
        with open(self.record_path, 'r') as file_obj:
            json_record = json.load(file_obj)
            self.players_wins = json_record

    def store_records(self):
        json_record = json.dumps(self.players_wins, indent=4)
        with open(self.record_path, 'w') as file_obj:
            file_obj.truncate(0)
            file_obj.write(json_record)

    def _update_record(self, player):
        if player == "Player1":
            self.players_wins["Player1"] += 1
        else:
            self.players_wins["Player2"] += 1

    def show_record(self):
        print("Player 1 Wins: ", self.players_wins["Player1"])
        print("Player 2 Wins: ", self.players_wins["Player2"])

    def simulate(self):
        self.fetch_records()
        continue_game = 'Y'
        while continue_game.lower() == 'y':
            player_decided = False
            winner = '#'
            print("---------------------------")
            print("Welcome to Tic Tac Toe Game")
            print("---------------------------")
            self.show_board()
            while(not player_decided):
                self.ask_symbol()
                self.show_board()
                if self.player:
                    player_decided, winner = self._check_winner('X')
                else:
                    player_decided, winner = self._check_winner('0')
                self.switch_player()
            
            if(winner == 'X'):
                print("Player 1 Won")
                self._update_record("Player1")
            elif(winner == '0'):
                print("Player 2 Won")
                self._update_record("Player2")
            else:
                print("Match Tied")

            self.show_record()

            self._reset_game()
            continue_game = input("Enter 'Y' if you want to continue: ")

        self.store_records()



game = TicTacToe(r"C:\Users\abdul\OneDrive\Desktop\Training\Games\TicTacToe.json")
game.simulate()