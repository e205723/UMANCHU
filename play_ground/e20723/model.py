from propertyInfo import propertyInfo
from gameObjects import *
from random import randint

class Model():
    def __init__(self, UserIPList, userNameList):
        self.users = [User(userIP, userName, order, [55, 11], 'u') for userIP, userName, order in zip(UserIPList, userNameList, range(4))]
        self.userIndex = 0
        self.time = Time()
        self.currentMode = None
        self.messageIndex = 0
        self.logIndex = 0
        self.map = Map(propertyInfo, letterMap)
        self.unitMap = [[[None] for j in range(73)] for i in range(59)]

        destinationIndex = 5
        while destinationIndex == 5:
            destinationIndex = randint(0,67)
        distinationInfo = self.map.propertyInfo[destinationIndex]
        self.destination = self.map.squaresMatrix[distinationInfo[1][1]][distinationInfo[1][0]]
        self.map.squaresMatrix[self.destination.coordinate[1]][self.destination.coordinate[0]].color = "目駅"

        for user in self.users:
            self.unitMap[user.coordinate[1]][user.coordinate[0]].append(str(user.order) + user.direction)

        #print(self.extractMap([55, 11]))
        #print(self.generateUnitMap([55, 11]))
        self.arrow = 5
        #self.menuはいらない、クライアント側にある
        self.menuIndex = 0
        self.log = ["" for _ in range(3)]
        self.select = ["" for _ in range(6)]
        self.selectMode = 2
        self.selectIndex = 6
        self.header = ["" for _ in range(2)]
        self.top = [""]
        self.darken = False
        self.message = ["" for _ in range(6)]

    def run(self):
        while True:
            if  self.currentMode is None:
                self.currentMode = Opening(None)
                self.currentMode.flow(self)
            else:
                self.currentMode.flow(self)

    def getDistanceFromDestiny(self, coordinate):
        horizontlDistance = (coordinate[0] - self.destination.coordinate[0])/3
        verticalDistance = (coordinate[1] - self.destination.coordinate[1])/3

        result = ""

        if horizontlDistance > 0:
            result += "ひだり" + str(int(horizontlDistance))
        elif horizontlDistance < 0:
            result += "みぎ" + str(-int(horizontlDistance))
        else:
            pass

        if horizontlDistance != 0 and verticalDistance != 0:
            result += "、"

        if verticalDistance > 0:
            result += "うえ" + str(int(verticalDistance))
        elif verticalDistance < 0:
            result += "した" + str(-int(verticalDistance))
        else:
            pass

        return result

    def getExtractedMap(self, coordinate = [55, 11]):
        return [[self.map.squaresMatrix[coordinate[1] + i - 5][coordinate[0] + j - 13].color for j in range(22)] for i in range(11)]

    def getUnitMap(self, coordinate = [55, 11]):
        return [[self.unitMap[coordinate[1] + i - 5][coordinate[0] + j - 13][-1] for j in range(22)] for i in range(11)]

    def getArrowDirection(self, coordinate):
        horizontlDistance = (coordinate[0] - self.destination.coordinate[0])
        verticalDistance = (coordinate[1] - self.destination.coordinate[1])
        if horizontlDistance**2 >= verticalDistance**2:
            if horizontlDistance > 0:
                self.arrow = 1
            else:
                self.arrow = 3
        else:
            if verticalDistance > 0:
                self.arrow = 0
            else:
                self.arrow = 2

    def getHeader(self):
        self.header[0] = self.users[self.userIndex].name + " " + self.users[self.userIndex].kanijMoney()
        self.header[1] = self.getDistanceFromDestiny(self.users[self.userIndex].coordinate) + "、" + self.time.getTime()

    def sendInfo(self, type):
        if type == "message":
            info = [None for _ in range(12)]
            info[10] = True
            info[11] = self.message
            print(info)
        elif type == "menu":
            info = [None for _ in range(12)]
            info[0] = self.getExtractedMap()
            info[1] = self.getUnitMap()
            info[3] = self.menuIndex
            self.getHeader()
            info[8] = self.header
            info[10] = False
            print(info)
        elif type == "log":
            info = [None for _ in range(12)]
            info[0] = self.getExtractedMap()
            info[1] = self.getUnitMap()
            info[8] = self.message
            info[10] = False
        else:
            print([self.getExtractedMap(), self.getUnitMap(), self.arrow, self.menuIndex, self.log, self.select, self.selectMode, self.selectIndex, self.header, self.top, self.darken, self.message])

    def listenKeyAction(self, type):
        if type == "message":
            keyAction = input("type d: ")
            if keyAction == "d" or keyAction == "l":
                pass
            elif keyAction == "s" or keyAction == "h":
                if self.messageIndex != 0:
                    self.messageIndex -= 2
                else:
                    self.messageIndex -= 1
            return keyAction
        elif type == "menu":
            keyAction = input("type j or k or d: ")
            if keyAction == "j" and self.menuIndex != 0:
                self.menuIndex -= 1
            elif keyAction == "k" and self.menuIndex != 2:
                self.menuIndex += 1
            elif keyAction == "d":
                if self.menuIndex == 0:
                    self.currentMode = BeforeThrowingDice(self.currentMode)
                elif self.menuIndex == 1:
                    '''
                    カードを使う
                    '''
                    pass
                elif self.menuIndex == 2:
                    '''
                    むしめがね
                    '''
                    pass

    def sendMessage(self, message):
        type = "message"

        for i in range(6):
            self.message[i] = message[self.messageIndex * 72 + i * 12: self.messageIndex * 72 + (i + 1) * 12]
        self.sendInfo(type)
        self.listenKeyAction(type)

        if len(message[(self.messageIndex + 1) * 72: (self.messageIndex + 1) * 72 + 12]) > 0:
            self.messageIndex += 1
            self.sendMessage(message)
        else:
            self.messageIndex = 0
            self.currentMode = Menu(self.currentMode)

    def sendMenu(self):
        type = "menu"
        self.sendInfo(type)
        self.listenKeyAction(type)

    def sendLog(self, log, mode):
        type = "log"

        for i in range(3):
            self.log[i] = log[self.logIndex * 41 + i * 17: self.logIndex * 41 + (i + 1) * 17]
        self.sendInfo(type)
        self.listenKeyAction(type)
        if len(log[(self.logIndex + 1) * 41: (self.logIndex + 1) * 41 + 17]) > 0:
            self.logIndex += 1
            self.sendLog(log)
        else:
            self.logIndex = 0
            if mode == "beforeThrowingDice":
                '''
                移動モード(Moveを実装しなければならない)
                '''
                #self.currentMode = Move(None)
                print("移動モード(Moveを実装しなければならない)")
