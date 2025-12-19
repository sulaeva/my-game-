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
    pygame.image.load('icon/враги/зомби/zombie/зомби6-removebg-preview.png'),
    pygame.image.load('icon/враги/зомби/zombie/зомби7-removebg-preview.png'),
    pygame.image.load('icon/враги/зомби/zombie/зомби8-removebg-preview.png'),
    pygame.image.load('icon/враги/зомби/zombie/зомби1-removebg-preview.png'),
    pygame.image.load('icon/враги/зомби/zombie/зомби2-removebg-preview.png'),
    pygame.image.load('icon/враги/зомби/zombie/зомби3-removebg-preview.png'),
    pygame.image.load('icon/враги/зомби/zombie/зомби4-removebg-preview.png'),
    pygame.image.load('icon/враги/зомби/zombie/зомби5-removebg-preview.png'),
    pygame.image.load('icon/враги/зомби/zombie/зомби6-removebg-preview.png')
]


enemy_count = 0 
enemy_x = 1000
enemy_y = 250 
enemy_speed = 2



enemy_atk = [
    pygame.image.load('icon/враги/зомби/zombie/зомби9-removebg-preview.png'),
    pygame.image.load('icon/враги/зомби/zombie/зомби10-removebg-preview.png'),
    pygame.image.load('icon/враги/зомби/zombie/зомби11-removebg-preview.png'),
    pygame.image.load('icon/враги/зомби/zombie/зомби12-removebg-preview.png'),
    pygame.image.load('icon/враги/зомби/zombie/зомби13-removebg-preview.png')
]



run = True
while run:
    clock.tick(10)

    dis.blit(bg, (0, 0))
    dis.blit(enemy_img[enemy_count], (enemy_x, enemy_y))
    enemy_count += 1 
    if enemy_count >= len(enemy_img):
        enemy_count = 0

    enemy_x -= enemy_speed
    if enemy_x < - 100:
        enemy_x = 1000

    



    pygame.display.update()


    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
            pygame.quit()

    