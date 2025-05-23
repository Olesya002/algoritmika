# напиши свой код здесь
class Hero():
    def __init__(self, pos, land):
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(0, 0.75, 1)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()
        self.mode = True
        self.turn_left()
        self.turn_right()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def cameraUp(self):
        base.mouseInterfaceNode.setPos(3, 3, 3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

        
    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)

    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def check_dir(self,angle):
        if angle >= 0 and angle <= 20:
            return (0, -1)
        elif angle <= 65:
            return (1, -1)
        elif angle <= 110:
            return (1, 0)
        elif angle <= 155:
            return (1, 1)
        elif angle <= 200:
            return (0, 1)
        elif angle <= 245:
            return (-1, 1)
        elif angle <= 290:
            return (-1, 0)
        elif angle <= 335:
            return (-1, -1)
        else:
            return (0, -1)
    def look_at(self, angle):
        ''' возвращает координаты, в которые переместится персонаж, стоящий в точке (x, y),
        если он делает шаг в направлении angle'''
        x_from = round(self.hero.getX())
        y_from = round(self.hero.getY())
        z_from = round(self.hero.getZ())


        dx, dy = self.check_dir(angle)
        x_to = x_from + dx
        y_to = y_from + dy
        return x_to, y_to, z_from

    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def try_move(self, angle):
        '''перемещается, если может'''
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            # перед нами свободно. Возможно, надо упасть вниз:
            pos = self.land.findHighestEmpty(pos)
            self.hero.setPos(pos)
        else:
            # перед нами занято. Если получится, заберёмся на этот блок:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)
                # не получится забраться - стоим на месте

    def changeMode(self):
        if self.mode:
            self.mode = False
        else:
            self.mode = True


    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)

    def forward(self):
        angle = (self.hero.getH()) % 360
        self.move_to(angle)

    def back(self):
        angle = (self.hero.getH()+180) % 360
        self.move_to(angle)

    def left(self):
        angle = (self.hero.getH()+90) % 360
        self.move_to(angle)

    def right(self):
        angle = (self.hero.getH()+270) % 360
        self.move_to(angle)

    def up(self):
        if self.mode:
            self.hero.setZ(self.hero.getZ() + 1)

    def down(self):
        if self.mode and self.hero.getZ() > 1:
            self.hero.setZ(self.hero.getZ() - 1)

    def build(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addBlock(pos)
        else:
            self.land.buildBlock(pos)

    def destroy(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.delBlock(pos)
        else:
            self.land.delBlockFrom(pos)

    def accept_events(self):
        base.accept( 'c' , self.changeView)
        base.accept('z', self.changeMode)

        base.accept( 'arrow_right', self.turn_right)
        base.accept( 'arrow_right'+'-repeat', self.turn_right)
        base.accept( 'arrow_left', self.turn_left)
        base.accept( 'arrow_left'+'-repeat', self.turn_left)

        base.accept('w', self.forward)
        base.accept('s', self.back)
        base.accept('a', self.left)
        base.accept('d', self.right)
        base.accept('arrow_up', self.up)
        base.accept('arrow_up' + '-repeat', self.up)
        base.accept('arrow_down', self.down)
        base.accept('arrow_down' + '-repeat', self.down)

        base.accept('w'+'-repeat', self.forward)
        base.accept('s'+'-repeat', self.back)
        base.accept('a'+'-repeat', self.left)
        base.accept('d'+'-repeat', self.right)

        base.accept('e', self.build)
        base.accept('q', self.destroy)
