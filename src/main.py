import pygame
import sys
from intro import draw_intro_screen
from menu import draw_menu_screen
from game import draw_game_screen
from outro import draw_outro_screen
from help import draw_help_screen
from score import draw_score_screen
from utils import Game



game = Game()

# 초기 설정
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.mixer.music.set_volume(0.5)

WIDTH, HEIGHT = 1194, 834
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("교수님 몰래 딴짓하기")
font = pygame.font.Font("assets/fonts/온글잎_공부잘하자나.ttf", 70)

def load_images(image_paths, width, height):
    images = []
    for path in image_paths:
        img = pygame.image.load(path)
        img = pygame.transform.scale(img, (width, height))  # 화면 크기에 맞게 스케일링
        images.append(img)
    return images

def initialize_images(screen):
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()

    # 선생님 이미지 로드
    teaching_images = load_images([
        "assets/images/teaching1.jpg",
        "assets/images/teaching2.jpg",
        "assets/images/teaching3.jpg",
        "assets/images/teaching4.jpg",
        "assets/images/teaching5.jpg"
    ], WIDTH, HEIGHT)

    # 학생 이미지 로드
    students_images = load_images([
        "assets/images/students1.png",
        "assets/images/students2.png",
        "assets/images/students3.png",
        "assets/images/students4.png"
    ], WIDTH, HEIGHT)

    return teaching_images, students_images
teaching_images, students_images = initialize_images(screen)

current_screen = "intro"

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # BGM 전환 처리
    if game.is_changed_bgm:
        pygame.mixer.music.load("assets/sounds/"+game.current_bgm+".mp3")  
        pygame.mixer.music.play(game.num_repeat_bgm)
        game.is_changed_bgm = False  
    
    # 화면 전환 로직
    if current_screen == "intro":
        current_screen = draw_intro_screen(screen, game) 
    elif current_screen == "menu":
        current_screen = draw_menu_screen(screen, font, game, event)
    elif current_screen == "game":
        current_screen = draw_game_screen(screen, font, game, event, teaching_images, students_images)
    elif current_screen == "outro":
        current_screen = draw_outro_screen(screen, game)
    elif current_screen == "help":
        current_screen = draw_help_screen(screen, font, event)
    elif current_screen == "score":
        current_screen = draw_score_screen(screen, font, game, event)

    pygame.display.flip()

pygame.quit()
sys.exit()

pygame.quit()
sys.exit()
