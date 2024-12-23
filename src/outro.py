import pygame



def draw_outro_screen(screen, game):
    WIDTH = screen.get_width() 
    HEIGHT = screen.get_height()  
    
    outro_images = [
        pygame.image.load("assets/images/outro1.jpg"),
        pygame.image.load("assets/images/outro2.jpg"),
        pygame.image.load("assets/images/outro3.jpg"),
        pygame.image.load("assets/images/outro4.jpg"),
    ]

    # 각 이미지를 화면 크기에 맞게 조정
    outro_images = [pygame.transform.scale(img, (WIDTH, HEIGHT)) for img in outro_images]

    for img in outro_images:
        screen.blit(img, (0, 0))
        pygame.display.flip()  
        pygame.time.delay(500)  

    return "score"
