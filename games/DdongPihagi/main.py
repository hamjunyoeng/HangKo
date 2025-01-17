import pygame, sys, os, random

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (150, 150, 150)

current_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
imamge_path = os.path.join(current_path, "images")  # images 폴더 위치 반환
record_path = os.path.join(current_path, 'record.txt')

def draw_score(SCORE):
    font_01 = pygame.font.SysFont("FixedSsy", 30, True, False)
    text_score = font_01.render("Score : " + str(SCORE), True, BLACK)
    screen.blit(text_score, [15, 15])

def gameStart():

    pygame.init()

    state = 0
    SCORE = 0

    global screen
    # 화면 크기 정보
    SCREEN_WIDTH = 720
    SCREEN_HEIGHT = 720

    # 파이게임 초기화 및 화면 크기 지정
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # 데이터 로드
    background_image = pygame.image.load(os.path.join(imamge_path, "background.png"))
    platform_image = pygame.image.load(os.path.join(imamge_path, "platform.png"))
    player_image = pygame.image.load(os.path.join(imamge_path, "man.png"))
    ddong_image = pygame.image.load(os.path.join(imamge_path, "ddong.png"))

    # 바닥 초기화
    platform_height = platform_image.get_size()[1]
    platform_pos_y = SCREEN_HEIGHT - platform_height

    # 플레이어 초기화
    player_width = player_image.get_size()[0]
    player_height = player_image.get_size()[1]
    player_pos_x = SCREEN_WIDTH / 2 - player_width / 2
    player_pos_y = SCREEN_HEIGHT - player_height - platform_height

    # 똥 초기화
    ddong_width = ddong_image.get_size()[0]
    ddong_height = ddong_image.get_size()[1]
    ddong_pos_x = random.randint(0, SCREEN_WIDTH - ddong_width+1)
    ddong_pos_y = -2*random.randint(ddong_height, 300)

    ddong_2_width = ddong_image.get_size()[0]
    ddong_2_height = ddong_image.get_size()[1]
    ddong_2_pos_x = random.randint(0, SCREEN_WIDTH - ddong_width+1)
    ddong_2_pos_y = -random.randint(ddong_height, 300)

    ddong_3_width = ddong_image.get_size()[0]
    ddong_3_height = ddong_image.get_size()[1]
    ddong_3_pos_x = random.randint(0, SCREEN_WIDTH - ddong_width+1)
    ddong_3_pos_y = -3*random.randint(ddong_height, 300)



    # 게임 루프를 제어하는 변수
    is_running = True

    # 시계 객체 생성
    clock = pygame.time.Clock()


    # 게임 루프 시작
    while is_running:
        clock.tick(60)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                state = 1

        # 업데이트
        key = pygame.key.get_pressed()

        # 왼쪽 방향키 -> 왼쪽 이동
        if key[pygame.K_LEFT] == 1:
            player_pos_x -= 700 * clock.get_time() / 1000

        # 오른쪽 방향키 -> 오른쪽으로 이동
        if key[pygame.K_RIGHT] == 1:
            player_pos_x += 700 * clock.get_time() / 1000

        if player_pos_x < 0:
            player_pos_x = 0

        if player_pos_x > SCREEN_WIDTH - player_width:
            player_pos_x = SCREEN_WIDTH - player_width

        # 똥이 떨어지게 설정
        ddong_pos_y += 700 * clock.get_time() / 1000
        ddong_2_pos_y += 700 * clock.get_time() / 1000
        ddong_3_pos_y += 700 * clock.get_time() / 1000

        if ddong_pos_y > SCREEN_HEIGHT - platform_height - ddong_height:
            SCORE += 10
            ddong_pos_x = random.randint(0, SCREEN_WIDTH - ddong_width + 1)
            ddong_pos_y = -2*random.randint(ddong_height, 500)

        if ddong_2_pos_y > SCREEN_HEIGHT - platform_height - ddong_2_height :
            SCORE += 10
            ddong_2_pos_x = random.randint(0, SCREEN_WIDTH - ddong_2_width + 1)
            ddong_2_pos_y = -random.randint(ddong_2_height, 200)

        if ddong_3_pos_y > SCREEN_HEIGHT - platform_height - ddong_3_height :
            SCORE += 10
            ddong_3_pos_x = random.randint(0, SCREEN_WIDTH - ddong_3_width + 1)
            ddong_3_pos_y = -3*random.randint(ddong_3_height, 200)

        # 각종 처리(충돌)
        player_rect = player_image.get_rect()
        player_rect.x = player_pos_x
        player_rect.y = player_pos_y

        ddong_rect = ddong_image.get_rect()
        ddong_2_rect = ddong_image.get_rect()
        ddong_3_rect = ddong_image.get_rect()

        ddong_2_rect.x = ddong_2_pos_x
        ddong_2_rect.y = ddong_2_pos_y
        ddong_rect.x = ddong_pos_x
        ddong_rect.y = ddong_pos_y
        ddong_3_rect.y = ddong_3_pos_y
        ddong_3_rect.x = ddong_3_pos_x

        # 충돌 검사
        isEnd = False
        if player_rect.colliderect(ddong_rect):
            isEnd = True
        elif player_rect.colliderect(ddong_2_rect):
            isEnd = True
        elif player_rect.colliderect(ddong_3_rect):
            isEnd = True

        #랜더(그리기)
        screen.blit(background_image, (0, 0))
        screen.blit(player_image, (player_pos_x, player_pos_y))
        screen.blit(ddong_image, (ddong_pos_x, ddong_pos_y))
        screen.blit(ddong_image, (ddong_2_pos_x, ddong_2_pos_y))
        screen.blit(ddong_image, (ddong_3_pos_x, ddong_3_pos_y))

        # 디스플레이 업데이트
        draw_score(SCORE)
        pygame.display.update()

        if isEnd:
            is_running = False

            screen.fill(WHITE)

            gameOverFont = pygame.font.SysFont("FixedSsy", 100, True, False)
            gameOverText = gameOverFont.render("GAME OVER", True, BLACK)
            gameOverRect = gameOverText.get_rect()
            gameOverRect.center = (360, 300)
            screen.blit(gameOverText, gameOverRect)

            scoreFont = pygame.font.SysFont("FixedSsy", 52, True, False)
            scoreText = scoreFont.render('score   ' + str(SCORE), True, BLACK)
            scoreRect = scoreText.get_rect()
            scoreRect.center = (360, 400)
            screen.blit(scoreText, scoreRect)

            pygame.display.update()
            pygame.time.delay(2000)

    saveRecord(loadRecord(), SCORE)
    return state


def loadRecord():
    currentPath = os.path.dirname(__file__) # 현재 파일의 위치 반환
    file = open(os.path.join(currentPath, 'record.txt'), 'r')

    high = file.readline()

    file.close()

    return high

def saveRecord(high, record):   # record는 항상 int
    if high == '' or int(high) < int(record):
        currentPath = os.path.dirname(__file__) # 현재 파일의 위치 반환
        file = open(os.path.join(currentPath, 'record.txt'), 'w')

        file.write(str(record))

        file.close()