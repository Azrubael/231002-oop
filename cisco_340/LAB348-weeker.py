class WeekDayError(Exception):
    pass
	

class Weeker:
    __week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        if day not in self.__week_days:
            raise WeekDayError
        self.day = day

    def __str__(self):
        return self.day

    def add_days(self, n):
        if not isinstance(n, int) or n < 0:
            print("Wrong increment value: ",n)
            raise WeekDayError
        index = self.__week_days.index(self.day)
        new_index = index + n
        if new_index > 6:
            new_index %= 7
        self.day = self.__week_days[new_index]

    def subtract_days(self, n):
        if not isinstance(n, int) or n < 0:
            print("Wrong decrement value: ",)
            raise WeekDayError
        index = self.__week_days.index(self.day)
        new_index = index - n
        if new_index < -7:
            new_index = new_index % 7
        self.day = self.__week_days[new_index]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
    