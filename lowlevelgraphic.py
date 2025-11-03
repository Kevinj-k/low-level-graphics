import pygame, math

def drawStuff(background):
      

    
    pygame.draw.circle(background, (0, 0, 0), (50, 100), 45)
    
    pygame.draw.circle(background,(0,0,0), (550,100),45)
    
    pygame.draw.arc(background, (0, 0, 0), ((252, 132), (100, 100)), 0, math.pi/2, 5)
    
    
    pygame.draw.ellipse(background, (0, 0, 0), ((252, 332), (150, 100)), 0)
    pygame.draw.ellipse(background, (198, 1, 31), ((252, 341), (150, 80)), 0)
    
    


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("My Drawing")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((232, 190, 172))

    drawStuff(background)

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONUP:
                print(pygame.mouse.get_pos())
        screen.blit(background, (0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()