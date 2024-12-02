import numpy as np

class TicTacToe:
  def __init__(self):
    self.board = np.array([[' ']*3]*3)
    self.turn = 'X'
    self.winner = None
    self.game_over = False
    
  def print_board(self):
    print('   0   1   2')
    for i, row in enumerate(self.board):
      print(i, end='  ')
      for cell in row:
        print(cell, end=' | ')
      print()
      print(' -------------')
  
  def make_move(self, row, col):
    if self.board[row][col] == ' ':
      self.board[row][col] = self.turn
      self.check_winner()
      self.turn = 'X' if self.turn == 'O' else 'O'
    else:
      print('Invalid move. Try again.')
  
  def check_winner(self):
    for i in range(3):
      if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
        self.winner = self.board[i][0]
        self.game_over = True
      if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
        self.winner = self.board[0][i]
        self.game_over = True
    if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
      self.winner = self.board[0][0]
      self.game_over = True
    if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
      self.winner = self.board[0][2]
      self.game_over = True
    if ' ' not in self.board:
      self.game_over = True
      print('Tie game!')
  
  def play(self):
    while not self.game_over:
      self.print_board()
      print(f'{self.turn}\'s turn')
      row = int(input('Enter row: '))
      col = int(input('Enter col: '))
      self.make_move(row, col)
    self.print_board()
    if self.winner:
      print(f'{self.winner} wins!')
    else:
      print('Game over!')

game = TicTacToe()
game.play()
