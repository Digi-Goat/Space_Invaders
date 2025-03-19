import pygame, random

# Initialize pygame
pygame.init()

# Set Display Surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
display_surface = pygame.display.set_mode(size)

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

class Game:
    """A class to help control and update gameplay"""

    def __init__(self, player, alien_group, player_bullet_group, alien_bullet_group):
        """Initialize the game"""
        self.round_number = 1
        self.score = 0
        self.player = player
        self.alien_group = alien_group
        self.player_bullet_group = player_bullet_group
        self.alien_bullet_group = alien_bullet_group

        self.new_round_sound = pygame.mixer.Sound("./assets/new_round.wav")
        self.beach_sound = pygame.mixer.Sound("./assets/breach.wav")
        self.alien_hit_sound = pygame.mixer.Sound("./assets/alien_hit.wav")
        self.player_hit_sound = pygame.mixer.Sound("./assets/player_hit.wav")

        self.font = pygame.font.Font("./assets/fonts/Facon.ttf", 32)

    def update(self):
        self.shift_aliens()
        self.check_collision()
        self.check_round_completion()

    def draw(self):
        WHITE = (255, 255, 255)
        score_text = self.font.render("Score: " + str(self.score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.centerx = WINDOW_WIDTH // 2
        score_rect.top = 10

        round_text = self.font.render("Round: " + str(self.round_number), True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topleft = (20, 10)

        lives_text = self.font.render("Lives: " + str(self.player.lives), True, WHITE)
        lives_rect = lives_text.get_rect()
        lives_rect.topright = (WINDOW_WIDTH - 20, 10)

        display_surface.blit(score_text, score_rect)
        display_surface.blit(round_text, round_rect)
        display_surface.blit(lives_text, lives_rect)
        pygame.draw.line(display_surface, WHITE, (0, 50), (WINDOW_WIDTH, 50), 4)
        pygame.draw.line(display_surface, WHITE, (0, WINDOW_HEIGHT - 100), (WINDOW_WIDTH, WINDOW_HEIGHT - 100), 4)

    def shift_aliens(self):
        """Shift a wave of aliens down the screen and reverse direction"""
        ...  # TODO: we will do this one later.

    def check_collision(self):
        """Check for collisions"""
        if pygame.sprite.groupcollide(self.player_bullet_group, self.alien_group, True, True):
            self.alien_hit_sound.play()
            self.score += 100

        if pygame.sprite.spritecollide(self.player, self.alien_bullet_group, True):
            self.player_hit_sound.play()
            self.player.lives -= 1
            self.check_game_status("You've been hit!", "Press 'Enter' to continue")

    def check_round_completion(self):
        """Check to see if a player has completed a single round"""
        if not self.alien_group:
            self.score += 1000 * self.round_number
            self.round_number += 1
            self.start_new_round()

    def start_new_round(self):
        """Start a new round"""
        ...  # TODO: we will do this one later.

    def check_game_status(self, main_text, sub_text):
        """Check to see the status of the game and how the player died"""
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
        """Pauses the game"""
        ...  # TODO: we will do this one later.

    def reset_game(self):
        """Reset the game"""
        self.pause_game("Final Score: " + str(self.score), "Press 'Enter' to play again")
        self.score = 0
        self.round_number = 1
        self.player.lives = 5
        self.alien_group.empty()
        self.alien_bullet_group.empty()
        self.player_bullet_group.empty()
        self.start_new_round()

# TxODO: Add all remaining class definitions here, keeping placeholders where necessary.

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.fire()

    display_surface.fill((0, 0, 0))

    my_player_group.update()
    my_player_group.draw(display_surface)

    my_alien_group.update()
    my_alien_group.draw(display_surface)

    my_player_bullet_group.update()
    my_player_bullet_group.draw(display_surface)

    my_alien_bullet_group.update()
    my_alien_bullet_group.draw(display_surface)

    my_game.update()
    my_game.draw()

    pygame.display.update()
    clock.tick(FPS)
