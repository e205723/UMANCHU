from gameObjects import *
from info import *
import random

class Model():
    def __init__(self, UserIPList, userNameList):
        self.users = [User(userIP, userName, order, [55, 11], 'u') for userIP, userName, order in zip(UserIPList, userNameList, range(4))]
        self.map = Map(propertyInfo, letterMap)
        self.unitMap = [[[None] for j in range(73)] for i in range(59)]
        for user in self.users:
            self.unitMap[user.coordinate[1]][user.coordinate[0]].append(str(user.order) + user.direction)
        #print(self.extractMap([55, 11]))
        #print(self.generateUnitMap([55, 11]))
        self.arrow = None
        self.menuIndex = 4
        self.log = ["" for _ in range(3)]
        self.select = ["" for _ in range(6)]
        self.select_mode = 2
        self.select_index = 6
        self.header = ["" for _ in range(2)]
        self.top = [""]
        self.message = ["" for _ in range(6)]
        self.messageIndex = 0
        self.darken = False

    def extractMap(self, coordinate = [55, 11]):
        return [[self.map.squaresMatrix[coordinate[1] + i - 5][coordinate[0] + j - 13].color for j in range(22)] for i in range(11)]

    def generateUnitMap(self, coordinate = [55, 11]):
        return [[self.unitMap[coordinate[1] + i - 5][coordinate[0] + j - 13][-1] for j in range(22)] for i in range(11)]

    def sendInfo(self):
        print([self.extractMap(), self.generateUnitMap(), self.arrow, self.menuIndex, self.log, self.select, self.select_mode, self.select_index, self.header, self.top, self.message, self.darken])

    def listenKeyAction(self, type):
        if type == "message":
            if input("type d") == "d":
                pass
            else:
                if self.messageIndex != 0:
                     self.messageIndex -= 2

    def getMessage(self, message):
        for i in range(len(self.message)):
            self.message[i] = message[self.messageIndex * 72 + i * 12: self.messageIndex * 72 + (i + 1) * 12]
            sendInfo()
            listenKeyAction("message")
            if len(message[(self.messageIndex + 1) * 72: (self.messageIndex + 1) * 72 + 12]) > 0:
                self.messageIndex += 1
                getMessage(message)
            else:
                pass
