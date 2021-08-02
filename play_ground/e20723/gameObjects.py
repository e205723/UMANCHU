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
        self.cards = [Card("きゅうこうカード")]
        self.steps = 0
        self.visitedSquares = []

    def kanijMoney(self):
        kanjiMoney = ""
        #値渡し
        num = self.money * 1
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

    def kanjiPrice(self):
        kanjiPrice = ""
        num = self.price * 1
        if num != 0:
            if num//100000000 > 0:
                kanjiPrice += str(num//100000000) + "兆"
                num = num % 100000000
            if num//10000 > 0:
                kanjiPrice += str(num//10000) + "億"
                num = num % 10000
            if num > 0:
                kanjiPrice += str(num) + "万"

            kanjiPrice += "円"
        else:
            kanjiPrice = "0円"

        return kanjiPrice


class Card():
    def __init__(self, name):
        self.name = name

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

    def isMarchOver(self):
        return self.mangth == 4

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
        model.sendMessage(messages[0].replace("$", model.destination.name), self.mode)

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
        model.sendLog(messages[1], self.mode)

class AfterThrowingDice(Mode):
    def __init__(self, previous):
        super(AfterThrowingDice, self).__init__(previous)
        self.mode = "afterThrowingDice"

    def flow(self, model):
        model.users[model.userIndex].steps = randint(1, 6)
        model.sendLog(messages[2].replace("$", str(model.users[model.userIndex].steps)), self.mode)

class Move(Mode):
    def __init__(self, previous):
        super(Move, self).__init__(previous)
        self.mode = "move"

    def flow(self, model):
        model.sendMove()

class BlueSquareMode(Mode):
    def __init__(self, previous):
        super(BlueSquareMode, self).__init__(previous)
        self.mode = "blueSquareMode"

    def flow(self, model):
        plus = int(10000 * model.time.correntMonthlyCoefficient)
        model.users[model.userIndex].money += plus
        log = messages[3].replace("$1", model.users[model.userIndex].name)
        log = log.replace("$2", str(plus))
        log = log.replace("$3", model.users[model.userIndex].kanjiMoney())
        model.sendLog(log, self.mode)

class RedSquareMode(Mode):
    def __init__(self, previous):
        super(RedSquareMode, self).__init__(previous)
        self.mode = "redSquareMode"

    def flow(self, model):
        minus = int(10000 * model.time.correntMonthlyCoefficient)
        model.users[model.userIndex].money -= minus
        if model.users[model.userIndex].money < 0:
            model.users[model.userIndex].money = 0
            log = messages[3].replace("$1", model.users[model.userIndex].name)
            log = log.replace("$2", str(-minus))
        else:
            log = messages[4].replace("$1", model.users[model.userIndex].name)
            log = log.replace("$2", str(-minus))
            log = log.replace("$3", model.users[model.userIndex].kanjiMoney())

        model.sendLog(log, self.mode)

class YellowSquareMode(Mode):
    def __init__(self, previous):
        super(YellowSquareMode, self).__init__(previous)
        self.mode = "yellowSquareMode"

    def flow(self, model):
        if len(model.users[model.userIndex].cards) == 6:
            log = messages[6].replace("$", model.users[model.userIndex].name)
        else:
            newCard = Card(cards[randint(0,2)])
            self.users[self.userIndex].cards.append(newCard)
            log = messages[7].replace("$1", model.users[model.userIndex].name)
            log = log.replace("$2", newCard.name)

        model.sendLog(log, self.mode)

class StationSquareMode(Mode):
    def __init__(self, previous):
        super(StationSquareMode, self).__init__(previous)
        self.mode = "stationSquareMode"

    def flow(self, model):
        model.sendSelect()

class BuyPropery(Mode):
    def __init__(self, previous):
        super(BuyPropery, self).__init__(previous)
        self.mode = "buyPropery"

    def flow(self, model):
        user = model.users[model.userIndex]
        property = model.map.squaresMatrix[user.coordinate[1]][user.coordinate[0]].properties[selectIndex]
        log = ""
        if property.owner is None:
            if property.price > user.money:
                log = messages[8].replace("$", property.name)
            else:
                log = messages[9].replace("$", property.name)
                user.properties.append(property)
                property.owner = user.name
        else:
            log = messages[10].replace("$1", property.owner)
            log = log.replace("$2", property.name)
        log += " おかいものをつづけたいばあいは s をおしてください。おわるばあいは d をおしてください"

        model.sendLog(log, self.mode)

class DesitinationSquareMode(Mode):
    def __init__(self, previous):
        super(DesitinationSquareMode).__init__(previous)
        self.mode = desitinationSquareMode

    def flow(self, model):
        pass
