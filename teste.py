import pygame
from pygame import mixer
import os

def loop_jogo(self, soundtrack0="corona_soundtrack.mp3",
              soundtrack1="8_bit_soundtrack.mp3",
              soundtrack2="battle_soundtrack.mp3",
              menu_soundtrack="menu_soundtrack.mp3",
              tutorial_soundtrack="tutorial.mp3",
              suspense="suspense.wav",
              vencer="vencer.mp3"):

    clock = pygame.time.Clock()
    dt = 16

    self.elementos['virii'] = pygame.sprite.RenderPlain(Virus([120, 50]))
    self.jogador = Jogador([self.screen_size[0] / 6, self.screen_size[1] - 150], 5)
    self.elementos['jogador'] = pygame.sprite.RenderPlain(self.jogador)
    self.elementos['tiros'] = pygame.sprite.RenderPlain()
    self.elementos['tiros_inimigo'] = pygame.sprite.RenderPlain()

    while self.run:
        if self.painel == "morto_menu":
            menu_soundtrack = os.path.join('sons', menu_soundtrack)
            mixer.music.load(menu_soundtrack)
            mixer.music.set_volume(0.025)
            pygame.mixer.music.play(-1)
            clock.tick(1000 / dt)
            self.manutenção()
            self.atualiza_elementos(dt)
            self.desenha_elementos()
            if self.opcao == 0:  ##TELA DE MENU
                self.text.jogo_text()
                self.text.menu_text()
                self.menu_eventos()
                pygame.display.flip()

            if self.opcao == 1:  ###TELA DE GAME OVER
                self.escreve_stats()
                self.text.game_over_text()
                self.menu_eventos()
                pygame.display.flip()

        if self.painel == "tutorial_personalizar":
            clock.tick(1000 / dt)
            self.manutenção()
            self.atualiza_elementos(dt)
            self.desenha_elementos()
            tutorial_soundtrack = os.path.join('sons', tutorial_soundtrack)
            mixer.music.load(tutorial_soundtrack)
            mixer.music.set_volume(0.03)
            pygame.mixer.music.play(-1)

            if self.opcao == 2:  ###TUTORIAL
                self.text.tutorial_text()
                self.tutorial_eventos()
                pygame.display.flip()

            if self.opcao == 3:  ###PERSONALIZAR
                self.text.personalizar_text()
                self.personalizar_eventos()
                pygame.display.flip()

        if self.painel == "fases":
            clock.tick(1000 / dt)
            self.muda_nivel()
            self.trata_eventos()
            self.ação_elemento()
            self.manutenção()
            self.atualiza_elementos(dt)
            self.desenha_elementos()
            self.escreve_stats()
            self.text.sair_text()
            pygame.display.flip()

            if self.nivel == 0:
                soundtrack0 = os.path.join('sons', soundtrack0)
                mixer.music.load(soundtrack0)
                mixer.music.set_volume(0.05)
                pygame.mixer.music.play(-1)

            if self.nivel == 1:
                soundtrack1 = os.path.join('sons', soundtrack1)
                mixer.music.load(soundtrack1)
                mixer.music.set_volume(0.05)
                pygame.mixer.music.play(-1)

            if self.nivel == 2:
                soundtrack2 = os.path.join('sons', soundtrack2)
                mixer.music.load(soundtrack2)
                mixer.music.set_volume(0.05)
                pygame.mixer.music.play(-1)

            if self.nivel == 3:
                soundtrack2 = os.path.join('sons', soundtrack2)
                mixer.music.load(soundtrack2)
                mixer.music.set_volume(0.05)
                pygame.mixer.music.play(-1)


        if self.painel == "passar_nivel":
            suspense = os.path.join('sons', suspense)
            mixer.music.load(suspense)
            mixer.music.set_volume(0.025)
            pygame.mixer.music.play(-1)
            clock.tick(1000 / dt)
            self.manutenção()
            self.atualiza_elementos(dt)
            self.desenha_elementos()
            self.escreve_stats()
            self.passar_nivel_text()
            self.passar_nivel_eventos()
            pygame.display.flip()

        if self.painel == "zerou":
            vencer = os.path.join('sons', vencer)
            mixer.music.load(vencer)
            mixer.music.set_volume(0.03)
            pygame.mixer.music.play(-1)

            if self.opcao == 0:  ##TELA DE ZERAR
                clock.tick(1000 / dt)
                self.atualiza_elementos(dt)
                self.desenha_elementos()
                self.text.zerou_text()
                self.text.zerou_menu_text()
                self.zerou_eventos()
                pygame.display.flip()

            if self.opcao == 1:  ##TELA DOS CRÉDITOS
                clock.tick(1000 / dt)
                self.atualiza_elementos(dt)
                self.desenha_elementos()
                self.text.zerou_creditos_text()
                self.creditos_eventos()
                pygame.display.flip()