import pygame

pygame.init()
clock = pygame.time.Clock()

dis = pygame.display.set_mode((1000, 400))

bg = pygame.image.load('image/vecteezy_parallax-background-with-destroyed-city-street_14320066.jpg')

enemy_img = [
    pygame.image.load('icon/враги/зомби/zombie/зомби1-removebg-preview.png'),
    pygame.image.load('icon/враги/зомби/zombie/зомби2-removebg-preview.png'),
    pygame.image.load('icon/враги/зомби/zombie/зомби3-removebg-preview.png'),
    pygame.image.load('icon/враги/зомби/zombie/зомби4-removebg-preview.png'),
    pygame.image.load('icon/враги/зомби/zombie/зомби5-removebg-preview.png'),
    pygame.image.load('icon/враги/зомби/zombie/зомби6-removebg-preview.png')
]

enemy_atk = [
    pygame.image.load('icon/враги/зомби/zombie/зомби9-removebg-preview.png'),
    pygame.image.load('icon/враги/зомби/zombie/зомби10-removebg-preview.png'),
    pygame.image.load('icon/враги/зомби/zombie/зомби11-removebg-preview.png'),
    pygame.image.load('icon/враги/зомби/zombie/зомби12-removebg-preview.png'),
    pygame.image.load('icon/враги/зомби/zombie/зомби13-removebg-preview.png')
]

enemy_x = 1000
enemy_y = 250
enemy_speed = 2

enemy_count = 0
attack_count = 0

enemy_alive = True
enemy_attack = False

# 🔲 Невидимый квадрат (hitbox)
hitbox = pygame.Rect(300, 250, 50, 50)

run = True
while run:
    clock.tick(10)
    dis.blit(bg, (0, 0))

    if enemy_alive:
        enemy_rect = enemy_img[0].get_rect(topleft=(enemy_x, enemy_y))

        # 🔥 Проверка столкновения
        if hitbox.colliderect(enemy_rect):
            enemy_attack = True

        if not enemy_attack:
            dis.blit(enemy_img[enemy_count], (enemy_x, enemy_y))
            enemy_count = (enemy_count + 1) % len(enemy_img)
            enemy_x -= enemy_speed
        else:
            dis.blit(enemy_atk[attack_count], (enemy_x, enemy_y))
            attack_count += 1

            # 💀 После анимации атаки — исчезает
            if attack_count >= len(enemy_atk):
                enemy_alive = False

    # ⚠️ Hitbox невидим, но можно включить для отладки:
    # pygame.draw.rect(dis, (255, 0, 0), hitbox, 2)

    pygame.display.update()

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
            pygame.quit()
