import pygame
from color import Color

class Screen(object):
    def __init__(self, screen_width=900, screen_height=900):

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.square_size = 900//3
        self.block_size = self.square_size // 3

        self.clock = pygame.time.Clock()
        self.set_title()

        self.font = pygame.font.SysFont("arial", 50)
        self.font_color = Color.ELEMENT_COLOR

        self.solved_grid = [
            [7, 8, 5, 4, 3, 9, 1, 2, 6],
            [6, 1, 2, 8, 7, 5, 3, 4, 9],
            [4, 9, 3, 6, 2, 1, 5, 7, 8],
            [8, 5, 7, 9, 4, 3, 2, 6, 1],
            [2, 6, 1, 7, 5, 8, 9, 3, 4],
            [9, 3, 4, 1, 6, 2, 7, 8, 5],
            [5, 7, 8, 3, 9, 4, 6, 1, 2],
            [1, 2, 6, 5, 8, 7, 4, 9, 3],
            [3, 4, 9, 2, 1, 6, 8, 5, 7]
        ]
        self.sudoku_puzzle = [
        [7,8,'',4,'','',1,2,''],
        [6,'','','',7,5,'','',9],
        ['','','',6,'',1,'',7,8],
        ['','',7,'',4,'',2,6,''],
        ['','',1,'',5,'',9,3,''],
        [9,'',4,'',6,'','','',5],
        ['',7,'',3,'','','',1,2],
        [1,2,'','','',7,4,'',''],
        ['',4,9,2,'',6,'','',7]
]
        # self.second_grid = np.random.randint(1, 10, size=(9, 9))
        # self.randomize_grid()
        self.x = []
        self.y = []
        self.zero_grid = [
            [0, 0, 0, 0, 0, 0, 0, 0]* 9
        ] 
    
    def fill_background(self, color=Color.WHITE):
        self.screen.fill(color)

    @staticmethod
    def set_title(title="Sudoku"):
        pygame.display.set_caption(title)

    @staticmethod
    def update():
        pygame.display.flip()

    def fill_grid(self):
        x = []
        y = []
        for row in range(0, 9):
            for col in range(0, 9): 
                pos_x=100 * (col+1) - 50
                pos_y=(row + 1)*100 - 70
                x.append(100*(col+1) - 50)
                y.append((row + 1)*100 - 70)
                self.populate_cells(str(self.sudoku_puzzle[row][col]), pos_x=pos_x, pos_y=pos_y)
        self.x = x
        self.y = y

    def populate_cells(self, num, pos_x, pos_y):
        text = self.font.render(str(num), False, self.font_color)
        self.screen.blit(text, (pos_x, pos_y))

    def check_grid(self, row, col, num):
        if self.solved_grid[col][row] == num:
            return True
        else:
            return False

    def draw_rect(self, pos, height, width):
        rect = pygame.Rect(pos[0], pos[1], width, height)
        rect.center = pos
        pygame.draw.rect(self.screen, Color.BLUE,rect, 5)

    def draw_grid(self):
        # Minor Lines
        for x in range(0, self.screen_width, self.block_size):
            pygame.draw.line(self.screen, Color.GREY, (x, 900), (x, 0), 2)
            pygame.draw.line(self.screen, Color.GREY, (900, x), (0, x), 2)

        # Major Lines
        for y in range(0, self.screen_width, self.square_size):
            pygame.draw.line(self.screen, Color.BLACK, (y, 900), (y, 0), 3)
            pygame.draw.line(self.screen, Color.BLACK, (900, y), (0, y), 3)
        
        pygame.draw.line(self.screen, Color.BLACK, (900, 0), (900, 900), 8)
        pygame.draw.line(self.screen, Color.BLACK, (0, 900), (900, 900), 8)
