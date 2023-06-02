import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60
# game varaiables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_location = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_location = [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7), (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]

captured_white = []
captured_black = []
turn_step = 0
selection = 100
valid_moves = []

black_queen = pygame.transform.scale(pygame.image.load('images/blackqueen.png'), (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))

black_rook = pygame.transform.scale(pygame.image.load('images/black rook.png'), (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))

black_knight = pygame.transform.scale(pygame.image.load('images/black knight.png'), (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))

black_king = pygame.transform.scale(pygame.image.load('images/black king.png'), (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))

black_bishop = pygame.transform.scale(pygame.image.load('images/black bishop.png'), (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))

black_pawn = pygame.transform.scale(pygame.image.load('images/black pawn.png'), (80, 80))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))

white_queen = pygame.transform.scale(pygame.image.load('images/white queen.png'), (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))

white_rook = pygame.transform.scale(pygame.image.load('images/white rook.png'), (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))

white_knight = pygame.transform.scale(pygame.image.load('images/white knight.png'), (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))

white_king = pygame.transform.scale(pygame.image.load('images/white king.png'), (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))

white_bishop = pygame.transform.scale(pygame.image.load('images/white bishop.png'), (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))

white_pawn = pygame.transform.scale(pygame.image.load('images/white pawn.png'), (80, 80))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

white_images = [white_bishop, white_king, white_knight, white_queen, white_rook, white_pawn]
black_images = [black_bishop, black_king, black_knight, black_queen, black_rook, black_pawn]

small_white_image = [white_king_small, white_pawn_small, white_rook_small, white_queen_small, white_bishop_small, white_knight_small]
small_black_image = [black_king_small, black_pawn_small, black_rook_small, black_queen_small, black_bishop_small, black_knight_small]

peices = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light grey', [600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'light grey', [700 - (column * 200), row * 100, 100, 100])

run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')
    draw_board()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()
pygame.quit()