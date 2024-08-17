import pygame
pygame.init()

screenwidth = 1280
screenheight = 650
gamewindow = pygame.display.set_mode((screenwidth, screenheight))
clock = pygame.time.Clock()
fps = 60

exit_game = False
pygame.display.set_caption("Ping Pong by Suzaan Khan")

 #GAME RECTANGLES
ball = pygame.Rect(screenwidth/2 - 15, screenheight/2 - 15, 30, 30)
player = pygame.Rect(screenwidth - 20, screenheight/2 - 70, 10, 140)
opponent = pygame.Rect(10, screenheight/2 - 70, 10, 140)

bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

ball_speedx = 7
ball_speedy = 7
# ball_root_speed = 7

player_y_speed = 0
opponent_y_speed = 5

score = 0
ball_speedx_2 = 18
ball_speedy_2 = 18

# def collision_sound():
#     collision_sound = pygame.mixer.music.load("pointsoundeffect.wav")
#     pygame.mixer.music.play()

collision_sound = pygame.mixer.Sound("pointsoundeffect.wav")

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_y_speed = 4
            if event.key == pygame.K_DOWN:
                player_y_speed = -4

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screenheight:
        player.bottom = screenheight

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screenheight:
        opponent.bottom = screenheight

    #VERTICLE BALL SPEED
    if ball.bottom >= screenheight:
        ball_speedy *= -1
        # collision_sound.play()
    if ball.top <= 0:
        ball_speedy *= -1
        # collision_sound.play()

    #HORIZONTAL BALL SPEED
    if ball.right >= screenwidth: #RIGHT COLLISION
        ball_speedx *= -1
    if ball.left <= 0:    #LEFT COLLISION
        ball_speedx *= 1

    if ball.colliderect(player):
        ball_speedx = ball_speedx * -1
        collision_sound.play()
        score = score + 1
        print(score)

    if ball.colliderect(opponent):
        ball_speedx *= -1
        collision_sound.play()

    if opponent.y < ball.y:
        opponent.y = opponent.y + 7
    if opponent.y > ball.y:
        opponent.y = opponent.y - 7

    ball.x = ball.x + ball_speedx
    ball.y = ball.y + ball_speedy

    player.y = player.y - player_y_speed
    # opponent.y = opponent.y - opponent_y_speed

    #VISIBLES
    gamewindow.fill(bg_color)
    pygame.draw.rect(gamewindow, light_grey, player)
    pygame.draw.rect(gamewindow, light_grey, opponent)
    pygame.draw.ellipse(gamewindow, light_grey, ball)
    pygame.draw.aaline(gamewindow, light_grey, (screenwidth/2, 0), (screenwidth/2, screenheight))

    clock.tick(fps)
    pygame.display.update()
pygame.quit()
quit()