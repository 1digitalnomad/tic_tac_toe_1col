def did_I_win_2_down(player, board):
    did_win = board[0][2] == player and board[1][2] == player and board[2][2] == player
    print(did_win)


did_I_win_2_down('X',
                 [
                     ['O', 'O', 'X'],
                     ['O', 'X', 'O'],
                     ['X', 'O', 'O']
                 ]
                 )

did_I_win_2_down('O', [['O', 'O', 'X'],
                       ['O', 'X', 'O'],
                       ['X', 'O', 'O']])


did_I_win_2_down('X', [['O', 'O', 'X'],
                       ['O', 'O', 'X'],
                       ['O', 'O', 'X']])


did_I_win_2_down('O', [['O', 'O', 'X'],
                       ['O', 'O', 'X'],
                       ['O', 'O', 'X']])
