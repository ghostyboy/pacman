import pygame
from pygame.transform import scale2x

screen = pygame.display.set_mode((700,600))

spritesheet = pygame.image.load('msg.png')

clock = pygame.time.Clock()


#pallets for pacman (< * * * *

pellet_image = scale2x(spritesheet.subsurface(50,70,5,5))

class pellets:
    def __init__(self, forx, fory):
        self.x = 20
        self.y = 20
        self.image = pellet_image

pellet1 = pellets(50,100)
pellet2 = pellets(70,100)
        

xpad = 4
pacman_right = spritesheet.subsurface(473,0,15,15)
screen.blit(pacman_right,(20,400))
pacman_left = spritesheet.subsurface(473,16,15,15)
screen.blit(pacman_left,(40,400))
screen.blit(pacman_right,(60,400))
pacman_up = spritesheet.subsurface(473,32,15,15)
screen.blit(pacman_up,(80,400))
pacman = pacman_right
pacman_down = (spritesheet.subsurface(680/3*2+xpad,48,16,16))
#pacman_wall = scale2x(spritesheet.subsurface(56,120,15,40))
wall_rect = pygame.Rect(261,414,15,40)
pallets = spriteet.subsurface(200, 100, 15, 15)


#pacman.spawnpoint
pacman_x = 300
pacman_y = 300


def get_pacman_rect(px, py):
    return pygame.Rect(px,py, 16, 16)


pacman_direction = None


speed = 3

moving = False
running = True
while running:
    pygame.display.update()
    clock.tick(30)
 
    screen.fill((0,0,0))
   # screen.blit(spritesheet,(0,0))
    #screen.blit(pacman_wall,(250,400))
    screen.blit(pacman,(pacman_x,pacman_y))
    
  
        
    if moving:
        #use this in case you need the pacman coordinates
      #  print "px: %i py: %i" % (pacman_x, pacman_y)
       # print "wall_rec: %s" % wall_rect
        if pacman_direction == 'down':
           pacman = pacman_down
           pacman_y += speed
        if pacman_direction =='up':
           pacman = pacman_up
           pacman_y -= speed
        if pacman_direction == 'left':
           pacman = pacman_left
           pacman_x -= speed
        if pacman_direction == 'right':
           pacman = pacman_right
           pacman_x += speed

       # if wall_rect.colliderect (get_pacman_rect(pacman_x, pacman_y)): 
         #   print "collide"
          #  moving = False
        
   
    for e in pygame.event.get():
        if e.type ==pygame.QUIT:
            running = True
            pygame.quit()
        if e.type == pygame.KEYUP:
            moving = False

        if e.type == pygame.KEYDOWN:
            moving = True
            kname = pygame.key.name(e.key)
            print kname
            pacman_direction = kname
            

   


    

    
    

