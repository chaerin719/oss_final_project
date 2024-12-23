import pygame, sys
from utils import Button

def draw_score_screen(screen, font, game, event):
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    
    score1_image = pygame.image.load("assets/images/score1.jpg")
    score2_image = pygame.image.load("assets/images/score2.jpg")
    score1_image = pygame.transform.scale(score1_image, (WIDTH, HEIGHT))
    score2_image = pygame.transform.scale(score2_image, (WIDTH, HEIGHT))
    
    score_image = None
    if game.score < 500 :
        if game.current_bgm != "score1_bgm":
            game.current_bgm = "score1_bgm"
            game.num_repeat_bgm = 1
            game.is_changed_bgm = True
        score_image = score1_image
    else:
        if game.current_bgm != "score2_bgm":
            game.current_bgm = "score2_bgm"
            game.num_repeat_bgm = 1
            game.is_changed_bgm = True
        score_image = score2_image
        
    screen.blit(score_image, (0, 0))
        

    # 점수 텍스트
    large_font = pygame.font.Font("assets/fonts/온글잎_공부잘하자나.ttf", 120)
    final_score_text = large_font.render(f"{game.score}", True, (0, 0, 0))
    text_rect = final_score_text.get_rect(center=(WIDTH // 2 - 10, HEIGHT // 2 - 100))
    screen.blit(final_score_text, text_rect)

    buttons = [
        Button(200, 500, 200, 50, "다시 하기"),
        Button(750, 500, 200, 50, "게임 종료"),
    ]
    
    for button in buttons:
        button.draw(screen, font)
        
        if event.type == pygame.MOUSEBUTTONUP and button.is_clicked(event):
            
            if button.text == "다시 하기":
                return "menu"   
            elif button.text == "게임 종료":
                pygame.quit()
                sys.exit()

    return "score"
