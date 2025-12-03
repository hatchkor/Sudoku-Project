import pygame
from sudoku_generator import *
pygame.init()

def draw_button(screen, rect, text, font, color):
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, (0,0,0), rect, 2)
    label = font.render(text, True, (0,0,0))
    label_rect = label.get_rect(center = rect.center)
    screen.blit(label, label_rect)

def show_main_menu():
    screen_width = 800
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Sudoku')
    font = pygame.font.SysFont('Charter', 30)
    easy_button = pygame.Rect(50, 300, 200, 50)
    medium_button = pygame.Rect(300, 300, 200, 50)
    hard_button = pygame.Rect(550, 300, 200, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if easy_button.collidepoint(mouse_pos):
                    return "easy"
                if medium_button.collidepoint(mouse_pos):
                     return "medium"
                if hard_button.collidepoint(mouse_pos):
                     return "hard"
            screen.fill((200, 200, 200))
            draw_button(screen, easy_button, "Easy", font, (31, 247, 20))
            draw_button(screen, medium_button, "Medium", font, (209, 219, 15))
            draw_button(screen, hard_button, "Hard", font, (227, 28, 25))

            title = font.render('Welcome to Sudoku!', True, (0, 0, 0))
            diff = font.render('Choose a difficulty:', True, (0, 0, 0))
            screen.blit(title, (300, 150))
            screen.blit(diff, (50, 250))
            pygame.display.update()
def main():
    show_main_menu()

if __name__ == '__main__':
    main()