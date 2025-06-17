import pygame
import constants as const

def main():
    pygame.init()
    screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (255,255,255))

        #last
        pygame.display.flip()

if __name__ == "__main__":
    main()