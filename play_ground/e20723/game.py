import os
import pygame
from pygame import Rect
from pygame.math import Vector2

os.environ['SDL_VIDEO_CENTERED'] = '1'

'''
ゲームステート
'''

class Unit():
    def __init__(self,state,position,tile):
        self.state = state
        self.position = position
        self.tile = tile
    '''
    moveVectorを引数にCarUnitを移動
    '''
    def move(self,moveVector):
        # Compute new tank position
        newPosition = self.position + moveVector

        # Don't allow positions outside the world
        if newPosition.x < 0 or newPosition.x >= self.state.worldWidth \
        or newPosition.y < 0 or newPosition.y >= self.state.worldHeight:
            return

        # Don't allow other unit positions
        for unit in self.state.units:
            if newPosition == unit.position:
                return

        self.position = newPosition

class GameState():
    def __init__(self):
        self.windowSize = Vector2(22,12)
        self.ground = [
            [ Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1)],
            [ Vector2(5,1), Vector2(5,1), Vector2(7,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(7,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,4), Vector2(7,2), Vector2(7,2), Vector2(7,2), Vector2(7,2), Vector2(7,2), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1)],
            [ Vector2(5,1), Vector2(6,1), Vector2(5,1), Vector2(5,1), Vector2(6,1), Vector2(6,2), Vector2(5,1), Vector2(6,1), Vector2(6,1), Vector2(5,1), Vector2(6,2), Vector2(7,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1)],
            [ Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(7,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1)],
            [ Vector2(5,1), Vector2(7,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,5), Vector2(7,2), Vector2(7,2), Vector2(7,2), Vector2(7,2), Vector2(8,5), Vector2(6,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1)],
            [ Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,1), Vector2(6,2), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(7,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1)],
            [ Vector2(6,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(5,1), Vector2(7,1), Vector2(5,1), Vector2(6,2), Vector2(6,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1)],
            [ Vector2(5,1), Vector2(6,4), Vector2(7,2), Vector2(7,2), Vector2(7,2), Vector2(8,4), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1)],
            [ Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(7,1), Vector2(5,1), Vector2(5,1), Vector2(6,1), Vector2(5,1), Vector2(7,4), Vector2(7,2), Vector2(7,2), Vector2(7,2), Vector2(7,2), Vector2(7,2), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1)],
            [ Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(6,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1)],
            [ Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(6,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1)],
            [ Vector2(5,1), Vector2(6,2), Vector2(5,1), Vector2(6,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1), Vector2(5,1)]
        ]
        self.squares = [
            [ None, None, None, None, None, None, None, None, None, Vector2(1,3), Vector2(1,1), Vector2(1,1), Vector2(1,1), Vector2(1,1), Vector2(1,1), Vector2(1,1), None, None, None, None, None, None],
            [ None, None, None, None, None, None, None, None, None, Vector2(2,1), None, None, None, None, None, None, None, None, None, None, None, None],
            [ None, None, None, None, None, None, None, None, None, Vector2(2,1), None, None, Vector2(1,3), Vector2(1,1), Vector2(0,3), None, None, None, None, None, None, None],
            [ None, None, None, None, None, None, None, Vector2(1,1), Vector2(1,1), Vector2(3,3), None, None, Vector2(2,1), None, Vector2(2,1), None, None, None, None, None, None, None],
            [ None, None, None, None, None, None, None, None, None, None, None, None, Vector2(2,1), None, Vector2(2,1), None, None, None, None, None, None, None],
            [ None, None, None, None, None, None, None, Vector2(1,1), Vector2(1,1), Vector2(0,3), None, None, Vector2(2,1), None, Vector2(2,1), None, None, None, None, None, None, None],
            [ None, None, None, None, None, None, None, None, None, Vector2(2,1), None, None, Vector2(2,1), None, Vector2(2,1), None, None, None, None, None, None, None],
            [ None, None, None, None, None, None, None, None, None, Vector2(2,1), None, None, Vector2(2,3), Vector2(1,1), Vector2(3,3), None, None, None, None, None, None, None],
            [ None, None, None, None, None, None, None, None, None, Vector2(2,1), None, None, None, None, None, None, None, None, None, None, None, None],
            [ None, None, None, None, None, None, None, None, None, Vector2(2,3), Vector2(1,1), Vector2(1,1), Vector2(1,1), Vector2(1,1), Vector2(1,1), Vector2(1,1), None, None, None, None, None, None],
            [ None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [ None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        ]
        self.units = [
            Unit(self,Vector2(1,9),Vector2(1,0)),
            Unit(self,Vector2(6,3),Vector2(0,2)),
            Unit(self,Vector2(6,5),Vector2(0,2)),
            Unit(self,Vector2(13,3),Vector2(0,1)),
            Unit(self,Vector2(13,6),Vector2(0,1))
        ]


    @property
    def worldWidth(self):
        return int(self.windowSize.x)

    @property
    def worldHeight(self):
        return int(self.windowSize.y)

    def update(self,moveCommand):
        for i in range(len(self.units)):
            if i==0:
                self.units[i].move(moveCommand)

class Layer():
    def __init__(self,ui,imageFile):
        self.ui = ui
        self.texture = pygame.image.load(imageFile)

    def renderTile(self,surface,position,tile):
        # Location on screen
        spritePoint = position.elementwise()*self.ui.cellSize

        # Texture
        texturePoint = tile.elementwise()*self.ui.cellSize
        textureRect = Rect(int(texturePoint.x), int(texturePoint.y), self.ui.cellWidth, self.ui.cellHeight)

        # Draw
        surface.blit(self.texture,spritePoint,textureRect)

    def render(self,surface):
        raise NotImplementedError()

class ArrayLayer(Layer):
    def __init__(self,ui,imageFile,gameState,array):
        super().__init__(ui,imageFile)
        self.gameState = gameState
        self.array = array

    def render(self,surface):
        for y in range(self.gameState.worldHeight):
            for x in range(self.gameState.worldWidth):
                tile = self.array[y][x]
                if not tile is None:
                    self.renderTile(surface,Vector2(x,y),tile)

class UnitsLayer(Layer):
    def __init__(self,ui,imageFile,gameState,units):
        super().__init__(ui,imageFile)
        self.gameState = gameState
        self.units = units

    def render(self,surface):
        for unit in self.units:
            self.renderTile(surface,unit.position,unit.tile)
            self.renderTile(surface,unit.position,Vector2(0,6))

class UserInterface():
    def __init__(self):
        pygame.init()

        # Game state
        self.gameState = GameState()

        # Rendering properties
        self.cellSize = Vector2(64,64)
        '''
        ここでレイヤーの順番を決めている
        '''
        self.layers = [
            ArrayLayer(self,"ground.png",self.gameState,self.gameState.ground),
            ArrayLayer(self,"walls.png",self.gameState,self.gameState.squares),
            UnitsLayer(self,"units.png",self.gameState,self.gameState.units)
        ]

        # Window
        windowSize = self.gameState.windowSize.elementwise() * self.cellSize
        self.window = pygame.display.set_mode((int(windowSize.x),int(windowSize.y)))
        pygame.display.set_caption("Discover Python & Patterns - https://www.patternsgameprog.com")
        pygame.display.set_icon(pygame.image.load("icon.png"))
        self.moveCommand = Vector2(0,0)

        # Loop properties
        self.clock = pygame.time.Clock()
        self.running = True

    @property
    def cellWidth(self):
        return int(self.cellSize.x)

    @property
    def cellHeight(self):
        return int(self.cellSize.y)

    def processInput(self):
        self.moveCommand = Vector2(0,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_l:
                    self.moveCommand.x = 1
                elif event.key == pygame.K_h:
                    self.moveCommand.x = -1
                elif event.key == pygame.K_j:
                    self.moveCommand.y = 1
                elif event.key == pygame.K_k:
                    self.moveCommand.y = -1

    def update(self):
        self.gameState.update(self.moveCommand)

    def render(self):
        self.window.fill((0,0,0))

        for layer in self.layers:
            layer.render(self.window)

        pygame.display.update()

    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(10)

userInterface = UserInterface()
userInterface.run()

pygame.quit()
