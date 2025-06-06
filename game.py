import pygame
import sys
import os
os.chdir(os.path.dirname(__file__))

pygame.init()

userx = 400
usery = 400
tile_boyut = 100

programIcon = pygame.image.load('images/walk.png')
pygame.display.set_icon(programIcon)

harita = [
    [0, 0, 1, 1, 1, 0, 2, 1],
    [0, 2, 2, 1, 1, 1, 2, 2],
    [1, 2, 0, 0, 1, 2, 2, 2],
    [1, 1, 0, 0, 0, 0, 2, 1],
    [0, 0, 1, 1, 1, 0, 2, 1],
    [0, 2, 2, 1, 1, 1, 2, 2],
    [1, 2, 0, 0, 1, 2, 2, 2],
    [1, 1, 0, 0, 0, 0, 2, 1],
]

adam = pygame.image.load("images/man.png")
adam = pygame.transform.scale(adam, (50, 50))

pygame.mixer.init()
yuru_sesi = pygame.mixer.Sound("sounds/yurume.wav")
yuru_sesi.set_volume(0.2)

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Düzgün kod")
saat = pygame.time.Clock()
running = True
ses_calıyor = False

while running:
    hareket_edildi = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        userx += 5
        hareket_edildi = True
    if keys[pygame.K_a]:
        userx -= 5
        hareket_edildi = True
    if keys[pygame.K_w]:
        usery -= 5
        hareket_edildi = True
    if keys[pygame.K_s]:
        usery += 5
        hareket_edildi = True

    userx = max(0, min(userx, 800 - 50))
    usery = max(0, min(usery, 800 - 50))

    if hareket_edildi:
        if not ses_calıyor:
            yuru_sesi.play(-1)
            ses_calıyor = True
    else:
        if ses_calıyor:
            yuru_sesi.stop()
            ses_calıyor = False

    screen.fill((255, 255, 255))
    for y in range(len(harita)):
        for x in range(len(harita[0])):
            tile = harita[y][x]
            if tile == 0:
                renk = (34, 177, 76)
            elif tile == 1:
                renk = (120, 120, 120)
            elif tile == 2:
                renk = (0, 162, 232)
            pygame.draw.rect(screen, renk, (x * tile_boyut, y * tile_boyut, tile_boyut, tile_boyut))

    screen.blit(adam, (userx, usery))
    pygame.display.flip()
    saat.tick(60)

pygame.quit()
sys.exit()
