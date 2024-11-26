# Задача №1

Исследование виртуальной стековой машины CPython:
```py
import dis

def foo(x):
    while x:
        x -= 1
    return x + 1

print(dis.dis(foo))
```

![image](https://github.com/user-attachments/assets/a4cdb2d7-ec9c-48c7-914d-ee21a28ed8ed)

```
11  0 LOAD_FAST 0 (x)     --->   stack.append(x)
    2 LOAD_CONST 1 (10)   --->   stack.append(10)
    4 BINARY_MULTIPLY     --->   stack.append(x * 10)
    6 LOAD_CONST 2 (42)   --->   stack.append(42)
    8 BINARY_ADD          --->   stack.append((x * 10) + 42)
   10 RETURN_VALUE        --->   return stack.pop()
```

==> У нас результат:
```py
def func(x):
    return x * 10 + 42
```

# Задача №2

Байткод:
```
  5           0 LOAD_CONST               1 (1)   --->   stack.append(1)
              2 STORE_FAST               1 (r)   --->   r = stack.pop()

  6     >>    4 LOAD_FAST                0 (n)   --->   stack.append(n)
              6 LOAD_CONST               1 (1)   --->   stack.append(1)
              8 COMPARE_OP               4 (>)   --->   (n > 1)
             10 POP_JUMP_IF_FALSE       30       --->   if (n > 1) == False: << jump to line 30 >>

  7          12 LOAD_FAST                1 (r)   --->   stack.append(r)
             14 LOAD_FAST                0 (n)   --->   stack.append(n)
             16 INPLACE_MULTIPLY                 --->   stack[0] = r * n; stack[1] = Null
             18 STORE_FAST               1 (r)   --->   r = stack.pop()

  8          20 LOAD_FAST                0 (n)   --->   stack.append(n)
             22 LOAD_CONST               1 (1)   --->   stack.append(1)
             24 INPLACE_SUBTRACT                 --->   stack[0] = n - 1; stack[1] = Null
             26 STORE_FAST               0 (n)   --->   n = stack.pop()
             28 JUMP_ABSOLUTE            4       --->   << jump to line 4 >>

  9     >>   30 LOAD_FAST                1 (r)   --->   stack.append(r)
             32 RETURN_VALUE                     --->   return stack.pop()
```

==> У нас факториальная функция:
```py
def func(n):
    r = 1
    while True:
        if (n > 1) == False:
            break
        r *= n
        n -= 1
    return r
```

![image](https://github.com/user-attachments/assets/df70dfcf-2603-46c1-b3d5-999402d9e966)

# Задача №3

Содержимое файла Foo.java:

![Screenshot 2024-11-26 162545](https://github.com/user-attachments/assets/f196846c-ebe7-4ff7-8470-339584e5e15b)

Байткод файла Foo.java:

![Screenshot 2024-11-26 162441](https://github.com/user-attachments/assets/223d3604-5739-4192-9e85-db12cf9b6a2f)

Содержимое файла Factorial.java:

![Screenshot 2024-11-26 163047](https://github.com/user-attachments/assets/c3712c15-4020-4f1d-aaa0-ad5ecc47c4be)

Байткод файла Factorial.java:

![Screenshot 2024-11-26 162415](https://github.com/user-attachments/assets/b5c1e849-3787-4b0c-abd9-5c37eb535d92)

# Задача №4

Скачать и установить ISO-образ Alpine Linux для виртуальных машин с официального сайта:

![image](https://github.com/user-attachments/assets/e0c595e9-b0fa-46cc-b859-af52b0841081)

![image](https://github.com/user-attachments/assets/17d0e433-b051-40f2-9132-e86232bf7cf4)

Команды:

```
qemu-img create -f qcow2 alpine-disk.qcow2 500M

qemu-system-x86_64 -m 512 -cdrom /mnt/f/alpine-standard-3.20.3-x86_64.iso -hda alpine-disk.qcow2 -boot d
```
![image](https://github.com/user-attachments/assets/1c9d6966-6d1a-4afb-a61e-20fc8aafdaaa)

```
root

echo "Welcome to Alpine, Vu Duc Zuy!" > /etc/motd

exit

root
```
![image](https://github.com/user-attachments/assets/e39e56b2-59cf-4c94-959e-31596324b45c)

# Задача №5

```
import pygame
import random

colors = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]


class Figure:
    x = 0
    y = 0

    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(1, len(colors) - 1)
        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])


class Tetris:
    def __init__(self, height, width):
        self.level = 2
        self.score = 0
        self.state = "start"
        self.field = []
        self.height = 0
        self.width = 0
        self.x = 100
        self.y = 60
        self.zoom = 20
        self.figure = None
    
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def new_figure(self):
        self.figure = Figure(3, 0)

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2

    def go_space(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def go_down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.state = "gameover"

    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x

    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation


# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tetris")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
fps = 25
game = Tetris(20, 10)
counter = 0

pressing_down = False

while not done:
    if game.figure is None:
        game.new_figure()
    counter += 1
    if counter > 100000:
        counter = 0

    if counter % (fps // game.level // 2) == 0 or pressing_down:
        if game.state == "start":
            game.go_down()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                game.go_side(-1)
            if event.key == pygame.K_RIGHT:
                game.go_side(1)
            if event.key == pygame.K_SPACE:
                game.go_space()
            if event.key == pygame.K_ESCAPE:
                game.__init__(20, 10)

    if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False

    screen.fill(WHITE)

    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colors[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.image():
                    pygame.draw.rect(screen, colors[game.figure.color],
                                     [game.x + game.zoom * (j + game.figure.x) + 1,
                                      game.y + game.zoom * (i + game.figure.y) + 1,
                                      game.zoom - 2, game.zoom - 2])

    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    text = font.render("Score: " + str(game.score), True, BLACK)
    text_game_over = font1.render("Game Over", True, (255, 125, 0))
    text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))

    screen.blit(text, [0, 0])
    if game.state == "gameover":
        screen.blit(text_game_over, [20, 200])
        screen.blit(text_game_over1, [25, 265])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
```

![image](https://github.com/user-attachments/assets/40d96935-0965-47cb-abf7-3d5c89dd6115)
