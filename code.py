# Шаг 1
import random
import pygame

#Шаг 2
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

player = pygame.image.load("hero.png")
player = pygame.transform.scale(player, (35, 50))
player_rect = player.get_rect()
player_rect.x = 320
player_rect.y = 240

back = pygame.image.load("background.png")
back = pygame.transform.scale(back, (640, 480))

win = pygame.image.load("win.png")
win = pygame.transform.scale(win, (640, 480))

dumpling = pygame.image.load("dumpling.png")
dumpling = pygame.transform.scale(dumpling, (50, 50))
dumpling_rect = dumpling.get_rect()
dumpling_rect.x = 120
dumpling_rect.y = 240

dumplings = 0

speedx = 0
speedy = 0
flip = False
#Шаг 3
running = True

start_ticks = pygame.time.get_ticks()

#Шаг 4
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speedx = -5
                flip = False
            if event.key == pygame.K_RIGHT:
                speedx = 5
                flip = True
            if event.key == pygame.K_UP:
                speedy = -5
            if event.key == pygame.K_DOWN:
                speedy = 5
            if event.key == pygame.K_r:
                dumplings = 0
                dumpling_rect.x = 120
                dumpling_rect.y = 240
                player_rect.x = 320
                player_rect.y = 240
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speedx = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speedy = 0
        if event.type == pygame.QUIT:
            running = False
    screen.blit(back, (0, 0))
    player_rect.x += speedx
    player_rect.y += speedy
    if flip == True:
        screen.blit(player, player_rect)
    else:
        screen.blit(pygame.transform.flip(player, True, False), player_rect)
    if player_rect.colliderect(dumpling_rect):
        dumpling_rect.x = random.randint(0, 590)
        dumpling_rect.y = random.randint(0, 430)
        dumplings += 1
    screen.blit(dumpling, dumpling_rect)

    f1 = pygame.font.Font(None, 36)
    text1 = f1.render(f'Пельмени: {dumplings}', True,
                      (180, 0, 0))
    screen.blit(text1, (10, 10))

    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    if seconds > 3:
        dumpling_rect.x = random.randint(0, 590)
        dumpling_rect.y = random.randint(0, 430)
        start_ticks = pygame.time.get_ticks()
    if dumplings >= 3:
        screen.blit(win, (0, 0))

    pygame.display.flip()
    clock.tick(30)