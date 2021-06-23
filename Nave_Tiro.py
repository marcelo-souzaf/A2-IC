from elementos import ElementoSprite

class Nave(ElementoSprite):
    def __init__(self, position, lives=0, speed=[0, 0], image=None, new_size=[100, 248]):
        self.set_image(image)
        super().__init__(image, position, speed, new_size)
        self.set_lives(lives)

    def get_lives(self):
        return self.lives

    def set_lives(self, lives):
        self.lives = lives

    def set_image(self, image):
        self.image = image

    def colisão(self):
        if self.get_lives() <= 0:
            self.kill()
        else:
            self.set_lives(self.get_lives() - 1)

    def atira(self, lista_de_tiros, image=None):
        s = list(self.get_speed())
        s[1] *= 2
        Tiro(self.get_pos(), s, image, lista_de_tiros)

    def boss_atira(self, lista_de_tiros):
        Tiro(self.get_bottom(), [0,4], 'laser_red.png', lista_de_tiros, [20,80])

    def alvejado(self):
        self.set_lives(self.get_lives() - 1)
        if self.get_lives() <= 0:
            self.kill()
            

    @property
    def morto(self):
        return self.get_lives() == 0



class Tiro(ElementoSprite):
    def __init__(self, position, speed=None, image=None, list=None, size=[60,60]):
        if not image:
            image = "tiro2.png"
        super().__init__(image, position, speed, size)
        if list is not None:
            self.add(list)