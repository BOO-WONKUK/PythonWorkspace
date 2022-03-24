import pygame
from random import *

#################################################

# 기본 초기화 (반드시 필요)
pygame.init() 

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기 설정

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기") 

# FPS
clock = pygame.time.Clock()

#################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load("C:/Users/wkb03/Desktop/PythonWorkspace/pygame_basic/background.png")

character = pygame.image.load("C:/Users/wkb03/Desktop/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

to_x = 0

character_speed = 0.6

enemy = pygame.image.load("C:/Users/wkb03/Desktop/PythonWorkspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_y_pos = 0
enemy_x_pos = randint(0, screen_width - enemy_width)

game_font = pygame.font.Font(None, 40)

total_time = 30

start_ticks = pygame.time.get_ticks()

running = True 
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정
    
    # 2. 이벤트 처리(키보드, 마우스 등)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT : 
                to_x = 0




    # 3. 게임 캐릭터 위치 정의
    
    character_x_pos += to_x * dt
    

    if character_x_pos <= 0 :
        character_x_pos = 0

    elif character_x_pos > screen_width - character_width : 
        character_x_pos = screen_width - character_width
    
    enemy_y_pos += character_speed * dt


    if enemy_y_pos >= int(screen_height - enemy_height) : 
        enemy_y_pos = 0

    if enemy_y_pos == 0 :
        enemy_x_pos = randint(0, screen_width - enemy_width)

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0, 0)) # 배경 그리기 
    screen.blit(character,(character_x_pos, character_y_pos) ) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

    # 타이머 
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 
    # 경과 시간(ms)을 1000으로 나눠서 초(s) 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # render -> 출력할 글자, True, 글자 색상
    screen.blit(timer, (10 , 10))

    # 만약 시간이 0 이하면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임 아웃")
        running = False    

    pygame.display.update() 

pygame.quit()
