import pygame
from sys import exit

def main():
    pygame.init()

    #  Tamanho da tela
    screen = pygame.display.set_mode((800, 400))

    #  Titulo do jogo
    pygame.display.set_caption("Pong Game")

    #  Varivel de framerate 
    clock = pygame.time.Clock()

    # Carrega a surface de imagem de fundo
    bgd_surface = pygame.image.load("bgd.png").convert_alpha()

    bar_surface = pygame.image.load("bar.png").convert_alpha()
    bar_y_pos = 150

    bar2_surface = pygame.image.load("bar2.png").convert_alpha()
    bar2_y_pos = 150

    ball_surface = pygame.image.load("ball.png").convert_alpha()

    velocidade = 5
    screen_width = 800
    screen_height = 400

    while True:
        
        #  Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()   

        # Posições da bola
        ball_xpos = 350
        ball_ypos = 150
        ball_step_x = 10
        ball_step_y = 10

        # Taca a imagem de fundo na tela
        screen.blit(bgd_surface, (0, 0))
        screen.blit(bar_surface, (30, bar_y_pos))
        screen.blit(bar2_surface, (700, bar2_y_pos))
        screen.blit(ball_surface, (ball_xpos, ball_ypos))

        #  Se bar1 sair da tela, volta para o inicio e vice-versa
        if bar_y_pos >= 400:
            bar_y_pos = 0
        elif bar_y_pos <= 0:
            bar_y_pos = 400

        if bar2_y_pos >= 400:
            bar2_y_pos = 0
        elif bar2_y_pos <= 0:
            bar2_y_pos = 400
    

        #  Movimentação das setas do bar 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            bar_y_pos -= velocidade
        if keys[pygame.K_DOWN]:
            bar_y_pos += velocidade

        #  Movimentação das setas do bar2
        if keys[pygame.K_w]:
            bar2_y_pos -= velocidade
        if keys[pygame.K_s]:
            bar2_y_pos += velocidade

        if ball_xpos > screen_width - 64 or ball_xpos < 0:
            ball_step_x = -ball_step_x
        if ball_ypos > screen_width - 64 or ball_ypos < 0:
            ball_step_y = -ball_step_y
        # atualiza a posição da bola
        ball_xpos += ball_step_x # move pra baixo na direita
        ball_ypos += ball_step_y # move pra baixo

        screen.blit(bgd_surface, (0,0))    
        screen.blit(bar_surface, (30, bar_y_pos))
        screen.blit(bar2_surface, (700, bar2_y_pos)) 
        screen.blit(ball_surface, (ball_xpos, ball_ypos))
        #  Atualiza a tela
        pygame.display.flip()

        #  Usa variavel de framerate e limita a 60 fps
        clock.tick(60)


if __name__=="__main__":
    main()