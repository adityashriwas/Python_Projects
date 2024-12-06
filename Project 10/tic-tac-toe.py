import sys
import pygame
import numpy as np
import random

pygame.init()

# Colors
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Dimensions
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 5
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 15
FONT_SIZE = 30

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BLACK)

# Font for displaying the winner
font = pygame.font.Font(None, FONT_SIZE)

# Game variables
board = np.zeros((BOARD_ROWS, BOARD_COLS))
player = 1
game_over = False
winner = None
difficulty = "hard"  # Default AI difficulty


def draw_lines(color=WHITE):
    """Draw grid lines."""
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, color, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
        pygame.draw.line(screen, color, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)


def draw_figures():
    """Draw the players' marks on the board."""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:  # Player 1 (Circle)
                pygame.draw.circle(screen, WHITE,
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:  # AI (Cross)
                pygame.draw.line(screen, WHITE,
                                 (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4),
                                 (col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4),
                                 CROSS_WIDTH)
                pygame.draw.line(screen, WHITE,
                                 (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4),
                                 (col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4),
                                 CROSS_WIDTH)


def display_winner(winner):
    """Display the winner on the screen."""
    text = ""
    if winner == 1:
        text = "Player Wins!"
        color = GREEN
    elif winner == 2:
        text = "AI Wins!"
        color = RED
    elif winner == "draw":
        text = "It's a Draw!"
        color = GRAY

    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)


def mark_square(row, col, player):
    """Mark a square on the board."""
    board[row][col] = player


def available_square(row, col):
    """Check if a square is available."""
    return board[row][col] == 0


def is_board_full():
    """Check if the board is full."""
    return not any(0 in row for row in board)


def check_win(player):
    """Check if a player has won."""
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def minimax(board, depth, is_maximizing):
    """Minimax algorithm for unbeatable AI."""
    if check_win(2):  # AI wins
        return 10 - depth
    elif check_win(1):  # Player wins
        return depth - 10
    elif is_board_full():  # Draw
        return 0

    if is_maximizing:  # AI's turn
        best_score = float('-inf')
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 0:
                    board[row][col] = 2
                    score = minimax(board, depth + 1, False)
                    board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:  # Player's turn
        best_score = float('inf')
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 0:
                    board[row][col] = 1
                    score = minimax(board, depth + 1, True)
                    board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score


def best_move():
    """Find the best move for the AI using Minimax."""
    best_score = float('-inf')
    move = (-1, -1)
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(board, 0, False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col)
    if move != (-1, -1):
        mark_square(move[0], move[1], 2)


def random_move():
    """Make a random move for Easy AI."""
    empty_spots = [(row, col) for row in range(BOARD_ROWS) for col in range(BOARD_COLS) if board[row][col] == 0]
    if empty_spots:
        row, col = random.choice(empty_spots)
        mark_square(row, col, 2)


def restart_game():
    """Restart the game."""
    global board, player, game_over, winner
    board = np.zeros((BOARD_ROWS, BOARD_COLS))
    player = 1
    game_over = False
    winner = None
    screen.fill(BLACK)
    draw_lines()


# Draw initial lines
draw_lines()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] // SQUARE_SIZE
            mouseY = event.pos[1] // SQUARE_SIZE

            if available_square(mouseY, mouseX):
                mark_square(mouseY, mouseX, player)
                if check_win(player):
                    winner = player
                    game_over = True
                player = 2  # Switch to AI

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()

    if not game_over and player == 2:  # AI's turn
        if difficulty == "easy":
            random_move()
        else:
            best_move()
        if check_win(2):
            winner = 2
            game_over = True
        player = 1

    if game_over and winner is None and is_board_full():
        winner = "draw"

    screen.fill(BLACK)
    draw_lines()
    draw_figures()
    if game_over:
        display_winner(winner)
    pygame.display.update()