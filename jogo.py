import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definindo as cores
branco = (255, 255, 255)

# Configurações da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo RPG")

# Carregando a imagem de fundo
fundo = pygame.image.load("fundo.jpg")
fundo = pygame.transform.scale((fundo), (largura_tela, altura_tela))
cursor = 'mouse.webp'

# Função para desenhar o texto na tela
def desenhar_texto(texto, tamanho, cor, x, y):
    fonte = pygame.font.SysFont(None, tamanho)
    texto = fonte.render(texto, True, cor)
    tela.blit(texto, (x, y))

# Função principal
def menu():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if 300 <= mouse[0] <= 500 and 400 <= mouse[1] <= 450:
                    print("Em construção")

        # Obtendo a posição do mouse
        mouse = pygame.mouse.get_pos()

        # Desenhando a imagem de fundo
        tela.blit(fundo, (0, 0))

        # Desenhando elementos textuais
        desenhar_texto("Bem-vindo ao Jogo RPG", 50, branco, 150, 100)
        desenhar_texto("Escolha sua classe e enfrente desafios para derrotar o Boss!", 30, branco, 50, 200)

        # Desenhando botão de iniciar
        pygame.draw.rect(tela, branco, (300, 400, 200, 50))
        desenhar_texto("Iniciar", 40, (0, 0, 0), 340, 405)

        pygame.display.flip()

# Executando o menu
menu()