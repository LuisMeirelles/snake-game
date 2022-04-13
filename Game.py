import pygame
from Food import Food
from globals_ import PIXEL_SIZE, WINDOW_SIZE, WINDOW_CAPTION
from Point import Point
from Snake import Snake


class Game:
    CLOCK = 30

    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.font = pygame.font.Font('nokiafont.ttf', 20)

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(WINDOW_SIZE)

        pygame.display.set_caption(WINDOW_CAPTION)

        x = WINDOW_SIZE[0] / 2
        y = WINDOW_SIZE[1] / 2

        point = Point((x, y))

        color = pygame.Color(255, 0, 0)

        self.snake = Snake(point, color)

        self.food = Food((0, self.font.get_height() + 20))

    def run(self):
        while True:
            self.can_move = True

            if self.is_dead():
                break

            self.screen.fill((51, 51, 51))

            self.show_food()
            self.handle_events()
            self.snake.update()

            self.show_snake()

            self.eat_food()

            self.generate_grid()

            self.show_score()

            self.clock.tick(self.CLOCK)

            pygame.display.update()

        pygame.quit()
        quit()

    def is_dead(self):
        text_height = (self.font.get_height() + 20) // PIXEL_SIZE * PIXEL_SIZE

        not_top = self.snake.position.y >= text_height
        not_bottom = self.snake.position.y <= WINDOW_SIZE[1] - PIXEL_SIZE
        not_left = self.snake.position.x >= 0
        not_right = self.snake.position.x <= WINDOW_SIZE[0] - PIXEL_SIZE

        valid_position = not_top and not_bottom and not_left and not_right

        if self.snake.position in self.snake.tail:
            valid_position = False

        return not valid_position

    def generate_grid(self):
        text_height = (self.font.get_height() + 20) // PIXEL_SIZE * PIXEL_SIZE

        for col in range(0, WINDOW_SIZE[0], PIXEL_SIZE):
            pygame.draw.rect(
                self.screen,
                (25, 25, 25),
                (col, text_height, 1, WINDOW_SIZE[1])
            )

        for row in range(text_height, WINDOW_SIZE[1], PIXEL_SIZE):
            pygame.draw.rect(
                self.screen,
                (25, 25, 25),
                (0, row, WINDOW_SIZE[0], 1)
            )

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if self.can_move:
                    self.move_snake(event.key)
                    self.can_move = False

    def move_snake(self, key):
        match key:
            case pygame.K_UP:
                if self.snake.velocity.y != 1:
                    self.snake.move_up()
            case pygame.K_DOWN:
                if self.snake.velocity.y != -1:
                    self.snake.move_down()
            case pygame.K_LEFT:
                if self.snake.velocity.x != 1:
                    self.snake.move_left()
            case pygame.K_RIGHT:
                if self.snake.velocity.x != -1:
                    self.snake.move_right()

    def show_snake(self):
        w = PIXEL_SIZE
        h = PIXEL_SIZE

        for rect in self.snake.tail:
            x = rect.x
            y = rect.y

            pygame.draw.rect(self.screen, self.snake.color, (x, y, w, h))

        x = self.snake.position.x
        y = self.snake.position.y

        pygame.draw.rect(self.screen, self.snake.color, (x, y, w, h))

    def show_food(self):
        color = (0, 0, 255)

        x = self.food.position.x
        y = self.food.position.y
        w = PIXEL_SIZE
        h = PIXEL_SIZE

        rect_value = (x, y, w, h)

        pygame.draw.rect(self.screen, color, rect_value)

    def eat_food(self):
        distance = self.food.position - self.snake.position

        if distance == Point((0, 0)):
            self.snake.eat(self.food)

    def show_score(self):
        text = self.font.render(f'Score: {self.snake.total}', False, (255, 255, 255))
        text_x = (WINDOW_SIZE[0] // 2) - (text.get_width() // 2)

        self.screen.blit(text, (text_x, 10))
