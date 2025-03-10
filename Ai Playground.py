#Name: Jax Byrge
#Class: 6th
#Assignment: Ai Playground
import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
BLOCK_SIZE = 30
COLS = 10
ROWS = 20
SCREEN_WIDTH = BLOCK_SIZE * (COLS + 6)  # Extra space for next piece and score
SCREEN_HEIGHT = BLOCK_SIZE * ROWS

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (255, 13, 114),  # pink
    (13, 194, 255),  # cyan
    (13, 255, 114),  # green
    (245, 56, 255),  # purple
    (255, 142, 13),  # orange
    (255, 225, 56),  # yellow
    (56, 119, 255)  # blue
]

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]  # Z
]


class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Tetris')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.reset()

    def reset(self):
        self.grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.score = 0
        self.lines = 0
        self.level = 1
        self.game_over = False
        self.next_piece = None
        self.current_piece = self.new_piece()

    def create_piece(self):
        shape = random.choice(SHAPES)
        color = random.choice(COLORS)
        return {
            'shape': shape,
            'color': color,
            'x': COLS // 2 - len(shape[0]) // 2,
            'y': 0
        }

    def new_piece(self):
        if self.next_piece:
            piece = self.next_piece
        else:
            piece = self.create_piece()
        self.next_piece = self.create_piece()
        return piece

    def collision(self, piece, dx=0, dy=0):
        for y, row in enumerate(piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    new_x = piece['x'] + x + dx
                    new_y = piece['y'] + y + dy
                    if (new_x < 0 or new_x >= COLS or
                            new_y >= ROWS or
                            (new_y >= 0 and self.grid[new_y][new_x])):
                        return True
        return False

    def merge(self):
        for y, row in enumerate(self.current_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current_piece['y'] + y][self.current_piece['x'] + x] = self.current_piece['color']

    def rotate(self):
        if not self.current_piece:
            return
        # Create rotated shape
        current = self.current_piece['shape']
        rotated = [[current[y][x] for y in range(len(current) - 1, -1, -1)]
                   for x in range(len(current[0]))]

        old_shape = self.current_piece['shape']
        self.current_piece['shape'] = rotated

        if self.collision(self.current_piece):
            self.current_piece['shape'] = old_shape

    def clear_lines(self):
        lines_cleared = 0
        y = ROWS - 1
        while y >= 0:
            if all(self.grid[y]):
                lines_cleared += 1
                del self.grid[y]
                self.grid.insert(0, [0 for _ in range(COLS)])
            else:
                y -= 1

        if lines_cleared:
            self.lines += lines_cleared
            self.score += [40, 100, 300, 1200][lines_cleared - 1] * self.level
            self.level = self.lines // 10 + 1

    def move(self, dx):
        if not self.current_piece or self.game_over:
            return
        self.current_piece['x'] += dx
        if self.collision(self.current_piece):
            self.current_piece['x'] -= dx

    def drop(self):
        if not self.current_piece or self.game_over:
            return
        self.current_piece['y'] += 1
        if self.collision(self.current_piece):
            self.current_piece['y'] -= 1
            self.merge()
            self.clear_lines()
            self.current_piece = self.new_piece()
            if self.collision(self.current_piece):
                self.game_over = True

    def hard_drop(self):
        if not self.current_piece or self.game_over:
            return
        while not self.collision(self.current_piece):
            self.current_piece['y'] += 1
        self.current_piece['y'] -= 1
        self.drop()

    def draw_grid(self):
        for y, row in enumerate(self.grid):
            for x, color in enumerate(row):
                if color:
                    pygame.draw.rect(self.screen, color,
                                     (x * BLOCK_SIZE, y * BLOCK_SIZE,
                                      BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(self.screen, (40, 40, 40),
                                 (x * BLOCK_SIZE, y * BLOCK_SIZE,
                                  BLOCK_SIZE, BLOCK_SIZE), 1)

    def draw_current_piece(self):
        if not self.current_piece:
            return
        for y, row in enumerate(self.current_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        self.screen,
                        self.current_piece['color'],
                        ((self.current_piece['x'] + x) * BLOCK_SIZE,
                         (self.current_piece['y'] + y) * BLOCK_SIZE,
                         BLOCK_SIZE, BLOCK_SIZE)
                    )

    def draw_next_piece(self):
        next_x = COLS * BLOCK_SIZE + BLOCK_SIZE
        next_y = BLOCK_SIZE * 2
        # Draw "Next" text
        next_text = self.font.render("Next:", True, WHITE)
        self.screen.blit(next_text, (next_x, BLOCK_SIZE))

        for y, row in enumerate(self.next_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        self.screen,
                        self.next_piece['color'],
                        (next_x + x * BLOCK_SIZE,
                         next_y + y * BLOCK_SIZE,
                         BLOCK_SIZE, BLOCK_SIZE)
                    )

    def draw_score(self):
        score_x = COLS * BLOCK_SIZE + BLOCK_SIZE
        score_y = BLOCK_SIZE * 6

        # Draw Score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (score_x, score_y))

        # Draw Level
        level_text = self.font.render(f"Level: {self.level}", True, WHITE)
        self.screen.blit(level_text, (score_x, score_y + 40))

        # Draw Lines
        lines_text = self.font.render(f"Lines: {self.lines}", True, WHITE)
        self.screen.blit(lines_text, (score_x, score_y + 80))

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_grid()
        self.draw_current_piece()
        self.draw_next_piece()
        self.draw_score()

        if self.game_over:
            game_over_text = self.font.render("GAME OVER", True, WHITE)
            restart_text = self.font.render("Press ENTER to restart", True, WHITE)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))
            self.screen.blit(game_over_text, text_rect)
            self.screen.blit(restart_text, restart_rect)

        pygame.display.flip()

    def run(self):
        last_drop = time.time()
        running = True

        while running:
            current_time = time.time()
            drop_time = 1.0 - (min(self.level, 20) - 1) * 0.05  # Speed increases with level

            if current_time - last_drop > drop_time and not self.game_over:
                self.drop()
                last_drop = current_time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if self.game_over:
                        if event.key == pygame.K_RETURN:
                            self.reset()
                            last_drop = time.time()
                        continue

                    if event.key == pygame.K_LEFT:
                        self.move(-1)
                    elif event.key == pygame.K_RIGHT:
                        self.move(1)
                    elif event.key == pygame.K_DOWN:
                        self.drop()
                    elif event.key == pygame.K_UP:
                        self.rotate()
                    elif event.key == pygame.K_SPACE:
                        self.hard_drop()

            self.draw()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    game = Tetris()
    game.run()