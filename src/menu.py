import pygame, random, sys
from utils import Button

def draw_menu_screen(screen, font, game, event):
    HEIGHT = screen.get_height() 
    WIDTH = screen.get_width()
    
    pygame.event.clear()
    game.reset()
    
    if not (game.current_bgm == "menu1_bgm" or game.current_bgm == "menu2_bgm"):
        game.current_bgm = "menu1_bgm" if random.randint(0,1) else "menu2_bgm"
        game.num_repeat_bgm = 1
        game.is_changed_bgm = True

    # 배경 이미지 로드
    background_img = pygame.image.load("assets/images/menu.jpg")
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

    # 배경 이미지 그리기
    screen.blit(background_img, (0, 0))


    # 버튼 생성
    buttons = [
        Button(200, 200, 200, 50, "수업 시작"),
        Button(200, 320, 200, 50, "도움말"),
        Button(200, 440, 200, 50, "게임 종료"),
    ]

    for button in buttons:
        button.draw(screen, font)

        # 마우스 버튼을 뗐을 때
        if event.type == pygame.MOUSEBUTTONUP and button.is_clicked(event):
            
            # 버튼 동작 처리
            if button.text == "수업 시작":
                game.is_changed_bgm = True
                game.num_repeat_bgm = -1
                game.current_bgm = "game_bgm"
                
                return "game"   
            elif button.text == "도움말":
                return "help"
            elif button.text == "게임 종료":
                pygame.quit()
                sys.exit()



    return "menu"
