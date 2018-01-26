import pygame

screen = pygame.display.set_mode((700,700))

spritesheet = pygame.image.load('msg.png')

screen.blit(spritesheet,(0,0))


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
pacman_direction = None

pacman_x = 300
pacman_y = 300

speed = 1

moving = False
running = True
while running:
    screen.fill((0,0,0))

    screen.blit(pacman,(pacman_x,pacman_y))

    if moving:
        if pacman_direction == 'down':
           pacman = pacman_down
           pacman_y += 0.1
        if pacman_direction =='up':
           pacman = pacman_up
           pacman_y -= 0.1
        if pacman_direction == 'left':
           pacman = pacman_left
           pacman_x -= 0.1
        if pacman_direction == 'right':
           pacman = pacman_right
           pacman_x += 0.1
   
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




pygame.display.update()










            

