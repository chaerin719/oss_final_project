import pygame
import random

# 게임 상태
class Game:
    def __init__(self):
        self.health = 200
        self.score = 0
        self.teacher_state = "back"
        self.teacher_timer = 0
        self.current_bgm = None
        self.is_changed_bgm = False
        self.num_repeat_bgm = 0
        
    def reset(self):
        self.health = 200
        self.score = 0
        self.teacher_state = "back"
        self.teacher_timer = 0

    def update_teacher(self, dt, current_frame):
        self.teacher_timer += dt

        if self.teacher_state == "back":
            if self.teacher_timer > random.randint(1000, 5000):
                self.teacher_state = "turn"
                self.teacher_timer = 0



    def check_player_action(self, is_mouse_pressed, teaching_current_frame):
        if self.teacher_state == "turn" and is_mouse_pressed:
            if teaching_current_frame == 4:
                pygame.event.clear()
                pygame.mixer.music.pause()
                self.current_bgm = "outro_bgm"
                self.is_changed_bgm = True
                return "outro"
        if self.health == 0:
           return "outro"
        
        if teaching_current_frame != 4 and is_mouse_pressed:
            if self.health <= 200:
                self.health += 1
            self.score += 1
        else:
            self.health -= 1
        
        return "game"

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        

    def draw(self, screen, font):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos):
                return True
        return False
