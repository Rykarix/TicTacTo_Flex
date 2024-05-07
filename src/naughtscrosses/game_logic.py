import numpy as np


class Player:
    def __init__(self, name: str, player_id: int, symbol: str):
        self.name = name
        self.id = player_id
        self.symbol = symbol


class NaughtsAndCrosses:
    def __init__(self, player1: Player, player2: Player):
        self.board = np.zeros((3, 3), dtype=int)
        self.players = {1: player1, 2: player2}
        self.current_player = 1
        self.winner = None
        self.game_over = False

    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1
        self.winner = None
        self.game_over = False

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                self.winner = self.board[i][0]
                self.game_over = True
                return
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                self.winner = self.board[0][i]
                self.game_over = True
                return
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            self.winner = self.board[0][0]
            self.game_over = True
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            self.winner = self.board[0][2]
            self.game_over = True
            return
        if np.all(self.board != 0):
            self.game_over = True

    def update(self, x: int, y: int) -> bool:
        if self.game_over:
            return False
        if self.board[x][y] != 0:
            return False
        self.board[x][y] = self.current_player
        self.check_winner()
        if not self.game_over:
            self.current_player = 3 - self.current_player
        return True
