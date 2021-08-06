from .letterMap import letterMap
from .messages import messages
from .cards import cardNames
from random import randint

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
        self.demerit = False
        self.previousCoordinate = [55, 11]

    def calcSettlement(self):
        sum = 0
        for property in self.properties:
            sum += property.getInterest()
        return sum

    def getAllMoney(self):
        sum = self.money
        for property in self.properties:
            sum += property.price
        return sum

class Property():
    def __init__(self, name, price, percentage):
        self.name = name
        self.price = price
        self.percentage = percentage
        self.owner = None
        self.station = None

    def getInterest(self):
        return int(self.price * self.percentage / 100)


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

class StationSquare(Square):
    def __init__(self, isAccessible, isStoppable, color, name, coordinate, properties):
        super(StationSquare, self).__init__(isAccessible, isStoppable, color)
        self.name = name
        self.coordinate = coordinate
        self.properties = properties
        self.prize = None

class CardSquare(Square):
    def __init__(self, isAccessible, isStoppable, color, cards):
        super(CardSquare, self).__init__(isAccessible, isStoppable, color)
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

class Time():
    def __init__(self):
        self.month = 4
        self.monthlyCoefficeints = [0, 0.5, 0.6, 0.9, 1.0, 1.3, 1.6, 1.9, 2, 1.8, 1.2, 0.8, 0.4]
        self.correntMonthlyCoefficient = 1.0
        self.year = 1
        self.limit = 1

    def getTime(self):
        return str(self.year) + "年目" + str(self.month) + "月"

    def update(self):
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.correntMonthlyCoefficient = self.monthlyCoefficeints[self.month]
            self.year += 1

    def hasReachedTheLimit(self):
        return self.year == self.limit + 1

    def isMarchOver(self):
        return self.month == 4

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

class Moving(Mode):
    def __init__(self, previous):
        super(Moving, self).__init__(previous)
        self.mode = "moving"

    def flow(self, model):
        model.sendMoving()

class BlueSquareMode(Mode):
    def __init__(self, previous):
        super(BlueSquareMode, self).__init__(previous)
        self.mode = "blueSquareMode"

    def flow(self, model):
        plus = int(10000 * model.time.correntMonthlyCoefficient)
        model.users[model.userIndex].money += plus
        log = messages[3].replace("$1", model.users[model.userIndex].name)
        log = log.replace("$2", model.kanjiMoney(plus))
        log = log.replace("$3", model.kanjiMoney(model.users[model.userIndex].money))
        model.sendLog(log, self.mode)

class RedSquareMode(Mode):
    def __init__(self, previous):
        super(RedSquareMode, self).__init__(previous)
        self.mode = "redSquareMode"

    def flow(self, model):
        minus = int(10000 * 2 / model.time.correntMonthlyCoefficient)
        model.users[model.userIndex].money -= minus
        if model.users[model.userIndex].money < 0:
            model.users[model.userIndex].money = 0
            log = messages[4].replace("$1", model.users[model.userIndex].name)
            log = log.replace("$2", model.kanjiMoney(minus))
        else:
            log = messages[5].replace("$1", model.users[model.userIndex].name)
            log = log.replace("$2", model.kanjiMoney(minus))
            log = log.replace("$3", model.kanjiMoney(model.users[model.userIndex].money))

        model.sendLog(log, self.mode)

class YellowSquareMode(Mode):
    def __init__(self, previous):
        super(YellowSquareMode, self).__init__(previous)
        self.mode = "yellowSquareMode"

    def flow(self, model):
        if len(model.users[model.userIndex].cards) == 6:
            log = messages[6].replace("$", model.users[model.userIndex].name)
        else:
            newCard = Card(cardNames[randint(0,2)])
            model.users[model.userIndex].cards.append(newCard)
            log = messages[7].replace("$1", model.users[model.userIndex].name)
            log = log.replace("$2", newCard.name)

        model.sendLog(log, self.mode)

class StationSquareMode(Mode):
    def __init__(self, previous):
        super(StationSquareMode, self).__init__(previous)
        self.mode = "stationSquareMode"

    def flow(self, model):
        model.sendSelect()

class BuyingPropery(Mode):
    def __init__(self, previous):
        super(BuyingPropery, self).__init__(previous)
        self.mode = "buyingPropery"

    def flow(self, model):
        user = model.users[model.userIndex]
        property = model.map.squaresMatrix[user.coordinate[1]][user.coordinate[0]].properties[model.selectIndex]
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
        log += " d をおしてください"
        model.selectIndex = 0
        model.sendLog(log, self.mode)

class DestinationSquareMode(Mode):
    def __init__(self, previous):
        super(DestinationSquareMode, self).__init__(previous)
        self.mode = "DestinationSquareMode"

    def flow(self, model):

        farthestUserIndex = 0
        maxDistance = 0
        for index in range(4):
            calclatedDistance = model.calcDistanceFromDestiny(model.users[index].coordinate)
            if maxDistance < calclatedDistance:
                farthestUserIndex = index
                maxDistance = calclatedDistance

        for i in range(4):
            model.users[i].demerit = (i == farthestUserIndex)

        prize = 0
        for property in model.destination.properties:
            prize += property.price
        model.users[model.userIndex].money += int(prize/3)
        model.map.squaresMatrix[model.destination.coordinate[1]][model.destination.coordinate[0]].color = "駅"
        destinationIndex = randint(0,67)
        destinationInfo = model.map.propertyInfo[destinationIndex]
        model.destination = model.map.squaresMatrix[destinationInfo[1][1]][destinationInfo[1][0]]
        model.map.squaresMatrix[model.destination.coordinate[1]][model.destination.coordinate[0]].color = "目駅"
        message = messages[11].replace("$1", model.users[model.userIndex].name)
        message = message.replace("$2", str(prize))
        message = message.replace("$3", model.destination.name)
        message = message.replace("$4", model.users[farthestUserIndex].name)
        model.sendMessage(message, self.mode)

class CardMode(Mode):
    def __init__(self, previous):
        super(CardMode, self).__init__(previous)
        self.mode = "cardMode"

    def flow(self, model):
        model.sendSelect()

class UsingCard(Mode):
    def __init__(self, previous):
        super(UsingCard, self).__init__(previous)
        self.mode = "usingCard"

    def flow(self, model):
        cardname = model.users[model.userIndex].cards.pop(model.selectIndex).name
        dice = cardNames.index(cardname)
        model.users[model.userIndex].steps = randint(1 * (dice + 2), 6 * (dice + 2))
        log = messages[12].replace("$1", cardname)
        log = log.replace("$2", str(model.users[model.userIndex].steps))
        model.sendLog(log, self.mode)

class GettingSettlement(Mode):
    def __init__(self, previous):
        super(GettingSettlement, self).__init__(previous)
        self.mode = "gettingSettlement"

    def flow(self, model):

        message = "けっさんです!けっさんです!けっさんです!!!!!"
        for user in model.users:
            user.money += user.calcSettlement()
            temp = messages[13].replace("$1", user.name)
            temp = messages[13].replace("$2", str(user.calcSettlement()))
            message += temp

        model.sendMessage(message, self.mode)

class Ending(Mode):
    def __init__(self, previous):
        super(Ending, self).__init__(previous)
        self.mode = "ending"

    def flow(self, model):
        max = 0
        for i in range(4):
            if model.users[i].getAllMoney() > model.users[i].getAllMoney():
                max = i
        message = messages[14].replace("$1", model.kanjiMoney(model.users[max].getAllMoney()))
        message = message.replace("$2", str(model.users[max].name))
        model.sendMessage(message, self.mode)
