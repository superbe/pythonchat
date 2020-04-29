class Organ:
    __pattern = """
    {0} {2} пива на стене, {0} {2} пива!
    Возьми одну, передай мне, {1} {3} пива на стене.
"""
    __empty_pattern = """
    Последняя бутылка пива на стене, последняя бутылка пива!
    Возьми её, передай мне, нет бутылок пива на стене.

    Нет бутылок пива на стене, нет бутылок пива!
    Сходи в магазин, купи ещё, 99 бутылок пива на стене.
"""

    def __init__(self, upper=99, lower=0):
        self.__upper = upper
        self.__lower = lower
        if self.__lower > self.__upper:
            self.__upper, self.__lower = self.__lower, self.__upper
        if self.__lower > 0:
            self.__lower = self.__lower - 1

    @staticmethod
    def __get_bottle_beer(index):
        if 4 < index % 10 or (10 <= index <= 20):
            return 'бутылок'
        elif index % 10 == 1:
            return 'бутылка'
        else:
            return 'бутылки'

    def __count_bottle(self, index=0):
        return self.__empty_pattern if index == 1 else self.__pattern.format(index, index - 1,
                                                                             self.__get_bottle_beer(index),
                                                                             self.__get_bottle_beer(index - 1))

    def whizz(self):
        return ''.join([self.__count_bottle(i) for i in range(self.__upper, self.__lower, -1)])


def song():
    instrument = Organ()
    return instrument.whizz()


def verses(upper: int, lower: int):
    instrument = Organ(upper, lower)
    return instrument.whizz()


if __name__ == '__main__':
    print(song())
    print(verses(5, 8))
