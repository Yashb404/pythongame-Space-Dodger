import pygame
import time
import random 

wIDTH, HEIGHT = 500,500
WIN = pygame.display.set_mode((wIDTH,HEIGHT))            
pygame.display.set_caption("Python Game")
 
def main():
    run=True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                break
    
    pygame.quit()
    
if __name__== "__main__":
    main()
