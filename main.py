import pygame
from snake import Snake
from apple import Apple

#Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
SNAKE_SPEED = 4

GRID_SIZE = 40
GRID_WIDTH = SCREEN_WIDTH/GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT/GRID_SIZE

LIGHT_GREEN = (126, 224, 129)
EMERALD = (68, 207, 108)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def drawGrid(surface):
    """Creates the background"""
    for x in range(0, int(GRID_WIDTH)):
        for y in range(0, int(GRID_HEIGHT)):
            rect = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE,GRID_SIZE))
            #Alternating colours for grid pattern
            if (x + y) % 2 == 0:
                pygame.draw.rect(surface=surface,color=LIGHT_GREEN, rect=rect)
            else:
                pygame.draw.rect(surface=surface,color=EMERALD,rect=rect)

def main():
    pygame.init()
    game_over = False
    show_game_over = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game by Alexander')
    font = pygame.font.SysFont(None, 30)

    drawGrid(screen)
    snake = Snake()
    apple = Apple(snake.segments)

    while not game_over:
        clock.tick(SNAKE_SPEED)
        drawGrid(screen)
        snake.user_input()
        
        if not snake.move():
            screen.fill(BLACK)
            drawGrid(screen)
            mesg = font.render("You Lost! Press P-Play Again or Q-Quit", True, BLACK)
            screen.blit(mesg, [120, 290])
            mesg = font.render(f"Final Score: {snake.score}", True, BLACK)
            screen.blit(mesg, [230, 330])
            show_game_over = True
            pygame.display.update()
            while show_game_over:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True    
                            show_game_over = False
                        if event.key == pygame.K_p:
                            snake = Snake()
                            apple = Apple(snake.segments)
                            show_game_over = False
                            break
                            
        if snake.segments[0] == apple.coordinates:
            snake.length += 1
            snake.score += 1
            apple.randomize_coordinates(snake.segments)

        snake.draw(screen)
        apple.draw(screen)
        scoretext = font.render(f"Score: {snake.score}", True, BLACK)
        screen.blit(scoretext, (5, 10))
        pygame.display.update()

main()