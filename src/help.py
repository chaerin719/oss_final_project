import pygame
from utils import Button 

def draw_help_screen(screen, font, event):
    screen.fill((50, 50, 50))  # 회색 배경
    pygame.mixer.music.pause()
    instructions = [
        "게임 방법:",
        "1. 마우스 왼쪽 클릭을 하면 점수가 오릅니다.",
        "2. 체력이 0이 되거나, 교수님이 딴짓을 확인하는 중에",
        "   클릭을 하고 있으면 게임이 종료됩니다.",
        "3. 높은 점수를 기록하세요!"
    ]   
    for idx, line in enumerate(instructions):
        text = font.render(line, True, (255, 255, 255))
        screen.blit(text, (70, 100 + idx * 100))

    button = Button(70, 650, 200, 70, "돌아가기")
    button.draw(screen, font)  
    
    if event.type == pygame.MOUSEBUTTONUP and button.is_clicked(event):
        return "menu"
    return "help"
