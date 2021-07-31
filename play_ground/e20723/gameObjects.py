import random

class Unit():
    def __init__(self, coordinate, direction):
        self.coordinate = coordinate
        self.direction = direction

class User(Unit):
    def __init__(self, userIP, userName, order, coordinate, direction):
        super(User, self).__init__(coordinate, direction)
        self.order = order
        self.userIP = userIP
        self.userName = userName
        #initialize a user's money with 1000
        self.money = 1000
        self.properties = []
        self.cards = []
        self.steps = 0

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
            return StationSquare(True, True, letter, *self.propertyInfo[self.index])
        elif letter == "縦":
            return Square(True, False, letter)
        elif letter == "横":
            return Square(True, False, letter)
        elif letter == "緑":
            greenSquares = ["緑", "草", "木"]
            return Square(False, False, greenSquares[random.randint(0,2)])
        elif letter == "水":
            return Square(False, False, letter)

    def getAllPossiblePaths():
        pass

class Time():
    def __init__(self, month, monthlyCoefficeints, year):
        self.month = month
        self.monthlyCoefficeints = monthlyCoefficeints
        self.year = year
