# напиши здесь код создания и управления картой
from direct.showbase.ShowBase import ShowBase
from perlin_noise import PerlinNoise
from numpy import floor
class Mapmanager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.colors = [
            (0, 1, 0, 1),
            (0, 0, 1, 1),
            (1, 0, 0, 1),
            (1, 1, 1, 1),
        ]
        self.startNew()

    def startNew(self):
        self.land = render.attachNewNode('Land')

    def GetColor(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.color) - 1]
        
    def addBlock(self, position):
        self.block = loader.loadModel('block.egg')
        self.texture = loader.loadTexture('block.png')
        self.block.setTexture(self.texture)
        self.color = self.GetColor(int(position[2]))
        self.block.setColor(self.color)
        self.block.setPos(position)
        self.block.setTag("at", str(position))
        self.block.reparentTo(self.land)

    def loadLand(self, filename):
         with open(filename) as file: 
            y = 0 
            for line in file: 
                x = 0 
                line = line.split(' ') 
                for z in line: 
                    for z0 in range(int(z)+1): 
                        block = self.addBlock((x, y, z0)) 
                    x += 1 
                y += 1

    def loadRandomMap(self, width, height, min_value, max_value):
            noise = PerlinNoise(octaves=2, seed=4522)
            amp = 20
            period = 24
            terrain_width = 25
    
            landscale = [[0 for i in range(terrain_width)] for i in range(terrain_width)]
            for position in range(terrain_width**2):
                # вычисление высоты y в координатах (x, z)
                x = floor(position / terrain_width)
                z = floor(position % terrain_width)
                y = abs(floor(noise([x/period, z/period])*amp))
                landscale[int(x)][int(z)] = int(y)
            
            y = 0
            for line in landscale:
                x = 0
                for z in line:
                    for z0 in range(z+1):
                        block = self.addBlock((x, y, z0))
                    x += 1
                y += 1

    def buildBlock(self, pos):
        """Ставим блок с учётом гравитации: """
        x, y, z = pos
        new = self.findHighestEmpty(pos)
        if new[2] <= z + 1:
            self.addBlock(new)

    def findBlocks(self, pos):
        return self.land.findAllMatches("=at=" + str(pos))
    
    def isEmpty(self, pos):
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        else:
            return True


    def findHighestEmpty(self, pos):
        x, y, z = pos
        z = 1
        while not self.isEmpty((x, y, z)):
            z += 1
        return (x, y, z) 
    
    def delBlock(self, position):
        """удаляет блоки в указанной позиции """
        blocks = self.findBlocks(position)
        for block in blocks:
            block.removeNode()


    def delBlockFrom(self, position):
        x, y, z = self.findHighestEmpty(position)
        pos = x, y, z - 1
        for block in self.findBlocks(pos):
                block.removeNode()

