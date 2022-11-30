import pygame

pygame.init()


clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
            if event.key == pygame.K_RIGHT:
                x += 10
            if event.key == pygame.K_UP:
                y -= 10
            if event.key == pygame.K_DOWN:
                y += 10
    
    
    pygame.display.flip()