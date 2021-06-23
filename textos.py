import pygame

class Textos:
    """
    Esta é a classe para renderizar os textos utilizados no jogo.
    """
    def __init__(self, size=(850, 800)):

        self.tela = pygame.display.set_mode(size)
        self.screen_size = self.tela.get_size()

        self.fonte = pygame.font.SysFont("monospace", 32)
        self.over_font = pygame.font.Font('freesansbold.ttf', 64)
        self.vencer_font = pygame.font.SysFont("freesansbold.ttf", 38)
        self.menu_font = pygame.font.SysFont("freesansbold.ttf", 32)
        self.opc_font = pygame.font.SysFont("freesansbold.ttf", 28)

    def sair_text(self):
        sair = self.menu_font.render("[ESC] SAIR", 1, (255, 255, 255))
        self.tela.blit(sair, (self.screen_size[0] / 2 + self.screen_size[0] / 3, self.screen_size[1]/1.075))

    def jogo_text(self):
        over_text = self.over_font.render("CORONA SHOOTER", 1, (255, 255, 255))
        self.tela.blit(over_text, (self.screen_size[0]/2 - self.screen_size[0]/2.7,self.screen_size[1]/3.25))

    def menu_text(self):
        jogar = self.menu_font.render("Jogar  (1)", 1, (255, 255, 255))
        tutorial = self.menu_font.render("Tutorial  (2)", 1, (255, 255, 255))
        personalizar = self.menu_font.render("Personalizar  (3)", 1, (255, 255, 255))
        quit = self.menu_font.render("Sair  (4)", 1, (255, 255, 255))
        self.tela.blit(jogar, (self.screen_size[0]/2 - self.screen_size[0]/3,self.screen_size[1]/2))
        self.tela.blit(tutorial, (self.screen_size[0]/2 - self.screen_size[0]/3, (self.screen_size[1]/2)+40))
        self.tela.blit(personalizar, (self.screen_size[0]/2 - self.screen_size[0]/3, (self.screen_size[1]/2)+80))
        self.tela.blit(quit, (self.screen_size[0]/2 - self.screen_size[0]/3, (self.screen_size[1] / 2) + 120))

    def tutorial_text(self):
        tutorial_title = self.over_font.render("TUTORIAL", 1, (255, 255, 255))
        tut_desc = self.menu_font.render("O Coronavírus está tentando invadir o planeta Terra.", 1, (255, 255, 255))
        tut_desc1 = self.menu_font.render("A vacina foi desenvolvida com uma nova tecnologia, mas,", 1, (255, 255, 255))
        tut_desc2 = self.menu_font.render("para ela funcionar, você precisa acertar os vírus com sua seringa!", 1,(255, 255, 255))
        tut_desc3 = self.menu_font.render("O desafio é composto por 5 fases, e você tem 5 vidas para", 1,(255, 255, 255))
        tut_desc4 = self.menu_font.render("impedir que os vírus cheguem à Terra e contaminem os humanos.", 1,(255, 255, 255))
        tut_desc5 = self.menu_font.render("Boa Sorte!", 1, (255, 255, 255))
        tutorial_opc1 = self.menu_font.render("Voltar  (4)", 1, (255, 255, 255))
        self.tela.blit(tutorial_title, (self.screen_size[0]/2 - self.screen_size[0]/2.7, self.screen_size[1]/5))
        self.tela.blit(tut_desc, (self.screen_size[0] / 2 - self.screen_size[0] / 2.7, self.screen_size[1] / 3.2))
        self.tela.blit(tut_desc1, (self.screen_size[0] / 2 - self.screen_size[0] / 2.7, self.screen_size[1] / 3.2 + 30))
        self.tela.blit(tut_desc2,(self.screen_size[0] / 2 - self.screen_size[0] / 2.7, self.screen_size[1] / 3.2 + 60))
        self.tela.blit(tut_desc3, (self.screen_size[0] / 2 - self.screen_size[0] / 2.7, self.screen_size[1] / 3.2 + 90))
        self.tela.blit(tut_desc4,(self.screen_size[0] / 2 - self.screen_size[0] / 2.7, self.screen_size[1] / 3.2 + 120))
        self.tela.blit(tut_desc5, (self.screen_size[0] / 2 - self.screen_size[0] / 2.7, self.screen_size[1] / 3.2 + 150))
        self.tela.blit(tutorial_opc1, ((self.screen_size[0] / 2 - self.screen_size[0] / 2.7), self.screen_size[1] / 1.5))

    def personalizar_text(self):
        personalizar = self.over_font.render("PERSONALIZAR", 1, (255, 255, 255))
        personalizar_desc = self.menu_font.render("Escolha a cor da sua seringa:", 1, (255, 255, 255))
        personalizar_opc1 = self.opc_font.render("Roxo Padrão  (1)", 1, (255, 255, 255))
        personalizar_opc2 = self.opc_font.render("Vermelho  (2)" , 1, (255, 255, 255))
        personalizar_opc3 = self.opc_font.render("Rosa  (3)", 1, (255, 255, 255))
        personalizar_opc4 = self.opc_font.render("Azul  (4)", 1, (255, 255, 255))
        personalizar_voltar = self.opc_font.render("Voltar  (5)", 1, (255, 255, 255))
        self.tela.blit(personalizar, (self.screen_size[0]/2 - self.screen_size[0]/2.7, self.screen_size[1]/5))
        self.tela.blit(personalizar_desc, (self.screen_size[0]/2 - self.screen_size[0]/2.7, (self.screen_size[1]/3.5)+60))
        self.tela.blit(personalizar_opc1, (self.screen_size[0]/2 - self.screen_size[0]/2.7, (self.screen_size[1]/3.5)+140))
        self.tela.blit(personalizar_opc2, (self.screen_size[0]/2 - self.screen_size[0]/2.7, (self.screen_size[1]/3.5)+180))
        self.tela.blit(personalizar_opc3, (self.screen_size[0]/2 - self.screen_size[0]/2.7, (self.screen_size[1]/3.5)+220))
        self.tela.blit(personalizar_opc4, ((self.screen_size[0]/2 - self.screen_size[0]/2.7), (self.screen_size[1]/3.5)+260))
        self.tela.blit(personalizar_voltar, ((self.screen_size[0] / 2 - self.screen_size[0] / 2.7), (self.screen_size[1] / 3.5) + 300))

    def game_over_text(self):
        over_text = self.over_font.render("GAME OVER!", 1, (255, 255, 255))
        self.tela.blit(over_text, (self.screen_size[0]/2 - self.screen_size[0]/4,self.screen_size[1]/3.25))
        menu = self.menu_font.render("Menu (1)", 1, (255, 255, 255))
        quit = self.menu_font.render("Sair  (2)", 1, (255, 255, 255))
        self.tela.blit(menu, (self.screen_size[0]/2 - self.screen_size[0]/3,self.screen_size[1]/2))
        self.tela.blit(quit, (self.screen_size[0]/2 - self.screen_size[0]/3, (self.screen_size[1] / 2) + 40))

    def zerou_text(self):
        zerou = self.over_font.render("PARABÉNS!!", 1, (255, 255, 255))
        zerou_desc = self.vencer_font.render("VOCÊ VENCEU O CORONA SHOOTER", 1, (255, 255, 255))
        zerou_obg = self.vencer_font.render("OBRIGADO POR JOGAR!", 1, (255, 255, 255))
        self.tela.blit(zerou, (self.screen_size[0]/2 - self.screen_size[0]/2.7, self.screen_size[1]/3.25))
        self.tela.blit(zerou_desc, (self.screen_size[0] / 2 - self.screen_size[0] /2.7, self.screen_size[1] / 2.5))
        self.tela.blit(zerou_obg, (self.screen_size[0] / 2 - self.screen_size[0] /2.7, self.screen_size[1] / 2.2))

    def zerou_menu_text(self):
        menu = self.menu_font.render("Menu  (1)", 1, (255, 255, 255))
        cred = self.menu_font.render("Créditos  (2)", 1, (255, 255, 255))
        quit = self.menu_font.render("Sair  (3)", 1, (255, 255, 255))
        self.tela.blit(menu, (self.screen_size[0]/2 - self.screen_size[0]/2.7, self.screen_size[1]/1.8))
        self.tela.blit(cred, (self.screen_size[0]/2 - self.screen_size[0]/2.7, self.screen_size[1]/1.68))
        self.tela.blit(quit, (self.screen_size[0] / 2 - self.screen_size[0] / 2.7, self.screen_size[1] / 1.57))

    def zerou_creditos_text(self):
        cred_title = self.over_font.render("Créditos", 1, (255, 255, 255))
        nome1 = self.menu_font.render("Dominique", 1, (255, 255, 255))
        nome2 = self.menu_font.render("Iara", 1, (255, 255, 255))
        nome3 = self.menu_font.render("Juliana", 1, (255, 255, 255))
        nome4 = self.menu_font.render("Jonathan", 1, (255, 255, 255))
        nome5 = self.menu_font.render("Marcelo", 1, (255, 255, 255))
        voltar = self.menu_font.render("Voltar  (4)", 1, (255, 255, 255))
        self.tela.blit(cred_title, (self.screen_size[0]/2 - self.screen_size[0]/2.7, self.screen_size[1]/5))
        self.tela.blit(nome1, (self.screen_size[0]/2 - self.screen_size[0]/2.7, (self.screen_size[1]/3.5)+100))
        self.tela.blit(nome2, (self.screen_size[0]/2 - self.screen_size[0]/2.7, (self.screen_size[1]/3.5)+140))
        self.tela.blit(nome3, (self.screen_size[0]/2 - self.screen_size[0]/2.7, (self.screen_size[1]/3.5)+180))
        self.tela.blit(nome4, (self.screen_size[0]/2 - self.screen_size[0]/2.7, (self.screen_size[1]/3.5)+220))
        self.tela.blit(nome5, (self.screen_size[0] / 2 - self.screen_size[0] / 2.7, (self.screen_size[1] / 3.5) + 260))
        self.tela.blit(voltar,((self.screen_size[0] / 2 - self.screen_size[0] / 2.7), (self.screen_size[1] / 3.5) + 400))
        
    def pausado_text(self):
        over_text = self.over_font.render("PAUSADO", 1, (255, 255, 255))
        self.tela.blit(over_text, (self.screen_size[0]/2 - self.screen_size[0]/4.4,self.screen_size[1]/2.5))

