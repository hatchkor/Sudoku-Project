import pygame
from sudoku_generator import *
pygame.init()

def main():
    screen_width = 800
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Sudoku')
    font = pygame.font.SysFont('Charter', 30)
    sudoku_text = font.render("Welcome to Sudoku", True, (0,0,0))
    difficulty_text = font.render("Choose a difficulty: ", True, (0,0,0))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255,255,255))
        screen.blit(sudoku_text, (300, 150))
        screen.blit(difficulty_text, (300, 250))
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    main()