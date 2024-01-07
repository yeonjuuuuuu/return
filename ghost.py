import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 설정
screen_width, screen_height = 1280, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("연쥬르륵")

# 색깔 설정
white = (255, 255, 255)

# 유령 설정
ghost_image = pygame.image.load("D:/coding/images/ghost.png")  # "ghost.png" 파일은 적절한 이미지 파일로 대체해야 합니다.
ghost_rect = ghost_image.get_rect()
ghost_rect.topleft = (screen_width // 2, screen_height // 2)

# 이동 속도
speed = 10

# 화면 반전 여부
flipped = False

# 음악 설정
pygame.mixer.music.load("D:/coding/songs/umauma.mp3") 
pygame.mixer.music.play(-1)  # -1은 반복 재생을 의미합니다.
pygame.mixer.music.set_volume(0.05)  # 볼륨 설정 (0.0에서 1.0 사이의 값)

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ghost_rect.left > 0:
        ghost_rect.x -= speed
        flipped = False
    if keys[pygame.K_RIGHT] and ghost_rect.right < screen_width:
        ghost_rect.x += speed
        flipped = True
    if keys[pygame.K_UP] and ghost_rect.top > 0:
        ghost_rect.y -= speed
    if keys[pygame.K_DOWN] and ghost_rect.bottom < screen_height:
        ghost_rect.y += speed

    # 배경 지우기
    screen.fill(white)

    # 유령 그리기 (반전 여부에 따라 이미지를 그리기)
    if flipped:
        ghost_image_flipped = pygame.transform.flip(ghost_image, True, False)
        screen.blit(ghost_image_flipped, ghost_rect)
    else:
        screen.blit(ghost_image, ghost_rect)

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 설정
    pygame.time.Clock().tick(120)
