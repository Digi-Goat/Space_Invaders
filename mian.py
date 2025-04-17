import pygame
import random

# Initialize pygame
pygame.init()

# Set display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load sounds
def load_sound(path):
    return pygame.mixer.Sound(path)

# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self, bullet_group):
        super().__init__()
        self.image = pygame.image.load("./assets/images/player_ship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH // 2
        self.rect.bottom = WINDOW_HEIGHT
        self.lives = 5
        self.velocity = 8
        self.bullet_group = bullet_group
        self.shoot_sound = load_sound("./assets/audio/player_fire.wav")

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity

    def fire(self):
        if len(self.bullet_group) < 2:
            self.shoot_sound.play()
            PlayerBullet(self.rect.centerx, self.rect.top, self.bullet_group)

    def reset(self):
        self.rect.centerx = WINDOW_WIDTH // 2


class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity, bullet_group):
        super().__init__()
        self.image = pygame.image.load("./assets/images/alien.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.starting_x = x
        self.starting_y = y
        self.direction = 1
        self.velocity = velocity
        self.bullet_group = bullet_group
        self.shoot_sound = load_sound("./assets/audio/alien_fire.wav")

    def update(self):
        self.rect.x += self.direction * self.velocity
        if random.randint(0, 1000) > 999 and len(self.bullet_group) < 3:
            self.shoot_sound.play()
            self.fire()

    def fire(self):
        AlienBullet(self.rect.centerx, self.rect.bottom, self.bullet_group)

    def reset(self):
        self.rect.topleft = (self.starting_x, self.starting_y)
        self.direction = 1


class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_group):
        super().__init__()
        self.image = pygame.image.load("./assets/images/green_laser.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.velocity = 10
        bullet_group.add(self)

    def update(self):
        self.rect.y -= self.velocity
        if self.rect.bottom < 0:
            self.kill()


class AlienBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_group):
        super().__init__()
        self.image = pygame.image.load("./assets/images/red_laser.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.velocity = 10
        bullet_group.add(self)

    def update(self):
        self.rect.y += self.velocity
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()


class Game:
    def __init__(self, player, alien_group, player_bullet_group, alien_bullet_group):
        self.round_number = 1
        self.score = 0
        self.player = player
        self.alien_group = alien_group
        self.player_bullet_group = player_bullet_group
        self.alien_bullet_group = alien_bullet_group

        self.new_round_sound = load_sound("./assets/audio/new_round.wav")
        self.breach_sound = load_sound("./assets/audio/breach.wav")
        self.alien_hit_sound = load_sound("./assets/audio/alien_hit.wav")
        self.player_hit_sound = load_sound("./assets/audio/player_hit.wav")

        self.font = pygame.font.Font("./assets/fonts/Facon.ttf", 32)

    def update(self):
        self.shift_aliens()
        self.check_collision()
        self.check_round_completion()

    def draw(self):
        score_text = self.font.render("Score: " + str(self.score), True, WHITE)
        round_text = self.font.render("Round: " + str(self.round_number), True, WHITE)
        lives_text = self.font.render("Lives: " + str(self.player.lives), True, WHITE)

        display_surface.blit(score_text, (WINDOW_WIDTH//2 - score_text.get_width()//2, 10))
        display_surface.blit(round_text, (20, 10))
        display_surface.blit(lives_text, (WINDOW_WIDTH - 150, 10))
        pygame.draw.line(display_surface, WHITE, (0, 50), (WINDOW_WIDTH, 50), 4)
        pygame.draw.line(display_surface, WHITE, (0, WINDOW_HEIGHT - 100), (WINDOW_WIDTH, WINDOW_HEIGHT - 100), 4)

    def shift_aliens(self):
        shift = False
        for alien in self.alien_group:
            if alien.rect.left <= 0 or alien.rect.right >= WINDOW_WIDTH:
                shift = True

        if shift:
            breach = False
            for alien in self.alien_group:
                alien.rect.y += 10 * self.round_number
                alien.direction *= -1
                alien.rect.x += alien.direction * alien.velocity
                if alien.rect.bottom >= WINDOW_HEIGHT - 100:
                    breach = True

            if breach:
                self.breach_sound.play()
                self.player.lives -= 1
                self.check_game_status("Aliens breached the line!", "Press 'Enter' to continue")

    def check_collision(self):
        if pygame.sprite.groupcollide(self.player_bullet_group, self.alien_group, True, True):
            self.alien_hit_sound.play()
            self.score += 100

        if pygame.sprite.spritecollide(self.player, self.alien_bullet_group, True):
            self.player_hit_sound.play()
            self.player.lives -= 1
            self.check_game_status("You've been hit!", "Press 'Enter' to continue")

    def check_round_completion(self):
        if not self.alien_group:
            self.score += 1000 * self.round_number
            self.round_number += 1
            self.start_new_round()

    def start_new_round(self):
        self.new_round_sound.play()
        for i in range(11):
            for j in range(5):
                x = 64 + i * 64
                y = 64 + j * 64
                velocity = self.round_number
                alien = Alien(x, y, velocity, self.alien_bullet_group)
                self.alien_group.add(alien)

    def check_game_status(self, main_text, sub_text):
        self.alien_bullet_group.empty()
        self.player_bullet_group.empty()
        self.player.reset()
        for alien in self.alien_group:
            alien.reset()

        if self.player.lives == 0:
            self.reset_game()
        else:
            self.pause_game(main_text, sub_text)

    def pause_game(self, main_text, sub_text):
        global running
        main = self.font.render(main_text, True, WHITE)
        main_rect = main.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
        sub = self.font.render(sub_text, True, WHITE)
        sub_rect = sub.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64))

        display_surface.fill(BLACK)
        display_surface.blit(main, main_rect)
        display_surface.blit(sub, sub_rect)
        pygame.display.update()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    def reset_game(self):
        self.pause_game(f"Final Score: {self.score}", "Press 'Enter' to play again")
        self.score = 0
        self.round_number = 1
        self.player.lives = 5
        self.alien_group.empty()
        self.alien_bullet_group.empty()
        self.player_bullet_group.empty()
        self.start_new_round()


# Main program
player_bullet_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
player = Player(player_bullet_group)
player_group = pygame.sprite.GroupSingle(player)
game = Game(player, alien_group, player_bullet_group, alien_bullet_group)
game.start_new_round()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.fire()

    display_surface.fill(BLACK)
    player_group.update()
    alien_group.update()
    player_bullet_group.update()
    alien_bullet_group.update()

    game.update()

    player_group.draw(display_surface)
    alien_group.draw(display_surface)
    player_bullet_group.draw(display_surface)
    alien_bullet_group.draw(display_surface)
    game.draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
