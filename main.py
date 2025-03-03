# Pygame game template

import pygame
import sys
import config # Import the config module


def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True


def draw_text(screen, text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initalize the clock here

     
    running = True
    while running:
        running = handle_events()
        screen.fill(config.GREEN) # Use color from config

        text_font = pygame.font.SysFont("Arial", 30)
        draw_text(screen, 'Hello World', text_font, config.BLUE, 0, 0)
        pygame.display.flip()

        # Limit the frame rate to the specified frames per second
        clock.tick(config.FPS) # Use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()



