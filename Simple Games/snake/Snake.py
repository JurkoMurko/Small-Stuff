import pygame as pg
import random

class Block:
    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)

    num_of_blocks = 20
    offset = 0.1

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = (screen_size / Block.num_of_blocks) * ((1 - Block.offset) ** 2)

    @property
    def X(self):
        return Block.gridify(self.x)

    @property
    def Y(self):
        return Block.gridify(self.y)

    @staticmethod
    def gridify(n):
        return (screen_size / Block.num_of_blocks) * (n + Block.offset)


class SnakeBlock(Block):
    def __init__(self, x, y):
        super().__init__(x, y)

    def show(self):
        pg.draw.rect(screen, Snake.green, pg.Rect(self.X, self.Y, self.size, self.size))


class Snake(Block):
    green = (0, 255, 0)

    tail = []

    go = True

    def __init__(self, x, y, direction, length):
        super().__init__(x, y)
        self.direction = direction
        self.length = length

        self.dir_x = direction[0]
        self.dir_y = direction[1]

        self.list = []

    def move(self):
        global eat

        # for i in range(self.length):
        self.list.insert(0, [self.x, self.y])

        if len(self.list) > 0 and Food.eat == 0:
            self.list.pop(-1)

        Food.eat = 0

        self.x += self.dir_x
        self.y += self.dir_y

        # bounds detection
        if self.x > 19 or self.x < 0:
            Snake.game_over()

        if self.y > 19 or self.y < 0:
            Snake.game_over()

    def death_check(self):
        for i in self.list:
            x = self.list.count(i)
            if x > 1:
                self.game_over()

    def show(self):
        # head
        pg.draw.rect(screen, Snake.green, pg.Rect(self.X, self.Y, self.size, self.size))

        # tail
        for i in range(len(self.list)):
            yeet = Block.gridify(self.list[i][0])
            yote = Block.gridify(self.list[i][1])
            pg.draw.rect(screen, Snake.green, pg.Rect(yeet, yote, self.size, self.size))

    @ staticmethod
    def game_over():
        Snake.go = False


class Food(Block):
    red = (255, 0, 0)
    eat = 0

    def __init__(self, x, y):
        super().__init__(x, y)

    def show(self):
        pg.draw.rect(screen, Food.red, pg.Rect(self.X, self.Y, self.size, self.size))

    def eaten(self):
        if self.x == snake.x and self.y == snake.y:
            return True
        else:
            return False


pg.init()

pg.display.set_caption("Snake")

screen_size = 600
screen = pg.display.set_mode((screen_size, screen_size))
clock = pg.time.Clock()

# fonty stuff
game_over_fs = 48
score_fs = 18
game_over_font = pg.font.Font("freesansbold.ttf", game_over_fs)
score_font = pg.font.Font("freesansbold.ttf", score_fs)

# Objects
snake = Snake(10, 10, [1, 0], 0)
food = Food(random.randint(0, 19), random.randint(0, 19))

while True:
    if snake.go:
        screen.fill(Block.black)

        # Handling input
        """
        there's a bug here where you can't use the exit button after you die
        """
        for event in pg.event.get():
            # Quit
            if event.type == pg.QUIT:
                pg.quit()
                quit()

            # movement
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    snake.dir_y = -1
                    snake.dir_x = 0
                if event.key == pg.K_DOWN:
                    snake.dir_y = 1
                    snake.dir_x = 0
                if event.key == pg.K_RIGHT:
                    snake.dir_y = 0
                    snake.dir_x = 1
                if event.key == pg.K_LEFT:
                    snake.dir_y = 0
                    snake.dir_x = -1

        snake.move()

        snake.death_check()

        if food.eaten():
            food.x = random.randint(0, 19)
            food.y = random.randint(0, 19)
            snake.length += 1
            Food.eat = 1

        food.show()
        snake.show()

    elif not snake.go:
        screen.fill(Block.black)

        screen.blit(game_over_font.render("GAME OVER", False, Block.white),
                    (screen_size / 2 - 150, screen_size / 2 - game_over_fs / 2 - 100))
        screen.blit(score_font.render("SCORE:   " + str(snake.length + 1), False, Block.white),
                    (screen_size / 2 - 50, screen_size / 2 - score_fs / 2 - 20))

    # Updating the window
    pg.display.update()
    clock.tick(7)
