import pygame
from sys import exit

def bouncing_ball():
    global x_speed, y_speed
    global counter1, counter2

    circleRect.x += x_speed
    circleRect.y += y_speed

    # colisão com as paredes da tela
    if circleRect.right >= screen_width:
        x_speed *= -1
        counter2 += 1
    elif circleRect.left <= 0:
        x_speed *= -1
        counter1 += 1
    if circleRect.bottom >= screen_height or circleRect.top <= 0:
        y_speed *= -1

    collision_tolerance = 10

    #  Colisão com a barra 1
    if circleRect.colliderect(bar1):
        if abs(bar1.top-circleRect.bottom) < collision_tolerance and y_speed > 0:
            y_speed *= -1
        if abs(bar1.bottom-circleRect.top) < collision_tolerance and y_speed < 0:
            y_speed *= -1
        if abs(bar1.right-circleRect.left) < collision_tolerance and x_speed < 0:
            x_speed *= -1
        if abs(bar1.left - circleRect.right) < collision_tolerance and x_speed > 0:
            x_speed *= -1

    #  Colisão com a barra 2
    if circleRect.colliderect(bar2):
        if abs (bar2.top-circleRect.bottom) < collision_tolerance and y_speed > 0:
            y_speed *= -1
        if abs (bar2.bottom-circleRect.top) < collision_tolerance and y_speed < 0:
            y_speed *= -1
        if abs (bar2.right-circleRect.left) < collision_tolerance and x_speed < 0:
            x_speed *= -1
        if abs (bar2.left - circleRect.right) < collision_tolerance and x_speed > 0:
            x_speed *= -1        

    pygame.draw.rect(screen, (255,50,50), circleRect, 50, 50)


pygame.init()
pygame.font.init()

#  Tamanho da tela
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

#  Titulo do jogo
pygame.display.set_caption("Pong Game")

#  Contadores de pontos
counter1 = 0
counter2 = 0

#  Varivel de framerate 
clock = pygame.time.Clock()

#  Fonte de texto
my_font = pygame.font.SysFont("Arial", 30)

bar1 = pygame.Rect(20, 250, 30, 50)
bar2 = pygame.Rect(750, 250, 30, 50)
circleRect = pygame.Rect(350, 150, 30, 30)

#  Velocidade da bola
x_speed, y_speed = 5, 4

#  Velocidade das barras
velocidade = 5

while True:

    #  Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()   


    #  Se bar1 sair da tela, volta para o inicio e vice-versa
    if bar1.y >= screen_height:
        bar1.y = -50
    elif bar1.y <= -50:
        bar1.y = screen_height

    if bar2.y >= screen_height:
        bar2.y = -50
    elif bar2.y <= -50:
        bar2.y = screen_height
        

    #  Movimentação das setas do bar 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        bar1.y -= velocidade
    if keys[pygame.K_DOWN]:
        bar1.y += velocidade

    #  Movimentação das setas do bar2
    if keys[pygame.K_w]:
        bar2.y -= velocidade
    if keys[pygame.K_s]:
        bar2.y += velocidade

    screen.fill((30,30,30))
    pygame.draw.rect(screen, (255,255,255), bar1)
    pygame.draw.rect(screen, (0,0,0), bar2)
    bouncing_ball()
    text_surface1 = my_font.render(f'Branco: {counter1}', False, (255, 255, 255))
    text_surface2 = my_font.render(f'Preto: {counter2}', False, (255, 255, 255))
    screen.blit(text_surface1, (90,10))
    screen.blit(text_surface2, (590,10))


    #  Atualiza a tela
    pygame.display.flip()

    #  Usa variavel de framerate e limita a 60 fps
    clock.tick(60)
