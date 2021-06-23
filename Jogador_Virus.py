from Nave_Tiro import Nave, Tiro
import random
import os, pygame

class Virus(Nave):
    def __init__(self, position, lives=1, speed=None, image=None, size=(80,80)):
        if not image:
            image = random.choice(["virus_orange.png", "virus_yellow.png", "virus_verm.png"])
        self.new_size = size
        super().__init__(position, lives, speed, image, size)


class Jogador(Nave):
    """
    A classe Player é uma classe derivada da classe GameObject.
       No entanto, o personagem não morre quando passa da borda, este só
    interrompe o seu movimento (vide update()).
       E possui experiência, que o fará mudar de nivel e melhorar seu tiro.
       A função get_pos() só foi redefinida para que os tiros não saissem da
    parte da frente da nave do personagem, por esta estar virada ao contrário
    das outras.
    """

    def __init__(self, position, lives=10, image=None, new_size=[50,140]):
        if not image:
            image = "seringa.png"
        self.new_size = new_size
        self.position = position
        super().__init__(position, lives, [0, 0], image, new_size)
        self.pontos = 0

    def set_image_roxo(self, seringa_roxa="seringa.png"):
        self.image = os.path.join('imagens', seringa_roxa)
        self.image = pygame.image.load(self.image)
        if self.new_size:
            self.scale(self.new_size)
        self.rect = self.image.get_rect()
        self.set_pos(self.position)

    def set_image_verm(self, seringa_verm="seringa_verm.png"):
        self.image = os.path.join('imagens', seringa_verm)
        self.image = pygame.image.load(self.image)
        if self.new_size:
            self.scale(self.new_size)
        self.rect = self.image.get_rect()
        self.set_pos(self.position)

    def set_image_rosa(self, seringa_rosa="seringa_rosa.png"):
        self.image = os.path.join('imagens', seringa_rosa)
        self.image = pygame.image.load(self.image)
        if self.new_size:
            self.scale(self.new_size)
        self.rect = self.image.get_rect()
        self.set_pos(self.position)

    def set_image_azul(self, seringa_azul="seringa_azul.png"):
        self.image = os.path.join('imagens', seringa_azul)
        self.image = pygame.image.load(self.image)
        if self.new_size:
            self.scale(self.new_size)
        self.rect = self.image.get_rect()
        self.set_pos(self.position)

    def update(self, dt):
        if (self.rect.right > self.area.right):
            self.rect.right = self.area.right

        elif (self.rect.left < 0):
            self.rect.left = 0

        if (self.rect.bottom > self.area.bottom):
            self.rect.bottom = self.area.bottom

        elif (self.rect.top < 0):
            self.rect.top = 0

    def get_pos(self):
        return (self.rect.center[0], self.rect.top)

    def get_bottom(self):
        return (self.rect.center[0], self.rect.bottom)

    def get_pontos(self):
        return self.pontos

    def set_pontos(self, pontos):
        self.pontos = pontos

    def atira(self, lista_de_tiros, image=None):
        l = 1
        if self.pontos > 25*(6-self.lives):
            l = 3
        if self.pontos > 50*(6-self.lives):
            l = 5

        p = self.get_pos()
        speeds = self.get_fire_speed(l)
        for s in speeds:
            Tiro(p, s, image, lista_de_tiros)

    def get_fire_speed(self, shots):
        speeds = []

        if shots <= 0:
            return speeds

        if shots == 1:
            speeds += [(0, -5)]

        if shots > 1 and shots <= 3:
            speeds += [(1, -5)]
            speeds += [(-1, -5)]

        if shots > 3 and shots <= 5:
            speeds += [(0, -5)]
            speeds += [(-2, -4)]
            speeds += [(2, -4)]

        return speeds

