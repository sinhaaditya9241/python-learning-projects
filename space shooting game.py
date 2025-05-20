import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Set up screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter")

# Load fonts
font = pygame.font.SysFont("arial", 30)
game_over_font = pygame.font.SysFont("arial", 64)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((50, 38))
        self.image.fill(BLACK)
        pygame.draw.polygon(self.image, GREEN, [(0,38), (25,0), (50,38)])
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 7

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Bullet, self).__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        # Remove the bullet if it goes off screen
        if self.rect.bottom < 0:
            self.kill()

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.Surface((40, 30))
        self.image.fill(BLACK)
        pygame.draw.ellipse(self.image, RED, [0,0,40,30])
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-150, -40)
        self.speedy = random.randint(2, 6)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-150, -40)
            self.speedy = random.randint(2, 6)

def draw_text(surf, text, size, x, y, color=WHITE):
    font = pygame.font.SysFont("arial", size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def game_over_screen(score):
    screen.fill(BLACK)
    draw_text(screen, "GAME OVER", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4, RED)
    draw_text(screen, f"Score: {score}", 44, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text(screen, "Press any key to restart", 28, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP:
                waiting = False

def main():
    # Sprite groups
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    # Spawn initial enemies
    for _ in range(8):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    clock = pygame.time.Clock()
    score = 0
    running = True

    while running:
        clock.tick(60)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)

        keys = pygame.key.get_pressed()
        player.update(keys)

        all_sprites.update()

        # Check for bullet-enemy collisions
        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for hit in hits:
            score += 10
            # Spawn a new enemy for each hit
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)

        # Check for enemy-player collisions
        hits = pygame.sprite.spritecollide(player, enemies, False)
        if hits:
            game_over_screen(score)
            main()  # Restart game

        # Drawing
        screen.fill((10, 10, 30))  # Dark space background
        # Draw stars for atmosphere
        for i in range(50):
            pygame.draw.circle(screen, WHITE, (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)), 1)
        all_sprites.draw(screen)

        draw_text(screen, f"Score: {score}", 30, SCREEN_WIDTH // 2, 10)

        pygame.display.flip()

if __name__ == "__main__":
    main()

