import sys
import pygame


# the button of starter
def Button(screen,position,text):
    bwidth = 400
    bheight = 100
    left, top = position
    pygame.draw.line(screen, (150, 150, 150), (left, top), (left + bwidth, top), 5)
    pygame.draw.line(screen, (150, 150, 150), (left, top - 2), (left, top + bheight), 5)
    pygame.draw.line(screen, (50, 50, 50), (left, top + bheight), (left + bwidth, top + bheight), 5)
    pygame.draw.line(screen, (50, 50, 50), (left + bwidth, top + bheight), [left + bwidth, top], 5)
    pygame.draw.rect(screen, (100, 100, 100), (left, top, bwidth, bheight))

    font = pygame.font.Font(None, 50)
    text_render = font.render(text, True, (255, 105, 180))
    return screen.blit(text_render, (left + 150, top + 5))

color=(45,45,45)

#interface of the beginning
def startInterface(screen):
    screen.fill(color)
    clock = pygame.time.Clock()
    while True:
        button_1 = Button(screen, (400, 300), 'Start!')
        button_2 = Button(screen, (400, 600), 'quit')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint(pygame.mouse.get_pos()):
                    return True
                elif button_2.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit(0)
        clock.tick(60)
        pygame.display.update()

    def Interface(screen,  mode='game_start'):
        pygame.display.set_mode(cfg.SCREENSIZE)
        if mode == 'game_start':
                clock = pygame.time.Clock()
                while True:
                    screen.fill((41, 36, 33))
                    button_1 = Button(screen, (220, 150), 'START')
                    button_2 = Button(screen, (220, 250), 'QUIT')
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit(-1)
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if button_1.collidepoint(pygame.mouse.get_pos()):
                                return True
                            elif button_2.collidepoint(pygame.mouse.get_pos()):
                                pygame.quit()
                                sys.exit(-1)
                    pygame.display.update()
                    clock.tick(60)

