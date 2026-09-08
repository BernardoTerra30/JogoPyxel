import pyxel

class Personagem:

    def __init__(self, x, y, largura, altura, cor):

        self.x1 = x
        self.y1 = y
        self.largura = largura
        self.altura = altura
        self.cor = cor

        self.criarBox()

    def criarBox(self):

        self.x2 = self.x1 + self.largura
        self.y2 = self.y1 + self.altura

    def draw(self):

        pyxel.rect(self.x1, self.y1, self.largura, self.altura, self.cor)
       

class Jogo:

    def __init__(self):

        pyxel.init(120,100,'Colisao')

        self.heroi = Personagem(10, 10, 5, 5, 7)
        self.inimigo = Personagem(80, 80, 8, 8, 10)
        # Atributos aqui

        pyxel.images[0].load(0, 0, 'cat_16x16.png')

        pyxel.run(self.update, self.draw)


    def movimento(self):

        if pyxel.btn(pyxel.KEY_UP):
            self.heroi.y1 = self.heroi.y1 - 1

        if pyxel.btn(pyxel.KEY_DOWN):
            self.heroi.y1 = self.heroi.y1 + 1

        if pyxel.btn(pyxel.KEY_LEFT):   
            self.heroi.x1 = self.heroi.x1 - 1
        
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.heroi.x1 = self.heroi.x1 + 1


        if pyxel.btn(pyxel.KEY_W):
            self.inimigo.y1 = self.inimigo.y1 - 1

        if pyxel.btn(pyxel.KEY_S):
            self.inimigo.y1 = self.inimigo.y1 + 1

        if pyxel.btn(pyxel.KEY_A): 
            self.inimigo.x1 = self.inimigo.x1 - 1
        
        if pyxel.btn(pyxel.KEY_D):
            self.inimigo.x1 = self.inimigo.x1 + 1        

# Atualiza x2 e y2 depois do movimento
        self.heroi.criarBox()
        self.inimigo.criarBox()

    def update(self):

        self.movimento()

        if self.colisao(self.heroi, self.inimigo):
            print("COLISÃO!")
            #definitivamente editando
 

    def colisao(self, obj1, obj2):

        colisaoX = (obj2.x1 <= obj1.x1 and obj1.x1 <= obj2.x2) or (obj2.x1 <= obj1.x2 and obj1.x2 <= obj2.x2)

        colisaoY = (obj2.y1 <= obj1.y1 and obj1.y1 <= obj2.y2) or (obj2.y1 <= obj1.y2 and obj1.y2 <= obj2.y2)

        return colisaoX and colisaoY

    def draw(self):

        pyxel.cls(0)

        self.inimigo.draw()

        pyxel.blt(self.heroi.x1, self.heroi.y1, 0, 0, 0, 16, 16)
Jogo()