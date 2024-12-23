import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)



# 수업 화면 함수
def draw_game_screen(screen, font, game, event, teaching_images, students_images):
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    
    # 현재 시간 계산
    dt = pygame.time.Clock().tick(60)  # 프레임 간 시간 계산
    current_time = pygame.time.get_ticks()  # 현재 시간(ms)
    
    # 초기화
    screen.fill(WHITE)

    # 선생님 애니메이션 상태 관리
    if not hasattr(game, "last_teacher_frame_time"):
        game.last_teacher_frame_time = current_time
    if not hasattr(game, "teaching_current_frame"):
        game.teaching_current_frame = 0

    if game.teaching_current_frame != 4 and pygame.mouse.get_pressed()[0]:
        if game.current_bgm != "videotape":
            game.current_bgm = "videotape"
            game.num_repeat_bgm = -1
            game.is_changed_bgm = True
    else:
        if game.current_bgm != "game_bgm":
            game.current_bgm = "game_bgm"
            game.num_repeat_bgm = -1
            game.is_changed_bgm = True

    teacher_frame_duration = 200  # 선생님 프레임 지속 시간(ms)

    # 프레임 전환 타이머
    time_since_last_teacher_frame = current_time - game.last_teacher_frame_time

    if game.teacher_state == "turn":
        if game.teaching_current_frame == 4:
            if time_since_last_teacher_frame > random.randint(1000,5000):
                game.teacher_state = "back"
                game.teacher_timer = 0
                game.last_teacher_frame_time = current_time
        else:
            if game.teaching_current_frame == 0:
                game.teaching_current_frame = 1
            if current_time - game.last_teacher_frame_time >= teacher_frame_duration:
                game.teaching_current_frame = 1 + ((game.teaching_current_frame) % (len(teaching_images)-1))
                game.last_teacher_frame_time = current_time
    else:
        if time_since_last_teacher_frame >= teacher_frame_duration:
            game.teaching_current_frame = 1 if game.teaching_current_frame == 0 else 0 
            game.last_teacher_frame_time = current_time

    # 학생 애니메이션 상태 관리
    if not hasattr(game, "last_student_frame_time"):
        game.last_student_frame_time = current_time
    if not hasattr(game, "student_current_frame"):
        game.student_current_frame = 0

    student_frame_duration = 200  # 학생 프레임 지속 시간(ms)

    # 프레임 전환 타이머
    time_since_last_student_frame = current_time - game.last_student_frame_time

    if pygame.mouse.get_pressed()[0]:  # 마우스가 눌려 있는 경우
        if time_since_last_student_frame >= student_frame_duration:
            game.student_current_frame = 1+((game.student_current_frame) % (len(students_images)-1))
            game.last_student_frame_time = current_time
    else:
        game.student_current_frame = 0

    # 이미지 그리기
    screen.blit(teaching_images[game.teaching_current_frame], (0, 0))  # 선생님 이미지
    screen.blit(students_images[game.student_current_frame], (0, 0))  # 학생 이미지

    # 체력바 표시
    pygame.draw.rect(screen, RED, (10, 10, 2*200, 20))
    pygame.draw.rect(screen, GREEN, (10, 10, 200 * (game.health / 100), 20))

    # 점수 표시
    score_text1 = font.render("점수", True, BLACK)
    score_text2 = font.render(f"{game.score}", True, BLACK)
    screen.blit(score_text1, (WIDTH - 140, 0))
    screen.blit(score_text2, (WIDTH - 140, 70))

    # 선생님 상태 업데이트
    game.update_teacher(dt, game.teaching_current_frame)

    # 플레이어 행동 처리
    is_mouse_pressed = pygame.mouse.get_pressed()[0]
    next_state = game.check_player_action(is_mouse_pressed, game.teaching_current_frame)

    # 화면 업데이트
    pygame.display.flip()

    return next_state
