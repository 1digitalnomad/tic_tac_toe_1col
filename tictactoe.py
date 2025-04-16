# check if player wins on rigt side.

# def did_I_win_2_down(player, board):
#     # first option
#     # did_win = board[0][2] == player and board[1][2] == player and board[2][2] == player
#     # print(did_win)
#     # second option
#     did_win = True
#     for x in range(3):
#         did_win &= player == board[x][2]
#     return did_win


# print(did_I_win_2_down('X',
#                        [
#                            ['O', 'O', 'X'],
#                            ['O', 'X', 'O'],
#                            ['X', 'O', 'O']
#                        ]
#                        ))

# print(did_I_win_2_down('O', [['O', 'O', 'X'],
#                        ['O', 'X', 'O'],
#                        ['X', 'O', 'O']]))


# print(did_I_win_2_down('X', [['O', 'O', 'X'],
#                        ['O', 'O', 'X'],
#                        ['O', 'O', 'X']]))


# print(did_I_win_2_down('O', [['O', 'O', 'X'],
#                        ['O', 'O', 'X'],
#                        ['O', 'O', 'X']]))


# Check if player wins any column


def did_i_win_down(player, board):

    for i in range(3):
        if player == board[0][i] and player == board[1][i] and player == board[2][i]:
            return True
    return False

    # print(f'did {player} win? {did_win} ')


1
print(did_i_win_down("x", [
    ['o', 'o', 'x'],  # 0
    ['o', 'x', 'o'],  # 1
    ['x', 'o', 'o'],  # 2

]))

# 2
print(did_i_win_down("o", [
    ['o', 'o', 'x'],
    ['o', 'x', 'o'],
    ['x', 'o', 'o'],

]))
# 3
print(did_i_win_down("x", [
    ['o', 'o', 'x'],
    ['o', 'o', 'x'],
    ['o', 'o', 'x'],

]))
4
print(did_i_win_down("o", [
    ['o', 'o', 'x'],
    ['o', 'o', 'x'],
    ['o', 'o', 'x'],

]))
