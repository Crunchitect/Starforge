import glob
import pygame
pygame.init()


screen = pygame.display.set_mode((300, 100))


def count_freq(pat, txt):
    M = len(pat)
    N = len(txt)
    res = 0
 
    # A loop to slide pat[] one by one
    for i in range(N - M + 1):
 
        # For current index i, check
        # for pattern match
        j = 0
        while j < M:
            if txt[i + j] != pat[j]:
                break
            j += 1
 
        if j == M:
            res += 1
    return res


def newline_count():
    newline_amount = 0
    for f in glob.glob('./**/*.py', recursive=True):
        newline_amount += 1
        with open(f, "r") as file:
            newline_amount += count_freq("\n", file.read())

    with open("../main.py", "r") as file:
        newline_amount += count_freq("\n", file.read())

    return newline_amount


running = True
while running:
    screen.fill((0, 0, 0))
    font = pygame.font.Font("../Fonts/font.ttf", 80)
    text = font.render(str(newline_count()), False, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False


print(newline_count())
