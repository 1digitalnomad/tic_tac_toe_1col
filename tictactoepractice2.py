# using boolean aggregators
# did the last column have a win down?
# def did_I_win_2_down(player, board):
#     # option 1 but it is not dry
#     # did_win = player == board[0][2] and player == board[1][2] and player == board[2][2]
#     # print("=" * 5)
#     # return did_win

#     # option 2
#     did_win = True
#     for i in range(len(board[0])):
#         did_win &= player == board[i][2]
#     return did_win


# print(did_I_win_2_down('X',
#                        [['O', 'O', 'X'],
#                         ['O', 'X', 'O'],
#                            ['X', 'O', 'O']]
#                        ))

# print(did_I_win_2_down('O',
#                        [['O', 'O', 'X'],
#                         ['O', 'X', 'O'],
#                            ['X', 'O', 'O']]
#                        ))

# print(did_I_win_2_down('X',
#                        [['O', 'O', 'X'],
#                         ['O', 'X', 'X'],
#                            ['X', 'O', 'X']]
#                        ))

# print(did_I_win_2_down('O',
#                        [['O', 'O', 'X'],
#                         ['O', 'X', 'X'],
#                            ['X', 'O', 'X']]
#                        ))

print("="*5)

# did any column win?
# For each column:
# Assume I won.

# Check each row in that column:
# If any cell isn’t mine, I didn’t win this column.
# If I won any column, return True.
# Otherwise, return False.


def did_I_win_down(player, board):
    all_win = False  # This means “So far, I haven’t found any winning column.”
    for col in range(3):  # loop through each column 0,1,2. we start with 0.
        did_win = True  # Start each column assuming it's a winning column.→ Optimistic: “Let’s assume this column is all mine.”

        for row in range(3):  # now we loop each row in column 0, 1,2. We start with 0
            # is player == to the current piece on the board?
            did_win &= player == board[row][col]
        # if any column (did win) then all_win should changed to True. either one has to be true to be True. fale or true = true
        all_win |= did_win
    return all_win  # return after all the loops are done


# true
print("any column win?", did_I_win_down("X",
                                        [['X', 'O', 'X'],
                                         ['O', 'X', 'X'],
                                            ['X', 'O', 'X']
                                         ])
      )

# # false
print("any column win?", did_I_win_down('O',
                                        [['O', 'O', 'X'],
                                         ['O', 'X', 'X'],
                                            ['X', 'O', 'X']]
                                        ))

# # false
print("any column win?", did_I_win_down('O',
                                        [['O', 'O', 'X'],
                                         ['O', 'X', 'O'],
                                            ['X', 'O', 'X']]
                                        ))
# # true
print("any column win?", did_I_win_down('O',
                                        [['O', 'O', 'X'],
                                         ['O', 'O', 'O'],
                                            ['X', 'O', 'X']]
                                        ))
