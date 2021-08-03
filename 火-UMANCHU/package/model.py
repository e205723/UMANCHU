import socket
import pickle
from random import randint
from time import sleep
from .propertyInfo import propertyInfo
from .gameObjects import *

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
        self.darken = False
        self.message = ["" for _ in range(6)]

    def listen(self):
        HOST = socket.gethostbyname(socket.gethostname())
        PORT = 49153
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
                    loadedData = pickle.loads(data)
                    if loadedData[0] == self.users[self.userIndex].ip:
                        sleep(0.3)
                        return loadedData[1]

    def send(self, info):
        for user in self.users:
            HOST = user.ip
            PORT = 49152        # The port used by the server
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((HOST, PORT))
                    s.sendall(pickle.dumps(info))
                    data = s.recv(1024)
            except:
                pass

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

    def kanjiMoney(self, money):
        kanjiMoney = ""
        num = money * 1
        if num != 0:
            if num//100000000 > 0:
                kanjiMoney += str(num//100000000) + "兆"
                num = num % 100000000
            if num//10000 > 0:
                kanjiMoney += str(num//10000) + "億"
                num = num % 10000
            if num > 0:
                kanjiMoney += str(num) + "万"

            kanjiMoney += "円"
        else:
            kanjiMoney = "0円"

        return kanjiMoney

    def getExtractedMap(self, coordinate):
        return [[self.map.squaresMatrix[coordinate[1] + i - 5][coordinate[0] + j - 13].color for j in range(22)] for i in range(11)]

    def getUnitMap(self, coordinate):
        return [[self.unitMap[coordinate[1] + i - 5][coordinate[0] + j - 13][-1] for j in range(22)] for i in range(11)]

    def getArrowDirection(self, coordinate):
        horizontlDistance = (coordinate[0] - self.destination.coordinate[0])
        verticalDistance = (coordinate[1] - self.destination.coordinate[1])
        if horizontlDistance**2 >= verticalDistance**2:
            if horizontlDistance > 0:
                return 1
            else:
                return  3
        else:
            if verticalDistance > 0:
                return  0
            else:
                return 2

    def getHeader(self):
        self.header[0] = self.users[self.userIndex].name + " " + self.kanjiMoney(self.users[self.userIndex].money)
        self.header[1] = self.getDistanceFromDestiny(self.users[self.userIndex].coordinate) + "、" + self.time.getTime()

    def sendInfo(self, type):
        user = self.users[self.userIndex]
        info = [None for _ in range(12)]
        if type == "message":
            info[10] = True
            info[11] = self.message
        elif type == "menu":
            info[0] = self.getExtractedMap(user.coordinate)
            info[1] = self.getUnitMap(user.coordinate)
            info[3] = self.menuIndex
            self.getHeader()
            info[8] = self.header
        elif type == "log":
            info[0] = self.getExtractedMap(user.coordinate)
            info[1] = self.getUnitMap(user.coordinate)
            info[4] = self.log
        elif type == "moving":
            info[0] = self.getExtractedMap(user.coordinate)
            info[1] = self.getUnitMap(user.coordinate)
            info[2] = self.getArrowDirection(user.coordinate)
            info[9] = user.name + " あと" + str(user.steps) + "ほ"
            if "駅" in self.map.squaresMatrix[user.coordinate[1]][user.coordinate[0]].color:
                info[9] += " ここは" + self.map.squaresMatrix[user.coordinate[1]][user.coordinate[0]].name
        elif type == "select":
            info[0] = self.getExtractedMap(user.coordinate)
            info[1] = self.getUnitMap(user.coordinate)
            info[5] = self.select
            info[6] = self.selectThreeOrSix
            info[7] = self.selectIndex
        self.send(info)

    def listenKeyAction(self, type):
        if type == "message":
            keyAction = self.listen()

            if keyAction == "d" or keyAction == "l":
                pass
            elif keyAction == "s" or keyAction == "h":
                if self.messageIndex != 0:
                    self.messageIndex -= 2
                else:
                    self.currentMode.goBack(self)
                    self.messageIndex -= 1
        elif type == "menu":
            keyAction = self.listen()
            if keyAction == "j":
                self.menuIndex = 1
            elif keyAction == "k":
                self.menuIndex = 0
            elif keyAction == "s":
                self.currentMode.goBack(self)
            elif keyAction == "d":
                if self.menuIndex == 0:
                    self.currentMode = BeforeThrowingDice(self.currentMode)
                elif self.menuIndex == 1:
                    if len(self.users[self.userIndex].cards) != 0:
                        self.selectIndex = 0
                        self.selectThreeOrSix = 1
                        self.currentMode = CardMode(self.currentMode)
                    else:
                        pass
        elif type == "select":
            keyAction = self.listen()
            if self.selectThreeOrSix == 0:
                if keyAction == "j" and self.selectIndex != len(self.map.squaresMatrix[self.users[self.userIndex].coordinate[1]][self.users[self.userIndex].coordinate[0]].properties) - 1:
                    self.selectIndex += 1
                elif keyAction == "k" and self.selectIndex != 0:
                    self.selectIndex -= 1
                elif keyAction == "s":
                    self.currentMode.goBack(self)
                elif keyAction == "d":
                    self.selectIndex = 0
                    self.currentMode = BuyingPropery(self.currentMode)
            elif self.selectThreeOrSix == 1:
                if keyAction == "j" and self.selectIndex != len(self.users[self.userIndex].cards) - 1:
                    self.selectIndex += 1
                elif keyAction == "k" and self.selectIndex != 0:
                    self.selectIndex -= 1
                elif keyAction == "s":
                    self.currentMode.goBack(self)
                elif keyAction == "d":
                    self.currentMode = UsingCard(None)

        elif type == "log":
            keyAction = self.listen()
            if keyAction == "d" or keyAction == "l":
                pass
            elif keyAction == "s" or keyAction == "h":
                if self.logIndex != 0:
                    self.logIndex -= 2
                else:
                    self.currentMode.goBack(self)
                    self.logIndex -= 1
        elif type == "moving":
            keyAction = self.listen()
            user = self.users[self.userIndex]

            h = -3 * int(keyAction == "h")
            j = 3 * int(keyAction == "j")
            k = -3 * int(keyAction == "k")
            l = 3 * int(keyAction == "l")

            h2 = -1 * int(keyAction == "h")
            j2 = int(keyAction == "j")
            k2 = -1 * int(keyAction == "k")
            l2 = int(keyAction == "l")

            if keyAction in "hjkl" and self.map.squaresMatrix[user.coordinate[1] + j + k][user.coordinate[0] + h + l].isStoppable and self.map.squaresMatrix[user.coordinate[1] + j2 + k2][user.coordinate[0] + h2 + l2].isAccessible:
                if len(user.visitedSquares) == 0:
                    user.visitedSquares.append(self.map.squaresMatrix[user.coordinate[1]][user.coordinate[0]])
                    user.steps -= 1
                else:
                    if user.visitedSquares[-1] == self.map.squaresMatrix[user.coordinate[1] + j + k][user.coordinate[0] + h + l]:
                        user.visitedSquares.pop(-1)
                        user.steps += 1
                    else:
                        user.visitedSquares.append(self.map.squaresMatrix[user.coordinate[1]][user.coordinate[0]])
                        user.steps -= 1
                self.unitMap[user.coordinate[1]][user.coordinate[0]].remove(str(self.userIndex) + user.direction)
                if not keyAction in "ghjk":
                    keyAction = "k"
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
                self.currentMode = Menu(None)
            elif mode == "desitinationSquareMode":
                self.currentMode = BuyingPropery(None)
            elif mode == "gettingSettlement":
                if self.time.hasReachedTheLimit():
                    self.currentMode = Ending(None)
                else:
                    self.updateUserIndex()
                    self.currentMode = Menu(None)
            elif mode == "ending":
                self.running = False

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
            elif mode in ["blueSquareMode", "redSquareMode", "yellowSquareMode", "buyingPropery"]:
                self.users[self.userIndex].visitedSquares = []
                self.updateUserIndex()
                if self.userIndex == 0:
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
        if self.selectThreeOrSix == 0:
            for property in self.map.squaresMatrix[user.coordinate[1]][user.coordinate[0]].properties:
                self.select[index * 2] = property.name
                secondRow = self.kanjiMoney(property.price) + " " +str(property.percentage) + "%"
                if not property.owner is None:
                    secondRow = secondRow + " " + property.owner
                self.select[index * 2 + 1] = secondRow
                index += 1
        else:
            for card in self.users[self.userIndex].cards:
                self.select[index] = card.name
                index += 1
        self.sendInfo(type)
        self.listenKeyAction(type)
