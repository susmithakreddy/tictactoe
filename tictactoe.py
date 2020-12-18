import pygame
import sys
import numpy as np

pygame.init()  # intializing the pygame module

WIDTH = 600
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 10
CROSS_WIDTH = 15
CROSS_SPACE = 50
SQUARE_SIZE = 200

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(WHITE)

#board
board = np.zeros((BOARD_ROWS, BOARD_COLS))


def draw_lines():
    pygame.draw.line(screen, BLACK, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (400, 0), (400, 600), LINE_WIDTH)


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (int(
                    col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, BLUE, (col * 200 + CROSS_SPACE, row * 200 + 200 - CROSS_SPACE),
                                 (col * 200 + 200 - CROSS_SPACE, row * 200 + CROSS_SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, BLUE, (col * 200 + CROSS_SPACE, row * 200 + CROSS_SPACE),
                                 (col * 200 + 200 - CROSS_SPACE, row * 200 + 200 - CROSS_SPACE), CROSS_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def check_win(player):
    # vertical win check
	for col in range(BOARD_COLS):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			draw_vertical_win_line(col, player)
			return True

	# horizontal win check
	for row in range(BOARD_ROWS):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			draw_horizontal_win_line(row, player)
			return True

	# asc diagonal win check
	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		draw_asc_diagonal(player)
		return True

	# desc diagonal win chek
	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		draw_desc_diagonal(player)
		return True

	return False


def draw_vertical_win_line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE//2
    if player == 1 :
	    color = RED
    elif player == 2:
        color = BLUE
    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH)


def draw_horizontal_win_line(row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE//2
    if player == 1:
	    color = RED
    elif player == 2:
	    color = BLUE
    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)


def draw_asc_diagonal(player):
    if player == 1:
	    color = RED
    elif player == 2:
	    color = BLUE
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


def draw_desc_diagonal(player):
    if player == 1:
	    color = RED
    elif player == 2:
	    color = BLUE
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)


def restart():
    screen.fill(WHITE)
    draw_lines()
    for row in range(BOARD_ROWS):
	    for col in range(BOARD_COLS):
		    board[row][col] = 0


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


draw_lines()

player = 1
game_over=False

#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over=True
                player = player % 2 + 1

                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False

    pygame.display.update()
