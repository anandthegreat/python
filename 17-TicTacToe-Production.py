"""Tic-tac-toe (n x n) winner detection.

Provides a single public function, `check_winner`, that inspects an n x n
board and reports whether the game is won, drawn, or still in progress.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Sequence

EMPTY_CELL = ""
PLAYER_X = "X"
PLAYER_O = "O"
VALID_MARKS = frozenset({EMPTY_CELL, PLAYER_X, PLAYER_O})


class GameStatus(str, Enum):
    """Possible outcomes of a board inspection."""

    IN_PROGRESS = "in_progress"
    GAME_OVER = "game_over"
    DRAW = "draw"


class WinDirection(str, Enum):
    """How a winning line was formed."""

    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"
    DIAGONAL = "diagonal"
    ANTI_DIAGONAL = "anti_diagonal"


@dataclass(frozen=True)
class GameResult:
    """Outcome of a `check_winner` call.

    Attributes:
        status: Overall game state.
        winner: The winning mark ('X' or 'O'), or None if no winner.
        direction: How the win was formed, or None if no winner.
    """

    status: GameStatus
    winner: Optional[str] = None
    direction: Optional[WinDirection] = None


class InvalidBoardError(ValueError):
    """Raised when the board fails structural or content validation."""


def _validate_board(board: Sequence[Sequence[str]]) -> int:
    """Validate board shape and contents; return the board size n.

    Raises:
        InvalidBoardError: if the board is empty, non-square, ragged,
            or contains a mark outside {'', 'X', 'O'}.
    """
    if not board:
        raise InvalidBoardError("Board must not be empty.")

    n = len(board)
    for row_idx, row in enumerate(board):
        if len(row) != n:
            raise InvalidBoardError(
                f"Board must be square: row {row_idx} has {len(row)} "
                f"cells, expected {n}."
            )
        for col_idx, cell in enumerate(row):
            if cell not in VALID_MARKS:
                raise InvalidBoardError(
                    f"Invalid mark {cell!r} at ({row_idx}, {col_idx}); "
                    f"expected one of {sorted(VALID_MARKS)!r}."
                )
    return n


def _line_winner(line: Sequence[str]) -> Optional[str]:
    """Return 'X' or 'O' if every cell in the line matches, else None."""
    first = line[0]
    if first == EMPTY_CELL:
        return None
    return first if all(cell == first for cell in line) else None


def check_winner(board: Sequence[Sequence[str]]) -> GameResult:
    """Inspect an n x n tic-tac-toe board and report the game state.

    Args:
        board: An n x n grid of cell values. Each cell must be one of
            '' (empty), 'X', or 'O'.

    Returns:
        A GameResult describing whether the game is in progress, won,
        or drawn.

    Raises:
        InvalidBoardError: if the board is malformed (see _validate_board).

    Example:
        >>> check_winner([["X", "", ""], ["", "X", ""], ["O", "O", "X"]])
        GameResult(status=<GameStatus.GAME_OVER: 'game_over'>, winner='X', direction=<WinDirection.DIAGONAL: 'diagonal'>)
    """
    n = _validate_board(board)

    # Rows
    for i in range(n):
        winner = _line_winner(board[i])
        if winner:
            return GameResult(GameStatus.GAME_OVER, winner, WinDirection.HORIZONTAL)

    # Columns
    for j in range(n):
        column = [board[i][j] for i in range(n)]
        winner = _line_winner(column)
        if winner:
            return GameResult(GameStatus.GAME_OVER, winner, WinDirection.VERTICAL)

    # Main diagonal (top-left to bottom-right)
    diagonal = [board[i][i] for i in range(n)]
    winner = _line_winner(diagonal)
    if winner:
        return GameResult(GameStatus.GAME_OVER, winner, WinDirection.DIAGONAL)

    # Anti-diagonal (top-right to bottom-left)
    anti_diagonal = [board[i][n - 1 - i] for i in range(n)]
    winner = _line_winner(anti_diagonal)
    if winner:
        return GameResult(GameStatus.GAME_OVER, winner, WinDirection.ANTI_DIAGONAL)

    # No winner — check for a draw (board full) vs still in progress
    board_full = all(cell != EMPTY_CELL for row in board for cell in row)
    if board_full:
        return GameResult(GameStatus.DRAW)

    return GameResult(GameStatus.IN_PROGRESS)


if __name__ == "__main__":
    boards = [
        [["X", "", ""], ["", "X", ""], ["O", "O", "X"]],   # diagonal X wins
        [["O", "", "X"], ["", "X", ""], ["X", "O", "O"]],   # anti-diagonal X wins
        [["X", "", ""], ["", "X", ""], ["O", "O", "O"]],   # horizontal O wins
        [["O", "", ""], ["O", "X", ""], ["O", "X", "X"]],   # vertical O wins
        [["X", "", ""], ["", "X", ""], ["O", "O", ""]],   # in progress
        [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "O"]],  # draw
    ]
    for b in boards:
        print(check_winner(b))
