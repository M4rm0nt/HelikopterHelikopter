import os
import pygame
from constants import SCHWARZ, BILDSCHIRM_BREITE, BILDSCHIRM_HOEHE, BILDER_VERZEICHNIS


def bild_laden(name):
    pfad = os.path.join(BILDER_VERZEICHNIS, f'{name}.png')
    return pygame.image.load(pfad)


def zeige_infos(BILDSCHIRM, info_liste, y_start, y_offset_separate_info=None, separate_info=None):
    schrift_klein = pygame.font.SysFont("arial", 25)
    gesamtbreite = sum([schrift_klein.render(info, True, SCHWARZ).get_width() + 10 for info in
                        info_liste]) - 10
    start_x = (BILDSCHIRM_BREITE - gesamtbreite) // 2

    for info in info_liste:
        text_surface = schrift_klein.render(info, True, SCHWARZ)
        BILDSCHIRM.blit(text_surface, (start_x, y_start))
        start_x += text_surface.get_width() + 10

    if separate_info is not None:
        if y_offset_separate_info is None:
            y_offset_separate_info = BILDSCHIRM_HOEHE - 30
        separate_text_surface = schrift_klein.render(separate_info, True, SCHWARZ)
        separate_text_rect = separate_text_surface.get_rect(midbottom=(BILDSCHIRM_BREITE // 2, y_offset_separate_info))
        BILDSCHIRM.blit(separate_text_surface, separate_text_rect)


def start_bildschirm(BILDSCHIRM):

    schrift_gross = pygame.font.SysFont("arial", 36)
    schrift_klein = pygame.font.SysFont("arial", 25)
    start = True
    while start:
        for ereignis in pygame.event.get():
            if ereignis.type == pygame.QUIT:
                pygame.quit()
                quit()
            if ereignis.type == pygame.KEYDOWN:
                if ereignis.key == pygame.K_SPACE:
                    start = False

        BILDSCHIRM.fill((255, 255, 255))
        titel_text = schrift_gross.render("ErzCollector", True, SCHWARZ)
        BILDSCHIRM.blit(titel_text, (100, 200))
        info_text = schrift_klein.render("Sammle Erz, meide Hubschrauber.", True, SCHWARZ)
        BILDSCHIRM.blit(info_text, (100, 300))
        info_text = schrift_klein.render("Starte mit Leertaste.", True, SCHWARZ)
        BILDSCHIRM.blit(info_text, (100, 400))
        info_text = schrift_klein.render("Für die Optionen zu sehen, drücke 'P' im Spiel.", True, SCHWARZ)
        BILDSCHIRM.blit(info_text, (100, 500))
        pygame.display.flip()
        pygame.time.Clock().tick(15)


def pause(BILDSCHIRM):
    pausiert = True
    while pausiert:
        for ereignis in pygame.event.get():
            if ereignis.type == pygame.QUIT:
                pygame.quit()
                quit()
            if ereignis.type == pygame.KEYDOWN:
                if ereignis.key == pygame.K_c:
                    pausiert = False
                elif ereignis.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif ereignis.key == pygame.K_p:
                    pausiert = False

        BILDSCHIRM.fill((255, 255, 255))
        pause_text = pygame.font.SysFont("arial", 36).render("Pause", True, SCHWARZ)
        BILDSCHIRM.blit(pause_text, (BILDSCHIRM_BREITE // 2 - pause_text.get_width() // 2, 100))

        ziele_start_y = 200
        steuerung = [
            "Steuerung",
            "Pfeiltasten oder WASD"
        ]
        for index, element in enumerate(steuerung):
            zeige_infos(BILDSCHIRM, [element], ziele_start_y + index * 30)

        ziele_start_y = 300
        ziele = [
            "Spielziele:",
            "- Sammle Erz von der Erzquelle.",
            "- Bringe das Erz zum Abladeplatz.",
            "- Vermeide Kollisionen mit Hubschraubern.",
            "- Du verlierst, wenn der Hubschrauber mehr als 20% des Erzes besitzt.",
            "- Halte den Kraftstoffvorrat im Auge."
        ]
        for index, ziel in enumerate(ziele):
            zeige_infos(BILDSCHIRM, [ziel], ziele_start_y + index * 30)

        options_start_y = 500
        options = [
            "- Drücke 2 mal 'P' zum Weiterspielen oder 'Q' zum Beenden."
        ]
        zeige_infos(BILDSCHIRM, options, options_start_y)

        pygame.display.flip()
        pygame.time.Clock().tick(5)

