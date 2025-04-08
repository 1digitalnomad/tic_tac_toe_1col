def did_I_win_2_down(player, board):
    # first option
    # did_win = board[0][2] == player and board[1][2] == player and board[2][2] == player
    # print(did_win)
    # second option
    did_win = True
    for x in range(3):
        did_win &= player == board[x][2]
    return did_win


print(did_I_win_2_down('X',
                       [
                           ['O', 'O', 'X'],
                           ['O', 'X', 'O'],
                           ['X', 'O', 'O']
                       ]
                       ))

print(did_I_win_2_down('O', [['O', 'O', 'X'],
                       ['O', 'X', 'O'],
                       ['X', 'O', 'O']]))


print(did_I_win_2_down('X', [['O', 'O', 'X'],
                       ['O', 'O', 'X'],
                       ['O', 'O', 'X']]))


print(did_I_win_2_down('O', [['O', 'O', 'X'],
                       ['O', 'O', 'X'],
                       ['O', 'O', 'X']]))
