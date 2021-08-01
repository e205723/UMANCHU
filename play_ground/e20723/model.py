from propertyInfo import propertyInfo
from gameObjects import *
import random

class Model():
    def __init__(self, UserIPList, userNameList):
        self.users = [User(userIP, userName, order, [55, 11], 'u') for userIP, userName, order in zip(UserIPList, userNameList, range(4))]
        self.map = Map(propertyInfo, letterMap)
        self.unitMap = [[[None] for j in range(73)] for i in range(59)]
        self.time = Time()
        self.current_mode = None
        self.destination = None

        for user in self.users:
            self.unitMap[user.coordinate[1]][user.coordinate[0]].append(str(user.order) + user.direction)

        #print(self.extractMap([55, 11]))
        #print(self.generateUnitMap([55, 11]))
        self.arrow = None
        #self.menuはいらない、クライアント側にある
        self.menuIndex = 4
        self.log = ["" for _ in range(3)]
        self.select = ["" for _ in range(6)]
        self.select_mode = 2
        self.selectIndex = 6
        self.header = ["" for _ in range(2)]
        self.top = [""]
        self.message = ["" for _ in range(6)]
        self.messageIndex = 0
        self.darken = False

    def run(self):
        self.current_mode = Opening(None)
        self.current_mode.flow(self, None)

    def getDistanceFromDestiny(self, coordinate):
        horizontlDistance = (coordinate[0] - self.destination.coordinate[0])/3
        verticalDistance = (coordinate[1] - self.destination.coordinate[1])/3

        result = ""

        if horizontlDistance > 0:
            result += "ひだりヘ" + str(horizontlDistance) + "マス"
        elif horizontlDistance < 0:
            result += "みぎヘ" + str(-horizontlDistance) + "マス"
        else:
            pass

        if horizontlDistance != 0 and verticalDistance != 0:
            result += "、"

        if verticalDistance > 0:
            result += "うえヘ" + str(horizontlDistance) + "マス"
        elif verticalDistance < 0:
            result += "したヘ" + str(horizontlDistance) + "マス"
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
                self.arrow = 4

    def getHeader(self, uer):
        self.header[0] = user.name + " " + user.kanijMoney()
        self.header[1] = "もくてきちまで" + self.getDistanceFromDestiny(user.coordinate) + " " + self.time.getTime()

    def sendInfo(self, type):
        if type == "message":
            print([self.getExtractedMap(), self.getUnitMap(), self.arrow, self.menuIndex, self.log, self.select, self.select_mode, self.selectIndex, self.header, self.top, self.message, self.darken])
        else:
            print([self.getExtractedMap(), self.getUnitMap(), self.arrow, self.menuIndex, self.log, self.select, self.select_mode, self.selectIndex, self.header, self.top, self.message, self.darken])

    def listenKeyAction(self, type):
        if type == "message":
            if input("type d") == "d":
                pass
            else:
                if self.messageIndex != 0:
                     self.messageIndex -= 2

    def sendMessage(self, message):
        type = "message"

        for i in range(len(self.message)):
            self.message[i] = message[self.messageIndex * 72 + i * 12: self.messageIndex * 72 + (i + 1) * 12]
        self.sendInfo(type)
        self.listenKeyAction(type)

        if len(message[(self.messageIndex + 1) * 72: (self.messageIndex + 1) * 72 + 12]) > 0:
            self.messageIndex += 1
            self.sendMessage(message)
        else:
            self.message = ["" for _ in range(6)]
