import random

class Model():
    def __init__(self, UserIPList, userNameList):
        self.users = [User(userIP, userName, order, [55, 11], 'u') for userIP, userName, order in zip(UserIPList, userNameList, range(4))]
        self.map = Map()
        self.unitMap = [[[None] for j in range(73)] for i in range(59)]
        for user in self.users:
            self.unitMap[user.coordinate[1]][user.coordinate[0]].append(str(user.order) + user.direction)
        print(self.extractMap([55, 11])[5][13])
        print(self.generateUnitMap([55, 11])[5][13])
        self.arrow = None

    def extractMap(self, coordinate):
        return [[self.map.squaresMatrix[coordinate[1] + i - 5][coordinate[0] + j - 13].color for j in range(22)] for i in range(11)]

    def generateUnitMap(self, coordinate):
        return [[self.unitMap[coordinate[1] + i - 5][coordinate[0] + j - 13][-1] for j in range(22)] for i in range(11)]

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
        #initialize a user's money with 10000000
        self.money = 10000000
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
    def __init__(self, name, price):
        self.name = name
        self.price = price
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
    def __init__(self, isAccessible, isStoppable, color, name, properties, prize):
        super(StationSquare, self).__init__(isAccessible, isStoppable, color)
        self.name = name
        self.properties = properties
        self.prize = prize

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
    def __init__(self):
        self.squaresMatrix = [[self.letterToSquareClass(letterMap[i][j]) for j in range(len(letterMap[i]))] for i in range(len(letterMap))]

    def letterToSquareClass(self, letter):
        if letter == "青":
            return BlueOrRedSquare(True, True, letter, 1000000)
        elif letter == "黄":
            return CardSquare(True, True, letter, [])
        elif letter == "赤":
            return BlueOrRedSquare(True, True, letter, -1000000)
        elif letter == "星":
            return CardMarketSquare(True, True, letter, [])
        elif letter == "駅":
            return StationSquare(True, True, letter, "name", [], 10000000)
        elif letter == "縦":
            return Square(True, False, letter)
        elif letter == "横":
            return Square(True, False, letter)
        elif letter == "緑":
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

greenSquares = ["緑", "草", "木"]

letterMap = [
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "黄", "横", "横", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "駅", "横", "横", "赤", "横", "横", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "赤", "横", "横", "黄", "横", "横", "赤", "横", "横", "黄", "横", "横", "青", "横", "横", "駅", "横", "横", "駅", "横", "横", "駅", "横", "横", "青", "横", "横", "星", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "青", "緑", "緑", "緑", "緑", "緑", "赤", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "星", "緑", "緑", "緑", "緑", "緑", "駅", "横", "横", "駅", "横", "横", "赤", "横", "横", "駅", "横", "横", "黄", "横", "横", "駅", "緑", "緑", "緑", "緑", "緑", "赤", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "駅", "横", "横", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "青", "緑", "緑", "駅", "緑", "緑", "緑", "緑", "緑", "赤", "緑", "緑", "緑", "緑", "緑", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "駅", "緑", "緑", "赤", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "青", "緑", "緑", "駅", "横", "横", "駅", "横", "横", "駅", "緑", "緑", "緑", "緑", "緑", "駅", "緑", "緑", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "黄", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "水", "赤", "水", "緑", "緑", "緑", "緑", "駅", "横", "横", "駅", "緑", "緑", "緑", "緑", "緑", "駅", "横", "横", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "水", "縦", "水", "水", "水", "緑", "水", "水", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "水", "水", "緑", "緑", "緑", "水", "水", "水", "縦", "緑", "緑", "水", "水", "水", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "駅", "横", "横", "青", "横", "横", "青", "横", "横", "赤", "横", "横", "赤", "横", "横", "青", "緑", "緑", "水", "水", "水", "水", "緑", "水", "水", "水", "水", "赤", "横", "横", "星", "横", "横", "黄", "横", "横", "青", "横", "横", "黄", "横", "横", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "水", "水", "水", "水", "水", "水", "水", "水", "水", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "水", "水", "水", "水", "水", "水", "水", "水", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "黄", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "黄", "緑", "水", "水", "水", "水", "水", "水", "緑", "緑", "緑", "緑", "駅", "横", "横", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "駅", "横", "横", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "水", "水", "水", "緑", "水", "水", "水", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "水", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "駅", "緑", "緑", "緑", "緑", "緑", "青", "緑", "緑", "緑", "緑", "緑", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "青", "緑", "緑", "緑", "緑", "緑", "緑", "水", "緑", "緑", "緑", "緑", "駅", "横", "横", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "青", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "青", "横", "横", "黄", "横", "横", "駅", "横", "横", "駅", "横", "横", "駅", "横", "横", "星", "横", "横", "黄", "横", "横", "赤", "横", "横", "青", "横", "横", "黄", "横", "横", "駅", "横", "横", "駅", "緑", "緑", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "青", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "駅", "横", "横", "駅", "緑", "緑", "緑", "緑", "緑", "駅", "横", "横", "青", "横", "横", "赤", "緑", "緑", "緑", "緑", "緑", "赤", "緑", "緑", "緑", "緑", "緑", "駅", "横", "横", "駅", "横", "横", "赤", "横", "横", "駅", "横", "横", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "赤", "横", "横", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "黄", "横", "横", "駅", "緑", "緑", "緑", "緑", "緑", "青", "緑", "緑", "緑", "緑", "緑", "駅", "横", "横", "駅", "横", "横", "黄", "緑", "緑", "緑", "緑", "緑", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "黄", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "駅", "緑", "緑", "駅", "緑", "緑", "緑", "緑", "緑", "黄", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "赤", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "駅", "横", "横", "駅", "緑", "緑", "緑", "緑", "緑", "駅", "緑", "緑", "駅", "横", "横", "駅", "緑", "緑", "黄", "横", "横", "赤", "横", "横", "青", "横", "横", "赤", "横", "横", "星", "横", "横", "青", "横", "横", "黄", "横", "横", "赤", "横", "横", "青", "横", "横", "星", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "縦", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "駅", "横", "横", "黄", "横", "横", "赤", "横", "横", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "駅", "横", "横", "駅", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"],
["緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑", "緑"]
]

#random.randint(0, 2)
