import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

class body:
    def __init__(self,x,y,width,height,color):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color
    def draw(self):
        pygame.draw.rect(screen,self.color, (self.x,self.y,self.width,self.height))
    def move(self,x,y):
        self.x=x
        self.y=y
class playerClass:
    def __init__(self,x,y,n,size):
        self.bodys=[]
        self.x=x
        self.y=y
        self.n=n
        self.size=size
        self.x_dir = 1
        self.y_dir = 0
        self.move_timer = 0
        self.move_delay = 10
        self.speed=4
        for i in range(n):
            self.bodys.append(body(i*self.size,self.y,self.size,self.size,(255,0,0)))
    
    def draw(self):
        for i in self.bodys:
            i.draw()
    def input(self):
        keys = pygame.key.get_pressed()
        
        # Prevent reversing direction directly (can't go Left if going Right)
        if keys[pygame.K_d] and self.x_dir != -1: # Right
            self.x_dir = 1
            
        if keys[pygame.K_a] and self.x_dir != 1: # Left
            self.x_dir = -1
        if keys[pygame.K_w] and self.y_dir != 1: # Up
            self.y_dir = -1
        if keys[pygame.K_s] and self.y_dir != -1: # Down
            self.y_dir = 1

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
                print(self.x_dir,self.y_dir)
                self.bodys[0].x += self.x_dir * (self.size/4)
                self.bodys[0].y += self.y_dir * (self.size/4)
                self.x_dir = 0
                self.y_dir = 0
snack=playerClass(0,0,5,50)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    snack.draw()
    snack.input()
    snack.update()
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()