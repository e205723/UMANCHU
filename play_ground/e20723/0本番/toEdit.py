import socket
import pickle
import os
import pygame
from pygame import Rect
from pygame.math import Vector2
from coordinates import *
from time import sleep

os.environ['SDL_VIDEO_CENTERED'] = '1'

class View():
    def __init__(self):
        self.infoToDisplay = None
        self.windowSize = Vector2(22,12)
        self.ground = [[Vector2(*groundDict["草"]) for i in range(22)] for j in range(12)]
        self.units = [[Vector2(*groundDict["草"]) for i in range(22)] for j in range(12)]
        self.arrow = [[Vector2(*groundDict["草"]) for i in range(22)] for j in range(12)]
        self.menuBackGround = [[Vector2(*groundDict["草"]) for i in range(22)] for j in range(12)]
        self.menu = [[Vector2(*groundDict["草"]) for i in range(22)] for j in range(12)]
        self.logBackGround = [[Vector2(*groundDict["草"]) for i in range(22)] for j in range(12)]
        self.log = [[Vector2(*groundDict["草"]) for i in range(22)] for j in range(12)]
        self.selectBackGround = [[Vector2(*groundDict["草"]) for i in range(22)] for j in range(12)]
        self.select = [[Vector2(*groundDict["草"]) for i in range(22)] for j in range(12)]
        self.headerBackGround = [[Vector2(*groundDict["草"]) for i in range(22)] for j in range(12)]
        self.header = [[Vector2(*groundDict["草"]) for i in range(22)] for j in range(12)]
        self.topBackGround = [[Vector2(*groundDict["草"]) for i in range(22)] for j in range(12)]
        self.top = [[Vector2(*groundDict["草"]) for i in range(22)] for j in range(12)]
        self.darken = [[Vector2(*groundDict["草"]) for i in range(22)] for j in range(12)]
        self.messageBackGround = [[Vector2(*groundDict["草"]) for i in range(22)] for j in range(12)]
        self.message = [[Vector2(*groundDict["草"]) for i in range(22)] for j in range(12)]

    @property
    def worldWidth(self):
        return int(self.windowSize.x)

    @property
    def worldHeight(self):
        return int(self.windowSize.y)

    def updateLayer(self):
        self.generateMapLayer()
        self.generateUnitMapLayer()
        self.generateArrowLayer()
        self.generateMenuLayer()
        self.generateLogLayer()
        self.generateSelectLayer()
        self.generateHeaderLayer()
        self.generateTopLayer()
        self.generateMessageLayer()

    def generateMapLayer(self):
        map = self.infoToDisplay[0]
        if not map is None:
            self.ground = [[Vector2(*groundDict[map[i][j]]) for j in range(22)] for i in range(11)]
        else:
            self.ground = [[None for j in range(22)] for i in range(11)]

    def generateUnitMapLayer(self):
        unitMap = self.infoToDisplay[1]
        if not map is None:
            self.units = [[Vector2(*unitsDict[unitMap[i][j]]) for j in range(22)] for i in range(11)]
        else:
            self.units = [[None for j in range(22)] for i in range(11)]

    def generateArrowLayer(self):
        arrow = self.infoToDisplay[2]
        self.arrow = [[None for j in range(22)] for i in range(11)]
        if not map is None:
            if arrow == 0:
                self.arrow[5][13] = Vector2(*arrowDict[0])
            elif arrow == 1:
                self.arrow[6][12] = Vector2(*arrowDict[0])
            elif arrow == 2:
                self.arrow[7][13] = Vector2(*arrowDict[0])
            elif arrow == 3:
                self.arrow[6][14] = Vector2(*arrowDict[0])
        else:
            pass

    def generateMenuLayer(self):
        menu = self.infoToDisplay[3]
        self.menuBackGround = [[None for j in range(22)] for i in range(11)]
        self.menu = [[None for j in range(22)] for i in range(11)]
        dice = "サイコロ"
        card = "カード"
        if not menu is None:
            if menu == 0:
                for i in range(5):
                    self.logBackGround[10][j] = Vector2(*backGroundDict["オレンジ"])
                    self.logBackGround[11][j] = Vector2(*backGroundDict["黒"])
            else:
                for i in range(5):
                    self.logBackGround[11][j] = Vector2(*backGroundDict["オレンジ"])
                    self.logBackGround[10][j] = Vector2(*backGroundDict["黒"])
                for j in range(4):
                    self.menu[10][j] = Vector2(*letterDict[dice[j]])
                for j in range(3):
                    self.menu[11][j] = Vector2(*letterDict[card[j]])
        else:
            pass

    def generateLogLayer(self):
        '''
        ログ
        '''
        log = self.infoToDisplay[4]
        self.logBackGround = [[None for j in range(22)] for i in range(11)]
        self.log = [[None for j in range(22)] for i in range(11)]
        if not log is None:
            for i in range(3):
                for j in range(17):
                    self.logBackGround[9 + i][j] = Vector2(*backGroundDict["黒"])
                    self.log[9 + i][j] = Vector2(*letterDict[[log[i][j]]])
        else:
            pass

    def generateSelectLayer(self):
        '''
        せんたく
        '''
        select = self.infoToDisplay[5]
        self.selectBackGround = [[None for j in range(22)] for i in range(11)]
        self.select = [[None for j in range(22)] for i in range(11)]
        if not log is None:
            for i in range(6):
                for j in range(17):
                    self.selectBackGround[2 + i][5 + j] = Vector2(*backGroundDict["黒"])
            for i in range(6):
                for j in range(len(select[i])):
                    self.select[2 + i][5 + j] = Vector2(*letterDict[select[i][j]])
            if self.infoToDisplay[6] == 0:
                pass
            else:
                for i in range(17):
                    self.selectBackGround[2 + self.infoToDisplay[7]][5 + j] = Vector2(*backGroundDict["オレンジ"])
        else:
            pass

    def generateHeaderLayer(self):
        header = self.infoToDisplay[8]
        self.headerBackGround = [[None for j in range(22)] for i in range(11)]
        self.header = [[None for j in range(22)] for i in range(11)]
        if not header is None:
            for i in range(2):
                for j in range(22):
                    self.headerBackGround[i][j] = Vector2(*backGroundDict["黒"])
                for j in range(len(header[i])):
                    self.header[i][j] = Vector2(*letterDict[self.header[i][j]])
        else:
            pass

    def generateTopLayer(self):
        top = self.infoToDisplay[9]
        self.topBackGround = [[None for j in range(22)] for i in range(11)]
        self.top = [[None for j in range(22)] for i in range(11)]
        if not top is None:
            for i in range(22):
                self.topBackGround[0][i] = Vector2(*backGroundDict["黒"])
            for i in range(len(top)):
                self.top[0][i] = Vector2(*letterDict[self.top[0][i]])
        else:
            pass

    def generateMessageLayer(self):
        message = self.infoToDisplay[11]
        if self.infoToDisplay[10]:
            self.darken = [[Vector2(*backGroundDict["黒"]) for j in range(22)] for i in range(11)]
        else:
            self.darken = [[None for j in range(22)] for i in range(11)]
        self.messageBackGround = [[None for j in range(22)] for i in range(11)]
        self.message = [[None for j in range(22)] for i in range(11)]
        for i in range(6):
            for j in range(12):
                if self.darken:
                    self.messageBackGround[3 + i][5 + j] = Vector2(*backGroundDict["オレンジ"])
                else:
                    self.messageBackGround[3 + i][5 + j] = Vector2(*backGroundDict["黒"])

