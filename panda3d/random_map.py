def loadRandomMap(self, width, height, min_value, max_value):
        noise = PerlinNoise(octaves=2, seed=4522)
        amp = 6
        period = 24
        terrain_width = 50
  
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
