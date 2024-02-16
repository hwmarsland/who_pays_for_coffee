class person: # Class that keeps track of all the important data for each person
    name = ''
    bal = 0
    lastPurchased = ''
    totalBal = 0

    def __init__(self, nameStr):
        self.name = nameStr


class drinkList: # Class used to keep track of the drinks
    dict = {
        'Not Getting Coffee':0,
        'Latte':7,
        'Espresso':6,
        'Black Coffee':3
    } # Formatted as 'name of drink' : price

class peopleList:
    personList = []