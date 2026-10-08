"""
CodSoft AI Internship - Task 2: Tic-Tac-Toe AI
Unbeatable AI using Minimax with Alpha-Beta Pruning.
Human = 'X', AI = 'O'.
"""
import math

WIN_LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
             (0, 3, 6), (1, 4, 7), (2, 5, 8),
             (0, 4, 8), (2, 4, 6)]
HUMAN, AI = "X", "O"


def print_board(b):
    print()
    for r in range(3):
        print(" " + " | ".join(b[r * 3:r * 3 + 3]))
        if r < 2:
            print("---+---+---")
    print()


def winner(b):
    for a, c, d in WIN_LINES:
        if b[a] != " " and b[a] == b[c] == b[d]:
            return b[a]
    return None


def moves_left(b):
    return [i for i, v in enumerate(b) if v == " "]


def minimax(b, is_ai_turn, alpha, beta, depth):
    w = winner(b)
    if w == AI:
        return 10 - depth          # prefer faster wins
    if w == HUMAN:
        return depth - 10          # prefer slower losses
    if not moves_left(b):
        return 0

    if is_ai_turn:
        best = -math.inf
        for m in moves_left(b):
            b[m] = AI
            best = max(best, minimax(b, False, alpha, beta, depth + 1))
            b[m] = " "
            alpha = max(alpha, best)
            if beta <= alpha:      # alpha-beta cut-off
                break
        return best
    best = math.inf
    for m in moves_left(b):
        b[m] = HUMAN
        best = min(best, minimax(b, True, alpha, beta, depth + 1))
        b[m] = " "
        beta = min(beta, best)
        if beta <= alpha:
            break
    return best


def best_move(b):
    best_score, move = -math.inf, None
    for m in moves_left(b):
        b[m] = AI
        score = minimax(b, False, -math.inf, math.inf, 1)
        b[m] = " "
        if score > best_score:
            best_score, move = score, m
    return move


def human_move(b):
    while True:
        try:
            pos = int(input("Your move (1-9): ")) - 1
            if pos in moves_left(b):
                return pos
            print("That cell is taken or invalid. Try again.")
        except ValueError:
            print("Please enter a number from 1 to 9.")


def play():
    print("Tic-Tac-Toe: you are X, AI is O. Cells are numbered 1-9:")
    print(" 1 | 2 | 3\n---+---+---\n 4 | 5 | 6\n---+---+---\n 7 | 8 | 9")
    board = [" "] * 9
    human_turn = input("Do you want to go first? (y/n): ").strip().lower() != "n"

    while True:
        print_board(board)
        if human_turn:
            board[human_move(board)] = HUMAN
        else:
            print("AI is thinking...")
            board[best_move(board)] = AI
        human_turn = not human_turn

        w = winner(board)
        if w or not moves_left(board):
            print_board(board)
            print("You win!" if w == HUMAN else "AI wins!" if w == AI else "It's a draw!")
            break


if __name__ == "__main__":
    while True:
        play()
        if input("Play again? (y/n): ").strip().lower() != "y":
            break
