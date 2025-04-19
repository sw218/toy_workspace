
import pygame
import random
import sys
import os

# 화면 크기 설정
WIDTH, HEIGHT = 800, 600

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ROYAL_BLUE = (65, 105, 225)
ORANGE = (255, 165, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Dodger")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

# PyInstaller 대응 경로 처리 함수
def get_base_path():
    if getattr(sys, 'frozen', False):
        return sys.executable
    return os.path.dirname(os.path.abspath(__file__))

def asset_path(filename):
    return os.path.join(get_base_path(), 'GameAssets', filename)

# 이미지 불러오기
player_img = pygame.image.load(asset_path("player.png"))
enemy_img = pygame.image.load(asset_path("enemy.png"))
obstacle_img = pygame.image.load(asset_path("obstacle.png"))

# 클래스 정의
class Player:
    def __init__(self):
        self.image = pygame.transform.scale(player_img, (50, 50))
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Obstacle:
    def __init__(self):
        self.image = pygame.transform.scale(obstacle_img, (40, 40))
        self.rect = self.image.get_rect(topleft=(random.randint(0, WIDTH - 40), -40))
        self.speed = random.randint(3, 7)

    def move(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# 씬 구조 정의
class SceneBase:
    def __init__(self):
        self.next = self

    def process_input(self, events, keys): pass
    def update(self): pass
    def render(self, screen): pass
    def switch_to_scene(self, next_scene): self.next = next_scene
    def terminate(self): self.switch_to_scene(None)

class TitleScene(SceneBase):
    def render(self, screen):
        screen.fill(WHITE)
        title = font.render("FALLING DODGER", True, ROYAL_BLUE)
        prompt = font.render("Press SPACE to Start", True, BLACK)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - 80))
        screen.blit(prompt, (WIDTH//2 - prompt.get_width()//2, HEIGHT//2))

    def process_input(self, events, keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.switch_to_scene(GameScene())

class GameScene(SceneBase):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.obstacles = []
        self.spawn_timer = 0

    def process_input(self, events, keys):
        self.player.move(keys)

    def update(self):
        self.spawn_timer += 1
        if self.spawn_timer > 30:
            self.spawn_timer = 0
            self.obstacles.append(Obstacle())

        for obs in self.obstacles:
            obs.move()

        for obs in self.obstacles:
            if self.player.rect.colliderect(obs.rect):
                self.switch_to_scene(GameOverScene())

        self.obstacles = [obs for obs in self.obstacles if obs.rect.top < HEIGHT]

    def render(self, screen):
        screen.fill(WHITE)
        self.player.draw(screen)
        for obs in self.obstacles:
            obs.draw(screen)

class GameOverScene(SceneBase):
    def render(self, screen):
        screen.fill(WHITE)
        gameover = font.render("GAME OVER", True, ORANGE)
        prompt = font.render("Press R to Restart", True, BLACK)
        screen.blit(gameover, (WIDTH//2 - gameover.get_width()//2, HEIGHT//2 - 80))
        screen.blit(prompt, (WIDTH//2 - prompt.get_width()//2, HEIGHT//2))

    def process_input(self, events, keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.switch_to_scene(TitleScene())

# 메인 루프
def run_game(starting_scene):
    current_scene = starting_scene

    while current_scene is not None:
        events = pygame.event.get()
        keys = pygame.key.get_pressed()

        for event in events:
            if event.type == pygame.QUIT:
                current_scene.terminate()

        current_scene.process_input(events, keys)
        current_scene.update()
        current_scene.render(screen)

        current_scene = current_scene.next

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run_game(TitleScene())
