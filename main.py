import random
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("PoGo game")
clock = pygame.time.Clock()

start_ticks = pygame.time.get_ticks()
time_start = pygame.time.get_ticks()

flip = False

speedx = 0
speedy = 0

backg = pygame.image.load("background.png")
backg = pygame.transform.scale(backg, (640, 480))

uWin = pygame.image.load("win.png")
uWin = pygame.transform.scale(uWin, (640, 480))

player = pygame.image.load("hero.png")
player = pygame.transform.scale(player, (100, 80))

player_rect = player.get_rect()
player_rect.x = 10
player_rect.y = 10

pinep = pygame.image.load("dumpling.png")
pinep = pygame.transform.scale(pinep, (40, 50))

pinep_rect = player.get_rect()
pinep_rect.x = 100
pinep_rect.y = 100
pineps = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                speedx = 5
            if event.key == pygame.K_a:
                speedx = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                speedx = 0
                flip = False
            if event.key == pygame.K_a:
                speedx = 0
                flip = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                speedy = -5
            if event.key == pygame.K_s:
                speedy = 5
            if event.key == pygame.K_r:
                pineps = 0
                pinep_rect.x = 120
                pinep_rect.y = 240
                player_rect.x = 320
                player_rect.y = 240
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                speedy = 0
            if event.key == pygame.K_s:
                speedy = 0
    player_rect.x += speedx
    player_rect.y += speedy
    screen.blit(backg, (0, 0))
    screen.blit(pinep, pinep_rect)
    if player_rect.colliderect(pinep_rect):
        pinep_rect.x = random.randint(0, 590)
        pinep_rect.y = random.randint(0, 430)
        pineps += 1

    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    if seconds >= 4:
        pinep_rect.x = random.randint(0, 590)
        pinep_rect.y = random.randint(0, 430)
        start_ticks = pygame.time.get_ticks()

    seconds_to_lose = (pygame.time.get_ticks() - time_start) / 1000
    if seconds_to_lose >= 15 and pineps < 10:
        running = False

    if flip == True:
        screen.blit(pygame.transform.flip(player, True, False), player_rect)
    else:
        screen.blit(player, player_rect)

    f1 = pygame.font.Font(None, 36)
    text1 = f1.render(f'Ананасов: {pineps}', True,
                      (180, 0, 0))
    screen.blit(text1, (10, 10))

    text2 = f1.render(f'Времени до провала: {int(15 - seconds_to_lose)}!', True,
                      (180, 0, 0))
    screen.blit(text2, (10, 30))

    if pineps >= 10:
        screen.blit(uWin, (0, 0))

    pygame.display.flip()
    clock.tick(30)