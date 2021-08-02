from propertyInfo import propertyInfo
from gameObjects import *
from random import randint

class Model():
    def __init__(self, UserIPList, userNameList):
        self.running = True
        self.users = [User(userIP, userName, order, [55, 11], 'k') for userIP, userName, order in zip(UserIPList, userNameList, range(4))]
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
        self.arrow = 4
        #self.menuはいらない、クライアント側にある
        self.menuIndex = 0
        self.log = ["" for _ in range(3)]
        self.select = ["" for _ in range(6)]
        self.selectThreeOrSix = 0
        self.selectIndex = 0
        self.header = ["" for _ in range(2)]
        self.top = ""
        self.darken = False
        self.message = ["" for _ in range(6)]

    def run(self):
        while self.running:
            if  self.currentMode is None:
                self.currentMode = Opening(None)
                self.currentMode.flow(self)
            else:
                self.currentMode.flow(self)

    def updateUserIndex(self):
        if self.userIndex == 3:
            self.userIndex = 0
        else:
            self.userIndex += 1

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

    def getExtractedMap(self, coordinate):
        return [[self.map.squaresMatrix[coordinate[1] + i - 5][coordinate[0] + j - 13].color for j in range(22)] for i in range(11)]

    def getUnitMap(self, coordinate):
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
        user = self.users[self.userIndex]
        if type == "message":
            info = [None for _ in range(12)]
            info[10] = True
            info[11] = self.message
            print(info)
        elif type == "menu":
            info = [None for _ in range(12)]
            info[0] = self.getExtractedMap(user.coordinate)
            info[1] = self.getUnitMap(user.coordinate)
            info[3] = self.menuIndex
            self.getHeader()
            info[8] = self.header
            info[10] = False
            print(info)
        elif type == "log":
            info = [None for _ in range(12)]
            info[0] = self.getExtractedMap(user.coordinate)
            info[1] = self.getUnitMap(user.coordinate)
            info[8] = self.message
            info[10] = False
            print(info)
        elif type == "moving":
            info = [None for _ in range(12)]
            info[0] = self.getExtractedMap(user.coordinate)
            info[1] = self.getUnitMap(user.coordinate)
            info[2] = user.getArrowDirection(user.coordinate)
            info[9] = user.name + " あと" + str(user.steps) + "ほ"
            print(info)
        elif type == "select":
            info = [None for _ in range(12)]
            info[0] = self.getExtractedMap(user.coordinate)
            info[1] = self.getUnitMap(user.coordinate)
            info[5] = self.select
            info[6] = self.selectThreeOrSix
            info[7] = self.selectIndex

        else:
            print([self.getExtractedMap(user.coordinate), self.getUnitMap(user.coordinate), self.arrow, self.menuIndex, self.log, self.select, self.selectThreeOrSix, self.selectIndex, self.header, self.top, self.darken, self.message])

    def listenKeyAction(self, type):
        if type == "message":
            keyAction = input("type d: ")
            if keyAction == "d" or keyAction == "l":
                pass
            elif keyAction == "s" or keyAction == "h":
                if self.messageIndex != 0:
                    self.messageIndex -= 2
                else:
                    self.currentMode.goBack(self)
                    self.messageIndex -= 1
        elif type == "menu":
            keyAction = input("type j or k or d: ")
            if keyAction == "j" and self.menuIndex != 0:
                self.menuIndex -= 1
            elif keyAction == "k" and self.menuIndex != 1:
                self.menuIndex += 1
            elif keyAction == "s":
                self.currentMode.goBack(self)
            elif keyAction == "d":
                self.menuIndex = 0
                if self.menuIndex == 0:
                    self.currentMode = BeforeThrowingDice(self.currentMode)
                elif self.menuIndex == 1:
                    if len(self.users[self.userIndex].cards) != 0:
                        '''
                        カードモード
                        '''
                        self.selectIndex = 0
                        self.selectThreeOrSix = 1
                        self.currentMode = CardMode(self.currentMode)
                    else:
                        pass
        elif type == "select":
            keyAction = input("type j or k or d: ")
            if self.selectThreeOrSix == 0:
                if keyAction == "j" and self.selectIndex != 0:
                    self.selectIndex -= 1
                elif keyAction == "k" and self.selectIndex != len(self.map.squaresMatrix[self.users[self.userIndex].coordinate[1]][self.users[self.userIndex].coordinate[0]].properties) - 1:
                    self.selectIndex += 1
                elif keyAction == "s":
                    self.currentMode.goBack(self)
                elif keyAction == "d":
                    self.selectIndex = 0
                    self.currentMode = BuyingPropery(self.currentMode)
            elif self.selectThreeOrSix == 1:
                if keyAction == "j" and self.selectIndex != 0:
                    self.selectIndex -= 1
                elif keyAction == "k" and self.selectIndex != len(self.users[self.userIndex].cards) - 1:
                    self.selectIndex += 1
                elif keyAction == "s":
                    self.currentMode.goBack(self)
                elif keyAction == "d":
                    pass
                    self.currentMode = UsingCard(None)

        elif type == "log":
            keyAction = input("type s or d or h or l: ")
            if keyAction == "d" or keyAction == "l":
                pass
            elif keyAction == "s" or keyAction == "h":
                if self.logIndex != 0:
                    self.logIndex -= 2
                else:
                    self.currentMode.goBack(self)
                    self.logIndex -= 1
        elif type == "moving":
            keyAction = input("type h or j or k or l:  ")
            user = self.users[self.userIndex]

            h = -3 * int(keyAction == "h")
            j = 3 * int(keyAction == "j")
            k = = -3 * int(keyAction == "k")
            l = 3 * int(keyAction == "l")

            if self.map.squaresMatrix[user.coordinate[1] + j + k][user.coordinate[0] + h + l].isStoppable:
                if len(self.visitedSquares) == 0:
                    self.visitedSquares.append(self.map.squaresMatrix[user.coordinate[1]][user.coordinate[0]])
                    user.steps -= 1
                else:
                    if self.visitedSquares[-1] == self.map.squaresMatrix[user.coordinate[1] + j + k][user.coordinate[0] + h + l]:
                        self.visitedSquares.pop(-1)
                        user.steps += 1
                    else:
                        self.visitedSquares.append(self.map.squaresMatrix[user.coordinate[1]][user.coordinate[0]])
                        user.steps -= 1
                self.unitMap[user.coordinate[1]][user.coordinate[0]].removing(str(self.userIndex) + user.direction)
                self.unitMap[user.coordinate[1] + j + k][user.coordinate[0] + h + l].append(str(self.userIndex) + keyAction)
                user.coordinate = [user.coordinate[0] + h + l, user.coordinate[1] + j + k]
                user.direction = keyAction

    def sendMessage(self, message, mode):
        type = "message"
        for i in range(6):
            self.message[i] = message[self.messageIndex * 72 + i * 12: self.messageIndex * 72 + (i + 1) * 12]
        self.sendInfo(type)
        self.listenKeyAction(type)

        if len(message[(self.messageIndex + 1) * 72: (self.messageIndex + 1) * 72 + 12]) > 0:
            self.messageIndex += 1
            self.sendMessage(message, mode)
        else:
            self.messageIndex = 0
            if mode == "opening":
                self.currentMode = Menu(self.currentMode)
            elif mode == "desitinationSquareMode":
                self.currentMode = StationSquareMode(None)
            elif mode == "gettingSettlement":
                if self.time.hasReachedTheLimit():
                    self.currentMode = Ending(None)
            elif mode == "ending":
                self.running False


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
            self.sendLog(log, mode)
        else:
            self.logIndex = 0
            if mode == "beforeThrowingDice":
                self.currentMode = AfterThrowingDice(None)
            elif mode in ["afterThrowingDice", "usingCard"]:
                self.currentMode = Moving(self.currentMode)
            elif mode in ["blueSquareMode", "redSquareMode", "yellowSquareMode", "buyPropery"]:
                self.updateUserIndex()
                if seld.userIndex == 0:
                    self.time.update()
                    if self.time.isMarchOver():
                        self.currentMode = GettingSettlement(None)
                    else:
                        self.currentMode =  Menu(None)
                else:
                    self.currentMode =  Menu(None)

    def sendMoving(self):
        type = "moving"
        while self.users[self.userIndex].steps != 0:
            self.sendInfo(type)
            self.listenKeyAction(type)
        if self.users[self.userIndex].steps == 0:
            colorOfArrived = self.map.squaresMatrix[self.users[self.userIndex].coordinate[1]][self.users[self.userIndex].coordinate[0]].color
            if colorOfArrived == "目駅":
                self.currentMode = DesitinationSquareMode(None)
                pass
            elif colorOfArrived == "駅":
                self.selectIndex = 0
                self.selectThreeOrSix = 0
                self.currentMode = StationSquareMode(None)
                pass
            elif colorOfArrived == "青":
                self.currentMode = BlueSquareMode(None)

            elif colorOfArrived == "赤":
                self.currentMode = RedSquareMode(None)

            elif colorOfArrived == "黄":
                self.currentMode = YellowSquareMode(None)
    def sendSelect(self):
        type = "select"
        user = self.users[self.userIndex]
        index = 0
        self.select = ["" for _ in range(6)]
        if selectThreeOrSix == 0:
            for property in self.map.squaresMatrix[user.coordinate[1]][user.coordinate[0]].properties:
                self.select[i * 2] = property.name
                secondRow = property.kanjiPrice() + " " +str(property.percentage) + "%"
                if not property.owner is None:
                    secondRow = secondRow + " " + property.owner
                self.select[i * 2 + 1] = secondRow
                index += 1
        else:
            for card in self.users[self.userIndex].cards:
                self.select[index] = card.name
                index += 1
        self.sendInfo(type)
        self.listenKeyAction(type)
