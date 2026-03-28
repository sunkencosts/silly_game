# Example file showing a circle moving on screen
import pygame

def check_collision(circle_rects, wall_rects)->bool:
    for cr in circle_rects:
        for wr in wall_rects:
            if cr.colliderect(wr):
                return True
    return False

def get_circle_rects(player_pos, count):
    rects = []
    for i in range(count):
        x = player_pos.x + (i*100)
        y = player_pos.y + (i*100)
        rects.append(pygame.Rect(x-10,y-10,20,20))
    return rects    

class Explosion:
    DURATION = 0.2 #seconds
   
    def __init__(self, postition:pygame.Vector2 ):
        self.position = pygame.Vector2(postition)
        self.elapsed = 0
        self.color = "orange"
        
    
    def is_dead(self):
        return self.elapsed >= self.DURATION 
    def update(self, dt):
        self.elapsed += dt
    def get_radius(self):
        progress = self.elapsed / self.DURATION
        return int(progress * 80)
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color,self.position, self.get_radius())
   
    
    

# pygame setup
pygame.init()

screen = pygame.display.set_mode((500, 720))
clock = pygame.time.Clock()
running = True
dt = 0
SPEED = 300
pygame.display.set_caption("Silly Game")
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
count = 3
wall_rects = [pygame.Rect(100 * i, 100, 50, 25) for i in range (10)]
explosions = []
space_was_pressed = False
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print(f"Key pressed: {event.unicode}, {pygame.key.name(event.key)}")

    keys = pygame.key.get_pressed()
    
    new_pos = pygame.Vector2(player_pos)
    if keys[pygame.K_a]:
        new_pos.x -= SPEED * dt
    if keys[pygame.K_d]:
        new_pos.x += SPEED * dt 
    
    if not check_collision(get_circle_rects(new_pos, count), wall_rects):
        player_pos.x = new_pos.x
    
    new_pos = pygame.Vector2(player_pos)
    if keys[pygame.K_w]:
        new_pos.y -= SPEED * dt
    if keys[pygame.K_s]:
        new_pos.y += SPEED * dt
    if not check_collision(get_circle_rects(new_pos, count), wall_rects):
        player_pos.y = new_pos.y
    
    if keys[pygame.K_SPACE] and not space_was_pressed:
        explosions.append(Explosion(player_pos))
    space_was_pressed = keys[pygame.K_SPACE]
        
    for explosion in explosions:
        explosion.update(dt)
    explosions = [e for e in explosions if not e.is_dead()]
    
    # Draw after know positions
    # fill the screen with a color to wipe away anything from last frame

    screen.fill("black")
    

    for i in range(count):
        draw_vector =  pygame.Vector2(player_pos.x + (i*100), player_pos.y + (i*100))
        pygame.draw.circle(screen, "red", draw_vector, 10)
    
    for rect in wall_rects:
        pygame.draw.rect(screen, "white", rect)
    
    for explosion in explosions:
        explosion.draw(screen)
        

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000




pygame.quit()