import pygame

pygame.init()

Screen = pygame.display.set_mode((500,600))

GREY = (150,150,150)
WHITE = (255,255,255)

running  = True

while running:
    Screen.fill(GREY)
    
    pygame.draw.rect(Screen, WHITE, (100,50,50,50))
    pygame.draw.rect(Screen, WHITE, (300,50,150,50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = false

    pygame.display.flip()
 
pygame.quit()
