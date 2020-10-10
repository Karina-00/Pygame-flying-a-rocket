from resources.values import *
from resources.rocket import Rocket
from resources.obstacle import Obstacle


def type_on_screen(text, size, coords=None):
    font = pygame.font.SysFont("Arial", size, bold=True)
    rend = font.render(text, 1, (255, 255, 255))
    if coords:
        SCREEN.blit(rend, coords)
        return
    x = (WIDTH - rend.get_rect().width) // 2
    y = (HEIGHT - rend.get_rect().height) // 2
    SCREEN.blit(rend, (x, y))


player = Rocket(450, 275)

for i in range(OBS_NR + 1):
    obstacles.append(Obstacle(i*WIDTH // OBS_NR, WIDTH // OBS_NR))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dy = -rocket_step
            if event.key == pygame.K_DOWN:
                dy = rocket_step
            if mode != "game" and event.key == pygame.K_SPACE:
                points = 0
                player = Rocket(350, 275)
                dy = rocket_step
                mode = "game"

    SCREEN.fill((0, 0, 0))
    if mode == "menu":
        SCREEN.blit(BACKGROUND_MENU, (0, 0))
        type_on_screen("Press SPACE to start the game", 50)
        image = pygame.image.load(os.path.join('media/rocket.png'))
        x = (WIDTH - image.get_rect().width) // 2
        SCREEN.blit(image, (x, 200))

    elif mode == "game":
        SCREEN.blit(BACKGROUND_GAME, (0, 0))
        for obstacle in obstacles:
            obstacle.movement(1)
            obstacle.draw()
            if obstacle.collision(player.rect):
                mode = "the_end"
        for obstacle in obstacles:
            if obstacle.x <= -obstacle.width:
                obstacles.remove(obstacle)
                obstacles.append(Obstacle(WIDTH, WIDTH // OBS_NR))
                points += 1
        player.draw()
        player.movement(dy)

        type_on_screen(f"Points: {points}", 20, (20, 20))

    elif mode == "the_end":
        type_on_screen(f"You got {round(points)} points, press SPACE to play again", 30)

    pygame.display.update()
