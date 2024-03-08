import pygame
from constants import init_fonts, BILDSCHIRM_BREITE, BILDSCHIRM_HOEHE, WEISS, ROT, FPS, Tasten
from game_objects import LKW, Erzquelle, Lager, Tankstelle, Hubschrauberlandeplatz, Hubschrauber
from utils import start_bildschirm, pause, zeige_infos


def main():

    global endnachricht

    pygame.init()
    init_fonts()

    bildschirm = pygame.display.set_mode((BILDSCHIRM_BREITE, BILDSCHIRM_HOEHE))
    pygame.display.set_caption("ErzCollector")
    uhr = pygame.time.Clock()

    start_bildschirm(bildschirm)

    lkw = LKW()
    erz_quelle = Erzquelle()
    lager = Lager()
    tankstelle = Tankstelle()
    hubschrauberlandeplatz = Hubschrauberlandeplatz()
    hubschrauber = Hubschrauber(lkw, hubschrauberlandeplatz)

    alle_sprites = pygame.sprite.Group()
    hubschrauber_gruppe = pygame.sprite.Group()
    alle_sprites.add(lkw, erz_quelle, lager, tankstelle, hubschrauberlandeplatz, hubschrauber)
    hubschrauber_gruppe.add(hubschrauber)

    laufend = True
    pausiert = False

    start_bildschirm(bildschirm)

    while laufend:
        tasten = pygame.key.get_pressed()
        for ereignis in pygame.event.get():
            if ereignis.type == pygame.QUIT:
                laufend = False
            if ereignis.type == pygame.KEYDOWN:
                if ereignis.key == Tasten.PAUSE.value:
                    pausiert = not pausiert

        if not pausiert:
            lkw.update(tasten, erz_quelle, lager, tankstelle, hubschrauber_gruppe)
            hubschrauber_gruppe.update()

            bildschirm.fill(WEISS)
            alle_sprites.draw(bildschirm)

            info_liste = [
                f'Sprit: {int(lkw.kraftstoff)}',
                f'Erz im LKW: {lkw.erz}',
                f'Erz am Lager: {lager.erz}/{lager.kapazitaet}'
            ]
            zeige_infos(bildschirm, info_liste, 10, separate_info=f'Erz gestohlen: {lkw.gestohlenes_erz}')

        else:
            pause(bildschirm)

        pygame.display.flip()
        uhr.tick(FPS)

        endnachricht = ""

        if lkw.kraftstoff <= 0 or lkw.gestohlenes_erz > 200:
            endnachricht = "Verloren. Spiel vorbei! Neu starten? (J/N)"
            laufend = False
        elif lager.erz > 800:
            endnachricht = "Gewonnen. Spiel vorbei! Neu starten? (J/N)"
            laufend = False
        elif lager.erz == 800 and lkw.gestohlenes_erz == 200:
            endnachricht = "Unentschieden. Spiel vorbei! Neu starten? (J/N)"
            laufend = False

    if endnachricht:
        schrift_gross = pygame.font.SysFont("arial", 36)
        text_surface = schrift_gross.render(endnachricht, True, ROT)
        text_rect = text_surface.get_rect(center=(BILDSCHIRM_BREITE / 2, BILDSCHIRM_HOEHE / 2))
        bildschirm.fill(WEISS)
        bildschirm.blit(text_surface, text_rect)
        pygame.display.flip()

        auf_eingabe_warten = True
        while auf_eingabe_warten:
            for ereignis in pygame.event.get():
                if ereignis.type == pygame.KEYDOWN:
                    if ereignis.key == pygame.K_j:
                        main()
                        auf_eingabe_warten = False
                    elif ereignis.key == pygame.K_n:
                        pygame.quit()
                        return
                elif ereignis.type == pygame.QUIT:
                    pygame.quit()
                    return


if __name__ == '__main__':
    main()
