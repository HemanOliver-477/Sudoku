import pygame, sys
from pygame import *
from screen import Screen
from color import Color

pygame.init()
screen = Screen()

def myround(x, base=50):
    return base* round(x/base)

def draw_text(text, surface, x, y):
    text = screen.font.render(text, 1, Color.BROWN)
    text_rect = text.get_rect()
    text_rect.center = (x, y) 
    surface.blit(text, text_rect)

mouseClick = False
mousex, mousey = 0, 0
pos = [1000, 1000]
key = ""
def main():
    while True:
        screen.fill_background()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                global pos
                pos = list(pygame.mouse.get_pos())
                pos[0] = myround(pos[0])
                pos[1] = myround(pos[1])
                mouseClick = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                    if mouseClick:
                        row = int(((pos[0] + 50)/ 100) - 1)
                        col = int(((pos[1] + 50)/ 100) - 1)
                        if screen.sudoku_puzzle[col][row] == '' and screen.check_grid(row, col, key):
                            print(row, col)
                            screen.sudoku_puzzle[col][row] = key
                elif event.key == pygame.K_2:
                    key = 2
                    if mouseClick:
                        row = int(((pos[0] + 50)/ 100) - 1)
                        col = int(((pos[1] + 50)/ 100) - 1)
                        if screen.sudoku_puzzle[col][row] == '' and screen.check_grid(row, col, key):
                            print(row, col)
                            screen.sudoku_puzzle[col][row] = key
                elif event.key == pygame.K_3:
                    key = 3
                    if mouseClick:
                        row = int(((pos[0] + 50)/ 100) - 1)
                        col = int(((pos[1] + 50)/ 100) - 1)
                        if screen.sudoku_puzzle[col][row] == '' and screen.check_grid(row, col, key):
                            print(row, col)
                            screen.sudoku_puzzle[col][row] = key
                elif event.key == pygame.K_4:
                    key = 4
                    if mouseClick:
                        row = int(((pos[0] + 50)/ 100) - 1)
                        col = int(((pos[1] + 50)/ 100) - 1)
                        if screen.sudoku_puzzle[col][row] == '' and screen.check_grid(row, col, key):
                            print(row, col)
                            screen.sudoku_puzzle[col][row] = key
                elif event.key == pygame.K_5:
                    key = 5
                    if mouseClick:
                        row = int(((pos[0] + 50)/ 100) - 1)
                        col = int(((pos[1] + 50)/ 100) - 1)
                        if screen.sudoku_puzzle[col][row] == '' and screen.check_grid(row, col, key):
                            print(row, col)
                            screen.sudoku_puzzle[col][row] = key
                elif event.key == pygame.K_6:
                    key = 6
                    if mouseClick:
                        row = int(((pos[0] + 50)/ 100) - 1)
                        col = int(((pos[1] + 50)/ 100) - 1)
                        if screen.sudoku_puzzle[col][row] == '' and screen.check_grid(row, col, key):
                            print(row, col)
                            screen.sudoku_puzzle[col][row] = key
                elif event.key == pygame.K_7:
                    key = 7
                    if mouseClick:
                        row = int(((pos[0] + 50)/ 100) - 1)
                        col = int(((pos[1] + 50)/ 100) - 1)
                        if screen.sudoku_puzzle[col][row] == '' and screen.check_grid( row, col, key):
                            print(row, col)
                            screen.sudoku_puzzle[col][row] = key
                elif event.key == pygame.K_8:
                    key = 8
                    if mouseClick:
                        row = int(((pos[0] + 50)/ 100) - 1)
                        col = int(((pos[1] + 50)/ 100) - 1)
                        if screen.sudoku_puzzle[col][row] == '' and screen.check_grid(row, col, key):
                            print(row, col)
                            screen.sudoku_puzzle[col][row] = key
                elif event.key == pygame.K_9:
                    key = 9
                    if mouseClick:
                        row = int(((pos[0] + 50)/ 100) - 1)
                        col = int(((pos[1] + 50)/ 100) - 1)
                        if screen.sudoku_puzzle[col][row] == '' and screen.check_grid(row, col, key):
                            print(row, col)
                            screen.sudoku_puzzle[col][row] = key

        screen.draw_rect(pos,screen.block_size, screen.block_size)
        screen.draw_grid()
        screen.fill_grid()
        screen.update()
        screen.clock.tick(60)

def start_menu():
    running = True
    click = False
    screen.fill_background(color=Color.YELLOW)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(450, 450, 300, 100)
        button_1.center = (450, 450)

        if button_1.collidepoint(mx, my):
            if click:
                main()
    
        pygame.draw.rect(screen.screen, Color.GREEN, button_1)
        draw_text("Start Sudoku", screen.screen, 450, 450)
        pygame.display.update()
        screen.clock.tick(60)

start_menu()