class Layer():
    def __init__(self, ui, imageFile, view, array):
        self.ui = ui
        self.texture = pygame.image.load(imageFile)
        self.view = view
        self.array = array

    def renderTile(self,surface,position,tile):
        # Location on screen
        spritePoint = position.elementwise()*self.ui.cellSize

        # Texture
        texturePoint = tile.elementwise()*self.ui.cellSize
        textureRect = Rect(int(texturePoint.x), int(texturePoint.y), self.ui.cellWidth, self.ui.cellHeight)

        # Draw
        surface.blit(self.texture,spritePoint,textureRect)

    def render(self,surface):
        for y in range(self.view.worldHeight):
            for x in range(self.view.worldWidth):
                tile = self.array[y][x]
                if not tile is None:
                    self.renderTile(surface,Vector2(x,y),tile)

class UserInterface():
    def __init__(self):
        pygame.init()

        # Game state
        self.view = View()

        # Rendering properties
        self.cellSize = Vector2(64,64)
        '''
        ここでレイヤーの順番を決めている
        '''
        self.layers = [
            Layer(self,"TILES/MAP.png",self.view,self.view.ground),
            Layer(self,"TILES/UNIT.png",self.view,self.view.units)
        ]

        # Window
        windowSize = self.view.windowSize.elementwise() * self.cellSize
        self.window = pygame.display.set_mode((int(windowSize.x),int(windowSize.y)))
        pygame.display.set_caption("UMANCHU")
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

    def listen(self):
        HOST = socket.gethostbyname(socket.gethostname())  # Standard loopback interface address (localhost)
        PORT = 49152   # Port to listen on (non-privileged ports are > 1023)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(pickle.dumps(""))
                    self.view.infoToDisplay = pickle.loads(data)

    def sendOrder(self, order):
        HOST = socket.gethostbyname(socket.gethostname())
        PORT = 49153        # The port used by the server
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(pickle.dumps([HOST, order]))
                data = s.recv(1024)
            sleep(1)
            return 0
        except:
            return 1

    def processInput(self):
        actions = []
        while(len(actions) == 0):
            actions = pygame.event.get()
            self.moveCommand = Vector2(0,0)
        order = ""
        for event in actions:
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_s:
                    order = "s"
                elif event.key == pygame.K_d:
                    order = "d"
                elif event.key == pygame.K_l:
                    order = "l"
                elif event.key == pygame.K_h:
                    order = "h"
                elif event.key == pygame.K_j:
                    order = "j"
                elif event.key == pygame.K_k:
                    order = "k"
        input = self.sendOrder(order)

    def render(self):
        self.window.fill((0,0,0))
        print(self.window)
        for layer in self.layers:
            layer.render(self.window)

        pygame.display.update()

    def run(self):
        while self.running:
            self.listen()
            self.render()
            self.processInput()

userInterface = UserInterface()
userInterface.run()

pygame.quit()
