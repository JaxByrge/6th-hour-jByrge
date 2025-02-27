#Name: Jax Byrge
#Class: 6th
#Assignment: Ai Playground
import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [(200, 0, 0), (0, 200, 0), (0, 0, 200), (200, 200, 0), (200, 0, 200), (0, 200, 200)]

# Define Tetris shapes
SHAPES = [
    [(0, 0), (1, 0), (0, 1), (1, 1)],  # Square
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # Line
    [(0, 1), (1, 1), (2, 1), (1, 0)],  # T-shape
    [(0, 1), (1, 1), (1, 0), (2, 0)],  # Z-shape
    [(0, 0), (1, 0), (1, 1), (2, 1)]  # S-shape
]

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

grid = [[None for _ in range(WIDTH // BLOCK_SIZE)] for _ in range(HEIGHT // BLOCK_SIZE)]
score = 0


class Block:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.x = WIDTH // BLOCK_SIZE // 2
        self.y = 0
        self.color = random.choice(COLORS)

    def move_down(self):
        if not self.collides(0, 1):
            self.y += 1
        else:
            self.add_to_grid()
            clear_rows()
            return False
        return True

    def move_sideways(self, dx):
        if not self.collides(dx, 0):
            self.x += dx

    def rotate(self):
        rotated = [(y, -x) for x, y in self.shape]
        if not self.collides(0, 0, rotated):
            self.shape = rotated

    def collides(self, dx, dy, shape=None):
        shape = shape or self.shape
        for x, y in shape:
            nx, ny = self.x + x + dx, self.y + y + dy
            if nx < 0 or nx >= WIDTH // BLOCK_SIZE or ny >= HEIGHT // BLOCK_SIZE or (
                    ny >= 0 and grid[ny][nx] is not None):
                return True
        return False

    def add_to_grid(self):
        for x, y in self.shape:
            grid[self.y + y][self.x + x] = self.color

    def draw(self):
        for dx, dy in self.shape:
            pygame.draw.rect(screen, self.color,
                             pygame.Rect((self.x + dx) * BLOCK_SIZE, (self.y + dy) * BLOCK_SIZE, BLOCK_SIZE,
                                         BLOCK_SIZE))


def clear_rows():
    global grid, score
    new_grid = [row for row in grid if any(cell is None for cell in row)]
    cleared_rows = len(grid) - len(new_grid)
    score += cleared_rows
    while len(new_grid) < len(grid):
        new_grid.insert(0, [None for _ in range(WIDTH // BLOCK_SIZE)])
    grid = new_grid


def draw_grid():
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x]:
                pygame.draw.rect(screen, grid[y][x],
                                 pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


def draw_score():
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))


# Main loop
running = True
block = Block()
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                block.move_sideways(-1)
            elif event.key == pygame.K_RIGHT:
                block.move_sideways(1)
            elif event.key == pygame.K_DOWN:
                block.move_down()
            elif event.key == pygame.K_UP:
                block.rotate()

    if not block.move_down():
        block = Block()

    draw_grid()
    block.draw()
    draw_score()
    pygame.display.flip()
    clock.tick(5)

pygame.quit()
