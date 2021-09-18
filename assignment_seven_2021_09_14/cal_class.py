class Cal(object):
    def __init__(self, month: str, day: int, year: int):
        self.month = month
        self.day = day
        self.year = year

    def __str__(self) -> str:
        return "{a} {b}, {c}".format(a = self.month, b = self.day, c = self.year)

    def __eq__(self, o: object) -> bool:
        if type(o) != Cal: return False
        return self.month == o.month and self.day == o.day and self.year == o.year

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)

    def __lt__(self, o: object) -> bool:
        if self.__eq__(o): 
            return False
        if self.year != o.year:
            return self.year < o.year
        elif self.month != o.month:
            return self.month < o.month
        elif self.day != o.day:
            return self.day < o.day
        return False

    def __gt__(self, o: object) -> bool:
        return not self.__lt__(o) and self.__ne__(o)
