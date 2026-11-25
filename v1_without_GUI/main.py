#!/usr/bin/env python3
"""Jogo da velha no terminal.

Modos:
  1 - Um jogador contra o computador (imbatível)
  2 - Dois jogadores no mesmo computador
"""

from tictactoe import TicTacToe, best_move

HUMAN = "X"
AI = "O"


def ask_int(prompt: str, valid) -> int:
    while True:
        answer = input(prompt).strip()
        if answer.isdigit() and int(answer) in valid:
            return int(answer)
        print(f"  Digite um valor entre {min(valid)} e {max(valid)}.")


def ask_move(game: TicTacToe, player: str) -> int:
    while True:
        pos = ask_int(f"Jogador {player}, escolha uma casa (1-9): ", range(1, 10)) - 1
        if pos in game.available_moves():
            return pos
        print("  Essa casa já está ocupada.")


def play_game(players: int) -> None:
    game = TicTacToe()
    current = HUMAN
    print("\nVocê é o X.\n" if players == 1 else "\nJogador 1 = X, Jogador 2 = O.\n")

    while not game.is_over():
        print(game, "\n")
        if players == 1 and current == AI:
            move = best_move(game, AI, HUMAN)
            print(f"Computador jogou na casa {move + 1}.\n")
        else:
            move = ask_move(game, current)
        game.play(move, current)
        current = AI if current == HUMAN else HUMAN

    print(game, "\n")
    win = game.winner()
    if win is None:
        print("Deu velha! Ninguém venceu.\n")
    elif players == 1:
        print("Você venceu! 🎉\n" if win == HUMAN else "O computador venceu.\n")
    else:
        print(f"Jogador {win} venceu! 🎉\n")


def main() -> None:
    print("** Jogo da Velha **")
    try:
        while True:
            print("\n1 - Contra o computador\n2 - Dois jogadores")
            players = ask_int("> ", (1, 2))
            play_game(players)
            if ask_int("Jogar de novo? 1-Sim  2-Não\n> ", (1, 2)) == 2:
                break
    except (KeyboardInterrupt, EOFError):
        pass
    print("Até a próxima!")


if __name__ == "__main__":
    main()
