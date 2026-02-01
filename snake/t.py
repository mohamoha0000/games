import pygame

pygame.init()
screen = pygame.display.set_mode((500, 200))
pygame.display.set_caption("إدخال نص")

font = pygame.font.SysFont(None, 40)
text = ""

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]   # حذف آخر حرف
            else:
                text += event.unicode  # إضافة الحرف

    # عرض النص
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (20, 80))

    pygame.display.flip()

pygame.quit()
