from Nave_Tiro import Nave

class Boss(Nave):
    def __init__(self, position, lives=100, image=None, new_size=[250,250]):
        if not image:
            image = "boss.png"
        super().__init__(position, lives, [0, 0], image, new_size)
        
    def alvejado(self):
        self.set_lives(self.get_lives() - 1)