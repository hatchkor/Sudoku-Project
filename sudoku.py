from sudoku_generator import *
pygame.init()

def draw_button(screen, rect, text, font, color):
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, (0,0,0), rect, 2) # screen, color, object, width
    label = font.render(text, True, (0,0,0))
    label_rect = label.get_rect(center = rect.center)
    screen.blit(label, label_rect)

def show_main_menu():
    pygame.display.set_caption('Sudoku')
    font = pygame.font.SysFont('Charter', 30) # name, size
    easy_button = pygame.Rect(50, 300, 200, 50) # x, y, width, height
    medium_button = pygame.Rect(300, 300, 200, 50)
    hard_button = pygame.Rect(550, 300, 200, 50)

    while True:
        draw_button(screen, easy_button, "Easy", font, (31, 247, 20))  # screen, rectangle, text, font, color
        draw_button(screen, medium_button, "Medium", font, (209, 219, 15))
        draw_button(screen, hard_button, "Hard", font, (227, 28, 25))

        title = font.render('Welcome to Sudoku!', True, (0, 0, 0))  # text, antialias, color
        diff = font.render('Choose a difficulty:', True, (0, 0, 0))
        screen.blit(title, (300, 150))  # object, (x, y)
        screen.blit(diff, (50, 250))
        pygame.display.update()
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
def show_win_screen():
    font = pygame.font.SysFont('Charter', 50)
    play_button = pygame.Rect(280, 300, 200, 50)
    while True:
        screen.fill((157, 158, 168))
        text = font.render('YOU WIN!!', True, (0, 0, 0))
        screen.blit(text, (300, 150))
        draw_button(screen, play_button, "Play Again?", font, (31, 247, 20))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button.collidepoint(mouse_pos):
                    main()

def show_game_over_screen():
    font = pygame.font.SysFont('Charter', 50)
    play_button = pygame.Rect(280, 300, 200, 50)
    while True:
        screen.fill((157, 158, 168))
        text = font.render('you lost.', True, (0, 0, 0))
        screen.blit(text, (300, 150))
        draw_button(screen, play_button, "Play Again?", font, (204, 33, 33))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button.collidepoint(mouse_pos):
                    main()


def main():
    global screen, removed
    selected = None
    font = pygame.font.SysFont('Charter', 30)
    screen = pygame.display.set_mode((800, 800))
    screen.fill((255, 255, 255))
    difficulty = show_main_menu()
    if difficulty == "easy":
        removed = 30
        screen.fill((255, 255, 255))
    elif difficulty == "medium":
        removed = 40
        screen.fill((255, 255, 255))
    elif difficulty == "hard":
        removed = 50
        screen.fill((255, 255, 255))
    reset_button = pygame.Rect(50, 600, 200, 50)
    restart_button = pygame.Rect(300, 600, 200, 50)
    exit_button = pygame.Rect(550, 600, 200, 50)
    board_data = generate_sudoku(9, removed)
    board = Board(450, 450, screen, difficulty, board_data)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                mouse_pos = pygame.mouse.get_pos()
                pos = board.click(mx, my)
                if pos:
                    selected = pos
                    board.select(*selected)
                if reset_button.collidepoint(mouse_pos):
                    board.reset_to_original()
                if restart_button.collidepoint(mouse_pos):
                    return main()
                if exit_button.collidepoint(mouse_pos):
                    pygame.quit()
            if event.type == pygame.KEYDOWN and selected:
                row, col = selected
                if board.original[row][col] != 0:
                    continue

                if event.key == pygame.K_RETURN:
                    board.place_sketch()
                elif event.key == pygame.K_1:
                    board.sketch_value(1)
                elif event.key == pygame.K_2:
                    board.sketch_value(2)
                elif event.key == pygame.K_3:
                    board.sketch_value(3)
                elif event.key == pygame.K_4:
                    board.sketch_value(4)
                elif event.key == pygame.K_5:
                    board.sketch_value(5)
                elif event.key == pygame.K_6:
                    board.sketch_value(6)
                elif event.key == pygame.K_7:
                    board.sketch_value(7)
                elif event.key == pygame.K_8:
                    board.sketch_value(8)
                elif event.key == pygame.K_9:
                    board.sketch_value(9)
                elif event.key == pygame.K_BACKSPACE:
                    board.clear()
        screen.fill((255,255,255))
        board.draw()
        board.draw_numbers()
        suds = font.render('Sudoku', True, (0, 0, 0))
        screen.blit(suds, (400, 25))
        draw_button(screen, reset_button, "Reset", font, (247, 143, 57))
        draw_button(screen, restart_button, "Restart", font, (247, 143, 57))
        draw_button(screen, exit_button, "Exit", font, (247, 143, 57))
        pygame.display.update()
        if board.is_full():
            if board.check_board():
                show_win_screen()
            else:
                show_game_over_screen()
    pygame.quit()



if __name__ == '__main__':
    main()
    
