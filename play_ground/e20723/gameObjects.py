from letterMap import letterMap
from messages import messages
from random import randint
import copy

class Unit():
    def __init__(self, coordinate, direction):
        self.coordinate = coordinate
        self.direction = direction

class User(Unit):
    def __init__(self, ip, name, order, coordinate, direction):
        super(User, self).__init__(coordinate, direction)
        self.order = order
        self.ip = ip
        self.name = name
        #initialize a user's money with 1000
        self.money = 10000
        self.properties = []
        self.cards = []
        self.steps = 0
        self.visitedSquares = []

    def kanijMoney(self):
        kanjiMoney = ""
        #値渡し
        num = self.money * 1
        if num//100000000 > 0:
            kanjiMoney += str(num//100000000) + "兆"
            num = num % 100000000
        if num//10000 > 0:
            kanjiMoney += str(num//10000) + "億"
            num = num % 10000
        if num > 0:
            kanjiMoney += str(num) + "万"

        kanjiMoney += "円"

        return kanjiMoney

    def throwDice():
        pass

    def useCard():
        pass

    def buyProrerties():
        pass

class Demerit(Unit):
    def __init__(self, coordinate, direction):
        super(Demerit, self).__init__(coordinate)
        self.userToFollow = None

    def takeMoney():
        pass

    def takeCards():
        pass

class Property():
    def __init__(self, name, price, percentage):
        self.name = name
        self.price = price
        self.percentage = percentage
        self.owner = None
        self.station = None

class Card():
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Square():
    def __init__(self, isAccessible, isStoppable, color):
        self.isAccessible = isAccessible
        self.isStoppable = isStoppable
        self.color = color

class BlueOrRedSquare(Square):
    def __init__(self, isAccessible, isStoppable, color, priceToAdd):
        super(BlueOrRedSquare, self).__init__(isAccessible, isStoppable, color)
        self.priceToAdd = priceToAdd

    def operateMoney():
        pass

class StationSquare(Square):
    def __init__(self, isAccessible, isStoppable, color, name, coordinate, properties):
        super(StationSquare, self).__init__(isAccessible, isStoppable, color)
        self.name = name
        self.coordinate = coordinate
        self.properties = properties
        self.prize = None

    def isBuyingUp():
        pass

    def listAffordable():
        pass

class CardSquare(Square):
    def __init__(self, isAccessible, isStoppable, color, cards):
        super(CardSquare, self).__init__(isAccessible, isStoppable, color)
        self.cards = cards

class CardMarketSquare(Square):
    def __init__(self, isAccessible, isStoppable, color, cards):
        super(CardMarketSquare, self).__init__(isAccessible, isStoppable, color)
        self.cards = cards

class NatureSquare(Square):
    def __init__(self, isAccessible, isStoppable, color):
        super(NatureSquare, self).__init__(isAccessible, isStoppable, color)

class Map():
    def __init__(self, propertyInfo, letterMap):
        self.index = -1
        self.propertyInfo = propertyInfo
        self.squaresMatrix = [[self.letterToSquareClass(letterMap[i][j]) for j in range(len(letterMap[i]))] for i in range(len(letterMap))]

    def letterToSquareClass(self, letter):
        if letter == "青":
            return BlueOrRedSquare(True, True, letter, 1000)
        elif letter == "黄":
            return CardSquare(True, True, letter, [])
        elif letter == "赤":
            return BlueOrRedSquare(True, True, letter, -1000)
        elif letter == "星":
            return CardMarketSquare(True, True, letter, [])
        elif letter == "駅":
            self.index += 1
            stationSquare = StationSquare(True, True, letter, *self.propertyInfo[self.index])
            for property in self.propertyInfo[self.index][2]:
                property.station = stationSquare
            return stationSquare
        elif letter == "縦":
            return Square(True, False, letter)
        elif letter == "横":
            return Square(True, False, letter)
        elif letter == "緑":
            greenSquares = ["緑", "草", "木"]
            return Square(False, False, greenSquares[randint(0,2)])
        elif letter == "水":
            return Square(False, False, letter)

    def getAllPossiblePaths():
        pass

class Time():
    def __init__(self):
        self.month = 4
        self.monthlyCoefficeints = [0, 0.5, 0.6, 0.9, 1.0, 1.3, 1.6, 1.9, 2, 1.8, 1.2, 0.8, 0.4]
        self.correntMonthlyCoefficient = 1.0
        self.year = 1
        self.limit = 4

    def getTime(self):
        return str(self.year) + "年目" + str(self.month) + "月"

    def update(self):
        self.month += 1
        if self.month == 13:
            self.mongth = 1
            self.correntMonthlyCoefficient = self.monthlyCoefficeints[self.month]
            self.year += 1

    def hasReachedTheLimit(self):
        return self.year == self.limit + 1

class Mode():
    def __init__(self, previous):
        self.previous = previous
        self.mode = None

    def goBack(self, model):
        if not self.previous is None:
            model.currentMode =  self.previous

    def flow(self, model):
        pass

class Opening(Mode):
    def __init__(self, previous):
        super(Opening, self).__init__(previous)
        self.mode = "opening"

    def flow(self, model):
        model.sendMessage(messages[0].replace("$", model.destination.name))

class Menu(Mode):
    def __init__(self, previous):
        super(Menu, self).__init__(previous)
        self.mode = "menu"

    def flow(self, model):
        model.sendMenu()

class BeforeThrowingDice(Mode):
    def __init__(self, previous):
        super(BeforeThrowingDice, self).__init__(previous)
        self.mode = "beforeThrowingDice"

    def flow(self, model):
        model.sendLog(messages[1], "beforeThrowingDice")
        '''
        Moveモードを実装したらコメントアウト取り消し
        '''
        #self.currentMode = Move(self.currentMode)

class AfterThrowingDice(Mode):
    def __init__(self, previous):
        super(AfterThrowingDice, self).__init__(previous)
        self.mode = "afterThrowingDice"

    def flow(self, model):
        model.users[model.userIndex].steps = randint(1, 6)
        model.sendLog(messages[2].replace("$", str(model.users[model.userIndex].steps)), "afterThrowingDice")
'''
Moveクラスを作成
'''

class Move(Mode):
    def __init__(self, previous):
        super(AfterThrowingDice, self).__init__(previous)
        self.mode = "move"

    def flow(self, model):
        model.sendMove()
