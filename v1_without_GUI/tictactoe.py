"""Lógica do jogo da velha (sem interface).

O tabuleiro é uma lista de 9 posições (0..8), da esquerda para a direita e de
cima para baixo:

    0 | 1 | 2
    3 | 4 | 5
    6 | 7 | 8
"""

EMPTY = " "
LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # linhas
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # colunas
    (0, 4, 8), (2, 4, 6),             # diagonais
)


class TicTacToe:
    def __init__(self) -> None:
        self.board = [EMPTY] * 9

    def __str__(self) -> str:
        cells = [c if c != EMPTY else str(i + 1) for i, c in enumerate(self.board)]
        rows = [" {} | {} | {} ".format(*cells[i : i + 3]) for i in range(0, 9, 3)]
        return ("\n" + "-" * 11 + "\n").join(rows)

    def available_moves(self) -> list[int]:
        return [i for i, c in enumerate(self.board) if c == EMPTY]

    def play(self, position: int, player: str) -> None:
        if self.board[position] != EMPTY:
            raise ValueError("posição já ocupada")
        self.board[position] = player

    def winner(self) -> str | None:
        for a, b, c in LINES:
            if self.board[a] != EMPTY and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    def is_full(self) -> bool:
        return EMPTY not in self.board

    def is_over(self) -> bool:
        return self.winner() is not None or self.is_full()

    def reset(self) -> None:
        self.board = [EMPTY] * 9


def best_move(game: TicTacToe, ai: str, human: str) -> int:
    """Escolhe a melhor jogada para `ai` via minimax (nunca perde)."""

    def minimax(is_ai_turn: bool) -> int:
        win = game.winner()
        if win == ai:
            return 1
        if win == human:
            return -1
        if game.is_full():
            return 0

        player = ai if is_ai_turn else human
        scores = []
        for move in game.available_moves():
            game.board[move] = player
            scores.append(minimax(not is_ai_turn))
            game.board[move] = EMPTY
        return max(scores) if is_ai_turn else min(scores)

    best_score = -2
    choice = game.available_moves()[0]
    for move in game.available_moves():
        game.board[move] = ai
        score = minimax(False)
        game.board[move] = EMPTY
        if score > best_score:
            best_score, choice = score, move
    return choice
