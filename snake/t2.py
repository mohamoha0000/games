import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

class Body:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

class SnakePlayer:
    def __init__(self, x, y, n, size):
        self.bodys = []
        self.size = size
        
        # Directions: (x, y) - Start not moving
        self.x_dir = 0
        self.y_dir = 0
        
        # Timer for movement speed (Snake shouldn't move 60 times a second)
        self.move_timer = 0
        self.move_delay = 100 # Milliseconds between moves

        # Create body parts (Head is at index 0)
        for i in range(n):
            # Create segments side by side
            self.bodys.append(Body(x - (i * size), y, size, size, (255, 0, 0)))

    def input(self):
        keys = pygame.key.get_pressed()
        
        # Prevent reversing direction directly (can't go Left if going Right)
        if keys[pygame.K_d] and self.x_dir != -1: # Right
            self.x_dir = 1
            self.y_dir = 0
        elif keys[pygame.K_a] and self.x_dir != 1: # Left
            self.x_dir = -1
            self.y_dir = 0
        elif keys[pygame.K_w] and self.y_dir != 1: # Up
            self.y_dir = -1
            self.x_dir = 0
        elif keys[pygame.K_s] and self.y_dir != -1: # Down
            self.y_dir = 1
            self.x_dir = 0

    def update(self):
        # We use a timer to slow down the snake so it moves on a "grid"
        current_time = pygame.time.get_ticks()
        
        if current_time - self.move_timer > self.move_delay:
            self.move_timer = current_time
            
            # Only move if we have a direction
            if self.x_dir != 0 or self.y_dir != 0:
                
                # 1. Move the body segments (Follow the leader)
                # Loop backwards from the tail up to the head
                for i in range(len(self.bodys) - 1, 0, -1):
                    self.bodys[i].x = self.bodys[i-1].x
                    self.bodys[i].y = self.bodys[i-1].y

                # 2. Move the Head
                self.bodys[0].x += self.x_dir * self.size
                self.bodys[0].y += self.y_dir * self.size

    def draw(self):
        for part in self.bodys:
            part.draw()

# Initialize Snake at specific coordinates
snack = SnakePlayer(200, 200, 5, 50)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    snack.input()
    snack.update() # Replaced fps() with update()
    snack.draw()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()