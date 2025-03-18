import pygame, random

#Intialize pygame
pygame.init()

#Set Display Surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
display_surface = pygame.display.set_mode(size)

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()


class Game:
    """A class to help control and update gameplay"""

    def __init__(self, player, alien_group, player_bullet_group, alien_bullet_group):
        """Initialize the game"""
        #Set game values
        self.round_number = 1
        self.score = 0
        self.player = player
        self.alien_group = alien_group
        self.player_bullet_group = player_bullet_group
        self.alien_bullet_group = alien_bullet_group

        #Set sounds and music
        self.new_round_sound = pygame.mixer.Sound("./assets/new_round.wav")
        self.beach_sound = pygame.mixer.Sound("./assets/breach.wav")
        self.alien_hit_sound = pygame.mixer.Sound("./assets/alien_hit.wav")
        self.player_hit_sound = pygame.mixer.Sound("./assets/player_hit.wav")

        #Set font
        self.font = pygame.font.Font("./assets/fonts/Facon.ttf", 32)

    def update(self):
        """Update the game"""
        # TODO: 3/13/2025: call self.shift_aliens()
        # TODO: 3/13/2025: call self.check_collisions()
        # TODO: 3/13/2025: call self.check_round_completion()

    def draw(self):
        """Draw the HUD and other information to display"""
        # Set colors
        # TODO: 3/13/2025: add all of this code to draw.  Tis a freebie.
        WHITE = (255, 255, 255)

        # Set text
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

        # Blit the HUD to the display
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
        # See if any bullet in the player bullet group hit an alien in the alien group

        # TODO: 3/13/2025 check if pygame.spite.groupcollide() is true
        #  passing in self.player_bullet_group, self.alien_group, True, and True into the method
        if pygame.sprite.groupcollide():  # don't forget to pass in args

    # TODO: 3/13/2025 call self.alien_hit_sound's play method
    # TODO: 3/13/2025 add 100 to self.score

    # See if the player has collided with any bullet in the alien bullet group
    # TODO: 3/13/2025 check if pygame.sprite.spritecollide is true passing in self.player, self.alien_bullet_group, True
    # beginning of the if block.  Please tab
    # TODO: 3/13/2025 call self.player_hit_sound's play method
    # TODO: 3/13/2025 subtract 1 from self.player.lives
    # TODO: 3/13/2025 call self.check_game_status passing in "You've been hit!", "Press 'Enter' to continue"
    # end of if block. back tab.

    def check_round_completion(self):
        """Check to see if a player has completed a single round"""
        # If the alien group is empty, you've completed the round
        # TODO: 3/13/2025: check if not self.alien_group
        if not self.alien_group:

    # if block begin
    # TODO: 3/13/2025: add 1000 * self.round_number to self.score
    # TODO: 3/13/2025: add 1 to self.round_number
    # TODO: 3/13/2025: call self's start_new_round method
    # end of if block

    def start_new_round(self):
        """Start a new round"""
        ...  # TODO: we will do this one later.

    def check_game_status(self, main_text, sub_text):
        """Check to see the status of the game and how the player died"""
        # Empty the bullet groups and reset player and remaining aliens
        # TODO: 3/13/2025: call self.alien_bullet_group's empty method
        # TODO: 3/13/2025: call self.player_bullet_group's empty method
        # TODO: 3/13/2025: call self.player's reset method
        for alien in self.alien_group:

    # inside the for loop
    # TODO: 3/13/2025: call alien's reset method
    # done with the for loop

    # Check if the game is over or if it is a simple round reset
    # TODO: 3/13/2025: if else statement here
    # check if self.player.lives is equal to 0.  Hint Hint == operator
    # when the condition is true call self.reset_game()
    # else
    # when the condition is false (else) call self.pause_game(main_text, sub_text)

    def pause_game(self, main_text, sub_text):
        """Pauses the game"""
        ...  # TODO: we will do this one later.

    def reset_game(self):
        """Reset the game"""
        # TODO: 3/13/2025: call self.pause_game passing in "Final Score: " + str(self.score)
        #  and "Press 'Enter' to play again"

        # Reset game values
        # TODO: 3/13/2025: set the following self variables
        # TODO: 3/13/2025: score to 0, round_number to 1, player.lives to 5

        # Empty groups
        # TODO: 3/13/2025: call the following self methods
        # TODO: 3/13/2025: alien_group.empty, alien_bullet_group.empty, player_bullet_group.empty

        # Start a new game
        self.start_new_round()

    class Player(pygame.sprite.Sprite):
        """A class to model a spaceship the user can control"""

        def __init__(self, bullet_group):
            """Initialize the player"""
            super().__init__()
            # TODO: (3/11/2025) assign to self.image the image loaded from "player_ship.png"
            # TODO: (3/11/2025) assign to self.rect the rect from the image
            # TODO: (3/11/2025) assign to self.rect.centerx the value of half of the WINDOW_WIDTH use //
            # TODO: (3/11/2025) assign to self.rect.bottom the WINDOW_HEIGHT

            # TODO: (3/11/2025) assign to self.lives the value of 5
            # TODO: (3/11/2025) assign to self.velocity the value 8

            # TODO: (3/11/2025) assign self.bullet_group appropriately

            # TODO: (3/11/2025) assign to self.shoot_sound the sound loaded from player_fire.wav

        def update(self):
            """Update the player"""
            keys = pygame.key.get_pressed()

            # Move the player within the bounds of the screen
            if keys[pygame.K_LEFT] and self.rect.left > 0:

        # TODO: (3/11/2025) subtract self.velocity from self.rect.x
        # TODO: (3/11/2025) handle pressing K_RIGHT similarly to K_LEFT

        def fire(self):
            """Fire a bullet"""
            # Restrict the number of bullets on screen at a time
            if len(self.bullet_group) < 2:

        # TODO: (3/11/2025) call self.shoot_sound's play method.
        # TODO: (3/11/2025) create  PlayerBullet passing in self.rect.centerx, self.rect.top, self.bullet_group

        def reset(self):
            """Reset the players position"""
            # TODO: (3/11/2025) assign half of the window width using // to self.rect.centerx

    class Alien(pygame.sprite.Sprite):
        """A class to model an enemy alien"""

        def __init__(self, x, y, velocity, bullet_group):
            """Initialize the alien"""
            super().__init__()
            # TODO: (3/11/2025) assign to self.image an image loaded from alien.png
            # TODO: (3/11/2025) assign to self.rect the rect from the self.image
            # TODO: (3/11/2025) assign to self.rect.topleft the tuple (x, y)

            # TODO: (3/11/2025) assign to self.starting_x the value of x
            # TODO: (3/11/2025) repeat for starting_y appropriately.

            # TODO: (3/11/2025) assign to self.direction the value of 1
            # TODO: (3/11/2025) assign to self.velocity the value of velocity

            # EXAMPLE:  assign 3 to x means:  x = 3
            # EXAMPLE:  assign to x the value of 3 means x = 3

            # TODO: (3/11/2025) assign to self.bullet_group the bullet_group

            # TODO: (3/11/2025) assign to self.shoot_sound the value of pygame.mixer.Sound()
            # TODO: (3/11/2025) (cont.) the sound from the assets folder alien_fire.wav

        def update(self):
            """Update the alien"""
            # Example:  add to x the value of 3
            # Example:  x += 3
            # TODO: (3/11/2025) add to self.rect.x the value of direction * velocity.  (Don't forget self

            # Randomly fire a bullet
            if random.randint(0, 1000) > 999 and len(self.bullet_group) < 3:
                self.shoot_sound.play()
                self.fire()

        def fire(self):
            """Fire a bullet"""
            AlienBullet(self.rect.centerx, self.rect.bottom, self.bullet_group)

        def reset(self):
            """Reset the alien position"""
            # TODO: (3/11/2025) assign to self.rect.topleft the tuple (self.starting_x, self.starting_y)
            # TODO: (3/11/2025) assign to self.direction the value of 1

    class PlayerBullet(pygame.sprite.Sprite):
        """A class to model a bullet fired by the player"""

        def __init__(self, x, y, bullet_group):
            """Initialize the bullet"""
            super().__init__()
            self.image = pygame.image.load("./assets/images/green_laser.png")
            self.rect = self.image.get_rect()
            # TODO: (3/11/2025) assign x to self.rect.centerx
            # TODO: (3/11/2025) do the same for centery

            # TODO: (3/11/2025) assign 10 to self.velocity
            # TODO: (3/11/2025) call bullet_group's add method and pass in self.

        def update(self):
            """Update the bullet"""
            # TODO: (3/11/2025) subtract self.velocity from self.rect.y:
            # TODO: (3/11/2025) check if self.rect.bottom is less than 0.
            # TODO: (3/11/2025) the if block will then kill the sprite.

    class AlienBullet(pygame.sprite.Sprite):
        """A class to model a bullet fired by the alien"""

        def __init__(self, x, y, bullet_group):
            """Initialize the bullet"""
            super().__init__()
            self.image = pygame.image.load("./assets/images/red_laser.png")
            self.rect = self.image.get_rect()

            # TODO: (3/11/2025) assign x to self.rect.centerx
            # TODO: (3/11/2025) do the same for centery

            # TODO: (3/11/2025) assign 10 to self.velocity
            # TODO: (3/11/2025) call bullet_group's add method and pass in self.

        def update(self):
            """Update the bullet"""
            # TODO: (3/11/2025) add self.velocity to self.rect.y:  Hint Hint:  +=

            if self.rect.top > WINDOW_HEIGHT:
                self.kill()

    # Create bullet groups
    my_player_bullet_group = pygame.sprite.Group()
    # TODO: repeat for my_alien_bullet_group

    # Create a player group and Player object
    my_player_group = pygame.sprite.Group()
    my_player = Player(my_player_bullet_group)
    my_player_group.add(my_player)

    # Create an alien group.  Will add Alien objects via the game's start new round method
    # TODO: create my_alien_group

    # Create the Game object
    my_game = Game(my_player, my_alien_group, my_player_bullet_group, my_alien_bullet_group)
    my_game.start_new_round()

    # The main game loop
    running = True
    while running:
        # Check to see if the user wants to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # The player wants to fire
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    my_player.fire()

        # Fill the display
        display_surface.fill((0, 0, 0))

        # Update and display all sprite groups
        my_player_group.update()
        my_player_group.draw(display_surface)

        my_alien_group.update()
        my_alien_group.draw(display_surface)

        my_player_bullet_group.update()
        my_player_bullet_group.draw(display_surface)

        my_alien_bullet_group.update()
        my_alien_bullet_group.draw(display_surface)

        # Update and draw Game object
        my_game.update()
        my_game.draw()

        # Update the display and tick clock
        pygame.display.update()
        clock.tick(FPS)

    # End the game
    pygame.quit()