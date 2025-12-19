import pygame 
pygame.init()
clock = pygame.time.Clock()

dis = pygame.display.set_mode((1000, 400))
pygame.display.set_caption("Bandits")
icon = pygame.image.load('icon/icon.my_2d.game.png')
pygame.display.set_icon(icon)

fon = pygame.image.load('image/vecteezy_parallax-background-with-destroyed-city-street_14320066.jpg')

fon_x = 0
fon_speed = 2

player_img = [
    pygame.image.load('image/photo_2025-12-18_20-09-54.png'),
    pygame.image.load('image/photo_2025-12-18_20-09-54 (2).png'),
    pygame.image.load('image/photo_2025-12-18_20-09-54 (3).png'),
    pygame.image.load('image/photo_2025-12-18_20-09-54 (4).png'),
    pygame.image.load('image/photo_2025-12-18_20-09-54 (5).png'),
    pygame.image.load('image/photo_2025-12-18_20-09-54.png'),
    pygame.image.load('image/photo_2025-12-18_20-09-54 (2).png'),
    pygame.image.load('image/photo_2025-12-18_20-09-54 (3).png')
]
player_count = 0
player_x = 100
player_y = 250

enemy2 = [
    pygame.image.load('enemy2/бандит2/2бандит1.png'),
    pygame.image.load('enemy2/бандит2/2бандит2.png'),
    pygame.image.load('enemy2/бандит2/2бандит3.png'),
    pygame.image.load('enemy2/бандит2/2бандит4.png'),
    pygame.image.load('enemy2/бандит2/2бандит5.png'),
    pygame.image.load('enemy2/бандит2/2бандит6.png'),
    pygame.image.load('enemy2/бандит2/2бандит7.png'),
    pygame.image.load('enemy2/бандит2/2бандит8.png'),
    pygame.image.load('enemy2/бандит2/2бандит9.png'),
    pygame.image.load('enemy2/бандит2/2бандит10.png'),
    pygame.image.load('enemy2/бандит2/2бандит11.png'),
    pygame.image.load('enemy2/бандит2/2бандит12.png'),
    pygame.image.load('enemy2/бандит2/2бандит1.png'),
]
enemy2_count = 0
enemy2_x = 800
enemy2_y = 250

enemy = [
    pygame.image.load('enemy/бандит/бандит1.png'),
    pygame.image.load('enemy/бандит/бандит2.png'),
    pygame.image.load('enemy/бандит/бандит3.png'),
    pygame.image.load('enemy/бандит/бандит4.png'),
    pygame.image.load('enemy/бандит/бандит5.png'),
    pygame.image.load('enemy/бандит/бандит6.png'),
    pygame.image.load('enemy/бандит/бандит7.png'),
    pygame.image.load('enemy/бандит/бандит8.png'),
    pygame.image.load('enemy/бандит/бандит9.png'),
    pygame.image.load('enemy/бандит/бандит10.png')
]
enemy_count = 0
enemy_x = 500
enemy_y = 250
enemy_speed = 3



run = True
while run:

    dis.blit(fon, (fon_x, 0))
    dis.blit(fon, (fon_x + 1000, 0))

    fon_x -= fon_speed 
    if fon_x <= -1000:
        fon_x = 0


    dis.blit(enemy[enemy_count], (enemy_x, enemy_y))

    if enemy_count == 9:
        enemy_count = 0 
    if enemy_x < -100:
        enemy_x = 1000

    dis.blit(player_img[player_count], (player_x, player_y))
    dis.blit(enemy2[enemy2_count], (enemy2_x, enemy2_y))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    clock.tick(60)
