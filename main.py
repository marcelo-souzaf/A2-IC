import pygame
from pygame import mixer
import os
from pygame.locals import (DOUBLEBUF,
                           USEREVENT,
                           FULLSCREEN,
                           KEYDOWN, KEYUP,
                           K_DOWN, K_s,
                           K_UP, K_w,
                           K_LEFT, K_a,
                           K_RIGHT, K_d,
                           K_p,
                           QUIT,
                           K_ESCAPE, K_RCTRL, K_LCTRL, K_SPACE,
                           K_1, K_2, K_3, K_4,K_5
                           )


from fundo import Fundo
from boss import Boss
from Jogador_Virus import Jogador, Virus
from textos import Textos
SHOOTEVENT = USEREVENT + 1
BOSSEVENT = USEREVENT + 2
BOSSATTACK = USEREVENT + 3
import random

class Jogo:
    def __init__(self, size=(850, 800), fullscreen=False, icon="virus_orange.png"):
        self.elementos = {}
        pygame.font.init()
        pygame.init()
        flags = pygame.DOUBLEBUF
        if fullscreen:
            flags |= FULLSCREEN
        self.tela = pygame.display.set_mode(size, flags=flags, depth=16)
        self.fundo = Fundo()
        self.text = Textos()
        self.jogador = None
        self.boss = None
        self.nivel = 0
        heart = pygame.image.load(os.path.join('imagens', 'vida.png')).convert_alpha()
        self.heart = pygame.transform.scale(heart, (25, 25))

        self.opcao = 0
        self.painel = "morto_menu"

        self.fonte = pygame.font.SysFont("monospace", 32)
        self.menu_font = pygame.font.SysFont("freesansbold.ttf", 32)
        self.nivel_font = pygame.font.SysFont("freesansbold.ttf", 42)

        self.screen_size = self.tela.get_size()
        pygame.mouse.set_visible(1)
        pygame.display.set_caption('Corona Shooter')
        icon = os.path.join('imagens', icon)
        icon = pygame.image.load(icon).convert_alpha()
        pygame.display.set_icon(icon)
        self.run = True

    def escreve_stats(self):
        vidas = self.fonte.render('Vidas: ', 1, (255, 255, 0))
        fase = self.fonte.render(f'Fase: {self.nivel}', 1, (255, 255, 0))
        score = self.fonte.render(f'Score: {self.jogador.pontos}', 1, (255, 255, 0))
        for i in range(self.jogador.get_lives()):
            self.tela.blit(self.heart, [140 + (30 * i), 26])
        self.tela.blit(vidas, (self.screen_size[0]/34, self.screen_size[1]/40))
        self.tela.blit(fase, (self.screen_size[0] - self.screen_size[0]/2.5, self.screen_size[1]/40))
        self.tela.blit(score, (self.screen_size[0] - self.screen_size[0]/4.5, self.screen_size[1]/40))

    def passar_nivel_text(self):
        passar_nivel_text = self.nivel_font.render(f'PARABÉNS, VOCÊ PASSOU DA FASE {self.nivel-1}!', 1, (255, 255, 255))
        self.tela.blit(passar_nivel_text, (self.screen_size[0]/2 - self.screen_size[0]/3,self.screen_size[1]/2.5))
        proximo = self.menu_font.render("Próxima Fase  (1)", 1, (255, 255, 255))
        menu = self.menu_font.render("Volte para o Menu  (2)", 1, (255, 255, 255))
        sair = self.menu_font.render("Sair  (3)", 1, (255, 255, 255))
        self.tela.blit(proximo, (self.screen_size[0]/2 - self.screen_size[0]/3, self.screen_size[1]/2))
        self.tela.blit(menu, (self.screen_size[0]/2 - self.screen_size[0]/3, (self.screen_size[1]/2)+40))
        self.tela.blit(sair, (self.screen_size[0]/2 - self.screen_size[0]/3, (self.screen_size[1]/2)+80))

    # Gera um número definido de vírus de acordo com a fase e altera seus atributos
    def manutenção(self):
        r = random.randint(0, 4*(1+(self.nivel/2)))
        x = random.randint(1, self.screen_size[0])
        virii = self.elementos["virii"]
        if r > len(virii):
            if self.nivel < 2:
                enemy = Virus([0, 0])
            if self.nivel == 2:
                enemy = Virus([0, 0], speed = [0,3])
            elif self.nivel >= 3:
                enemy = Virus([0, 0], speed = [0,3], lives = 2)
            size = enemy.get_size()
            enemy.set_pos([min(max(x, size[0] / 2), self.screen_size[0] - size[0] / 2), size[1] / 2])
            colisores = pygame.sprite.spritecollide(enemy, virii, False)
            colisores2 = pygame.sprite.spritecollide(enemy, self.elementos['boss'], False)
            if colisores or colisores2:
                return
            self.elementos["virii"].add(enemy)

    def muda_nivel(self):
        xp = self.jogador.get_pontos()
        if xp >= 50 and self.nivel == 0:
            self.fundo = Fundo("space_fase1.png")
            self.nivel = self.nivel + 1
            self.painel = "passar_nivel"
            self.loop_musica_passar_zerar()

        elif xp >= 150 and self.nivel == 1:
            self.fundo = Fundo("space_fase2.png")
            self.nivel = self.nivel + 1
            self.painel = "passar_nivel"
            self.loop_musica_passar_zerar()

        elif xp >= 300 and self.nivel == 2:
            self.fundo = Fundo("space_fase3.png")
            self.nivel = self.nivel + 1
            self.painel = "passar_nivel"
            self.loop_musica_passar_zerar()
            
        elif xp >= 500 and self.nivel == 3:
            self.fundo = Fundo("fundo_boss.png")
            self.nivel = self.nivel + 1
            self.painel = "passar_nivel"
            self.loop_musica_passar_zerar()

    def atualiza_elementos(self, dt):
        self.fundo.update()
        for v in self.elementos.values():
            v.update(dt)

    def desenha_elementos(self):
        self.fundo.draw(self.tela)
        for v in self.elementos.values():
            v.draw(self.tela)

    def verifica_impactos(self, elemento, list, action):
        if isinstance(elemento, pygame.sprite.RenderPlain):
            hitted = pygame.sprite.groupcollide(elemento, list, 1, 0)
            for v in hitted.values():
                for o in v:
                    action(o)
            return hitted

        elif isinstance(elemento, pygame.sprite.Sprite):
            if pygame.sprite.spritecollide(elemento, list, 1):
                action()
            return elemento.morto

    # Executa as ações dos elementos do jogo.
    def ação_elemento(self, explosionSound="short_explosion.wav", game_over="game_over.wav"):
        
        # Move os vírus em direção ao jogador quando eles se aproximam
        for virus in self.elementos['virii']:
            if 0 < virus.get_pos()[0] - self.jogador.get_pos()[0] < 200:
                virus.rect.move_ip(-1,0)
            elif -200 < virus.get_pos()[0] - self.jogador.get_pos()[0] < 0:
                virus.rect.move_ip(1,0)
                
        for boss in self.elementos['boss']:
            if 0 < boss.get_pos()[0] - self.jogador.get_pos()[0] < 200:
                boss.rect.move_ip(-2,0)
            elif -200 < boss.get_pos()[0] - self.jogador.get_pos()[0] < 0:
                boss.rect.move_ip(2,0)
                
        # Verifica se o personagem foi alvejado pelo boss
        self.verifica_impactos(self.jogador, self.elementos["tiros_inimigo"],
                               self.jogador.alvejado)

        # Verifica se o personagem trombou em algum inimigo
        self.verifica_impactos(self.jogador, self.elementos["virii"],
                               self.jogador.colisão)
        if self.nivel == 4:
            self.verifica_impactos(self.jogador, self.elementos['boss'],
                               self.jogador.colisão)
            hitted_boss = self.verifica_impactos(self.elementos['tiros'], self.elementos['boss'],
                                                 Boss.alvejado)
            if hitted_boss:
                hit_sound = pygame.mixer.Sound(os.path.join('sons', 'pain.wav'))
                hit_sound.set_volume(0.05)
                hit_sound.play()
                for boss in hitted_boss.values():
                    if boss[0].get_lives() <= 0:
                        boss[0].kill()
                        self.fundo = Fundo("space_zerou.png")
                        self.painel = "zerou"
                        self.loop_musica_passar_zerar()
        
        if self.jogador.morto:
            game_over = os.path.join('sons', game_over)
            game_over = pygame.mixer.Sound(game_over)
            game_over.set_volume(0.08)
            game_over.play()
            self.opcao = 1
            self.painel = "morto_menu"
            self.loop_musica_menu()
            return

        # Verifica se o personagem atingiu algum alvo.
        hitted = self.verifica_impactos(self.elementos["tiros"],
                                        self.elementos["virii"],
                                        Virus.alvejado)
        
        if hitted:
            explosionSound = os.path.join('sons', explosionSound)
            explosionSound = pygame.mixer.Sound(explosionSound)
            explosionSound.set_volume(0.07)
            explosionSound.play()
        

        # Aumenta o número de pontos de acordo com quantidade atingida.
        self.jogador.set_pontos(self.jogador.get_pontos() + len(hitted))

    # Faz a leitura dos eventos definidos por elementos do jogo ou pelo jogador
    def trata_eventos(self):
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            self.run = False
        if event.type == SHOOTEVENT:
            self.jogador.atira(self.elementos["tiros"])
        if event.type == BOSSEVENT:
            global asa
            imagem0 = pygame.image.load(os.path.join('imagens','bat0.png')).convert_alpha()
            imagem1 = pygame.image.load(os.path.join('imagens','bat1.png')).convert_alpha()
            for boss in self.elementos['boss']:
                if asa:
                    asa = not asa
                    boss.image = imagem1
                else:
                    asa = not asa
                    boss.image = imagem0
                        
        if event.type == BOSSATTACK:
            for boss in self.elementos['boss']:
                boss.boss_atira(self.elementos['tiros_inimigo'])
            
        if event.type == KEYDOWN:
            key = event.key
            # Encerra o jogo
            if key == K_ESCAPE:
                self.run = False
            # Adiciona um leve atraso na ação de disparar
            elif key == K_SPACE:
                pygame.time.set_timer(SHOOTEVENT, 150, loops = 1)
            # Pausa o jogo
            if key == K_p:
                if self.painel == "fases":
                    pause = True
                    pygame.mixer.music.pause()
                    while pause:
                        event = pygame.event.poll()
                        self.text.pausado_text()
                        pygame.display.flip()
                        if event.type == KEYDOWN:
                            if event.key == K_p:
                                pause = False
                                pygame.mixer.music.unpause()
                                
        # Move o jogador
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] or keys[K_a]:
            self.jogador.rect.move_ip(-8,0)
        if keys[K_RIGHT] or keys[K_d]:
            self.jogador.rect.move_ip(8,0)
        if keys[K_UP] or keys[K_w]:
            self.jogador.rect.move_ip(0,-4)
        if keys[K_DOWN] or keys[K_s]:
            self.jogador.rect.move_ip(0,4)

    def menu_eventos(self):
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            self.run = False
        if event.type == KEYUP:
            if self.opcao == 0:
                key = event.key
                if key == K_1:
                    self.jogador.set_lives(5)
                    self.nivel = 0
                    self.jogador.pontos = 0
                    self.painel = "fases"
                    self.loop_musica_fase_0_1()
                elif key == K_2:
                    self.opcao = 2
                    self.painel = "tutorial_personalizar"
                    self.loop_musica_personalizar_tutorial()
                elif key == K_3:
                    self.opcao = 3
                    self.painel = "tutorial_personalizar"
                    self.loop_musica_personalizar_tutorial()
                elif key in (K_ESCAPE, K_4):
                    self.run = False

            if self.opcao == 1: #TELA DE GAME OVER
                key = event.key
                if key == K_1:
                    self.fundo = Fundo("sky_fase0.png")
                    self.loop_musica_menu()
                    self.opcao = 0
                elif key == K_2:
                    self.run = False


    def tutorial_eventos(self):
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            self.run = False
        if event.type == KEYUP:
            key = event.key
            if key == K_4:
                self.opcao = 0
                self.painel = "morto_menu"
                self.loop_musica_menu()
            elif key == K_ESCAPE:
                self.run = False

    def personalizar_eventos(self):
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            self.run = False
        if event.type == KEYUP:
            key = event.key
            if key == K_1:
                self.jogador.set_image_roxo()
            elif key == K_2:
                self.jogador.set_image_verm()
            elif key == K_3:
                self.jogador.set_image_rosa()
            elif key == K_4:
                self.jogador.set_image_azul()
            if key == K_5:
                self.opcao = 0
                self.painel = "morto_menu"
                self.loop_musica_menu()
            elif key == K_ESCAPE:
                self.run = False

    def passar_nivel_eventos(self):
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            self.run = False
        if event.type == KEYUP:
            key = event.key
            if key == K_1 and self.nivel == 1:
                self.painel = "fases"
                self.loop_musica_fase_0_1()
            elif key == K_1 and self.nivel == 2:
                self.painel = "fases"
                self.loop_musica_fase_2_3_4()
            elif key == K_1 and self.nivel == 3:
                self.painel = "fases"
                self.loop_musica_fase_2_3_4()
            elif key == K_1 and self.nivel == 4:
                global asa
                self.painel = "fases"
                self.loop_musica_fase_2_3_4()
                self.elementos['boss'].add(Boss([self.screen_size[0]/2, 100], image = 'bat0.png'))
                pygame.time.set_timer(BOSSEVENT, 500, 0)
                pygame.time.set_timer(BOSSATTACK, 1250, 0)
                asa = True
            if key == K_2:
                self.fundo = Fundo("sky_fase0.png")
                self.nivel = 0
                self.loop_musica_menu()
                self.painel = "morto_menu"  
            elif key in (K_3, K_ESCAPE):
                self.run = False

    def zerou_eventos(self):
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            self.run = False
        if event.type == KEYUP:
            key = event.key
            if key == K_1:
                self.fundo = Fundo("sky_fase0.png")
                self.painel = "morto_menu"
                self.loop_musica_menu()
            elif key == K_2:
                self.opcao = 1
            elif key in (K_3, K_ESCAPE):
                self.run = False

    def creditos_eventos(self):
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            self.run = False
        if event.type == KEYUP:
            key = event.key
            if key == K_4:
                self.opcao = 0
            elif key == K_ESCAPE:
                self.run = False


    def loop_jogo(self, menu_soundtrack="menu_soundtrack.mp3"):
        clock = pygame.time.Clock()
        dt = 16

        self.elementos['virii'] = pygame.sprite.RenderPlain(Virus([120, 50]))
        self.jogador = Jogador([self.screen_size[0]/6, self.screen_size[1]-150], 5)
        self.elementos['jogador'] = pygame.sprite.RenderPlain(self.jogador)

        self.elementos['tiros'] = pygame.sprite.RenderPlain()
        self.elementos['tiros_inimigo'] = pygame.sprite.RenderPlain()
        self.elementos['boss'] = pygame.sprite.RenderPlain()

        if self.painel == "morto_menu":
            menu_soundtrack = os.path.join('sons', menu_soundtrack)
            mixer.music.load(menu_soundtrack)
            mixer.music.set_volume(0.025)
            pygame.mixer.music.play(-1)

        if self.painel == "tutorial_personalizar":
            self.jogador = Jogador([self.screen_size[0] / 6, self.screen_size[1] - 150], 5)
            self.elementos['jogador'] = pygame.sprite.RenderPlain(self.jogador)

        if self.painel == "fases":
            self.elementos['virii'] = pygame.sprite.RenderPlain(Virus([120, 50]))
            self.jogador = Jogador([self.screen_size[0] / 6, self.screen_size[1] - 150], 5)
            self.elementos['jogador'] = pygame.sprite.RenderPlain(self.jogador)

        if self.painel == "passar_nivel":
            self.jogador = Jogador([self.screen_size[0] / 6, self.screen_size[1] - 150], 5)
            self.elementos['jogador'] = pygame.sprite.RenderPlain(self.jogador)

        while self.run:
            if self.painel == "morto_menu":
                clock.tick(1000 / dt)
                self.manutenção()
                self.atualiza_elementos(dt)
                self.desenha_elementos()
                if self.opcao == 0:  ###TELA DE MENU
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

            if self.painel == "passar_nivel":
                clock.tick(1000 / dt)
                self.elementos['virii'].empty()
                self.elementos['tiros'].empty()
                self.fundo.update()
                self.desenha_elementos()
                self.escreve_stats()
                self.passar_nivel_text()
                self.passar_nivel_eventos()
                pygame.display.flip()

            if self.painel == "zerou":
                if self.opcao == 0:  ###TELA DE ZERAR
                    clock.tick(1000 / dt)
                    self.atualiza_elementos(dt)
                    self.desenha_elementos()
                    self.text.zerou_text()
                    self.text.zerou_menu_text()
                    self.zerou_eventos()
                    self.tela.blit(pygame.image.load(os.path.join('imagens','bat2.png')), [(self.screen_size[0]-250)/2, 50])
                    pygame.display.flip()

                if self.opcao == 1:  ###TELA DOS CRÉDITOS
                    clock.tick(1000 / dt)
                    self.atualiza_elementos(dt)
                    self.desenha_elementos()
                    self.text.zerou_creditos_text()
                    self.creditos_eventos()
                    pygame.display.flip()

    def loop_musica_fase_0_1(self, soundtrack0="corona_soundtrack.mp3", soundtrack1="8_bit_soundtrack.mp3"):
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

    def loop_musica_fase_2_3_4(self, soundtrack2="battle_soundtrack.mp3", soundtrack4="boss_soundtrack.mp3"):
        if self.nivel == 2:
            soundtrack2 = os.path.join('sons', soundtrack2)
            mixer.music.load(soundtrack2)
            mixer.music.set_volume(0.05)
            pygame.mixer.music.play(-1)

        elif self.nivel == 3:
            soundtrack2 = os.path.join('sons', soundtrack2)
            mixer.music.load(soundtrack2)
            mixer.music.set_volume(0.05)
            pygame.mixer.music.play(-1)
            
        elif self.nivel == 4:
            soundtrack4 = os.path.join('sons', soundtrack4)
            mixer.music.load(soundtrack4)
            mixer.music.set_volume(0.05)
            pygame.mixer.music.play(-1)

    def loop_musica_personalizar_tutorial(self, tutorial_soundtrack="tutorial.mp3"):
        tutorial_soundtrack = os.path.join('sons', tutorial_soundtrack)
        mixer.music.load(tutorial_soundtrack)
        mixer.music.set_volume(0.03)
        pygame.mixer.music.play(-1)


    def loop_musica_menu(self, menu_soundtrack="menu_soundtrack.mp3"):
        menu_soundtrack = os.path.join('sons', menu_soundtrack)
        mixer.music.load(menu_soundtrack)
        mixer.music.set_volume(0.025)
        pygame.mixer.music.play(-1)

    def loop_musica_passar_zerar(self, suspense="suspense.wav", vencer="vencer.mp3"):
        if self.painel == "passar_nivel":
            suspense = os.path.join('sons', suspense)
            mixer.music.load(suspense)
            mixer.music.set_volume(0.025)
            pygame.mixer.music.play(-1)
        if self.painel == "zerou":
            vencer = os.path.join('sons', vencer)
            mixer.music.load(vencer)
            mixer.music.set_volume(0.03)
            pygame.mixer.music.play(-1)






if __name__ == '__main__':
    J = Jogo()
    J.loop_jogo()
    
# Encerra a janela do pygame após encerrar o loop do jogo
pygame.display.quit()
pygame.quit()
