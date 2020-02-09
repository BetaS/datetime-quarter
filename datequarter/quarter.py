# -*- coding: utf-8 -*-

import datetime
from typing import Tuple, List, Generator


class DateQuarter:
    _year: int = 0
    _quarter: int = 0

    def __init__(self, year: int, quarter: int):
        year = year + (quarter-1) // 4
        quarter = (quarter-1) % 4 + 1

        self._year = year
        self._quarter = quarter

    @classmethod
    def from_date(cls, date):
        return cls(date.year, ((date.month-1)//3)+1)

    def __repr__(self):
        return f"<DateQuarter-{self._year},{self._quarter}Q>"

    def __gt__(self, other):
        if type(other) == datetime.date:
            return self.__gt__(DateQuarter.from_date(other))
        elif type(other) == DateQuarter:
            if self._year > other._year:
                return True
            elif self._year == other._year and self._quarter > other._quarter:
                return True

            return False
        else:
            raise ArithmeticError()

    def __lt__(self, other):
        if type(other) == datetime.date:
            return self.__lt__(DateQuarter.from_date(other))
        elif type(other) == DateQuarter:
            if self._year < other._year:
                return True
            elif self._year == other._year and self._quarter < other._quarter:
                return True
        else:
            raise ArithmeticError()

        return False

    def __contains__(self, item):
        if type(item) == datetime.date:
            return self.__eq__(DateQuarter.from_date(item))
        else:
            raise ArithmeticError()

    def __eq__(self, other):
        if type(other) == DateQuarter:
            if self._year == other._year and self._quarter == other._quarter:
                return True
        else:
            raise ArithmeticError()

        return False

    def __ge__(self, other):
        if type(other) == datetime.date:
            return self.__ge__(DateQuarter.from_date(other))
        elif type(other) == DateQuarter:
            if self._year > other._year:
                return True
            elif self._year == other._year and self._quarter >= other._quarter:
                return True
        else:
            raise ArithmeticError()

        return False

    def __le__(self, other):
        if type(other) == datetime.date:
            return self.__le__(DateQuarter.from_date(other))
        elif type(other) == DateQuarter:
            if self._year < other._year:
                return True
            elif self._year == other._year and self._quarter <= other._quarter:
                return True
        else:
            raise ArithmeticError()

        return False

    def __getitem__(self, item):
        if item == 0:
            return self._year
        elif item == 1:
            return self._quarter
        else:
            raise KeyError()

    def __add__(self, other):
        if type(other) == int:
            return DateQuarter(self._year, self._quarter + other)
        else:
            raise ArithmeticError()

    def __sub__(self, other):
        if type(other) == int:
            return DateQuarter(self._year, self._quarter - other)
        elif type(other) == DateQuarter:
            quarter = (self._year - other._year) * 4
            quarter += (self._quarter - other._quarter)
            return quarter
        else:
            raise ArithmeticError()

    def year(self) -> int:
        return self._year

    def quarter(self) -> int:
        return self._quarter

    def days(self) -> List[datetime.date]:
        start = self.start_date()
        end = self.end_date()
        curr = start
        while curr <= end:
            yield curr
            curr = curr + datetime.timedelta(days=1)

    def start_date(self) -> datetime.date:
        return datetime.date(year=self._year, month=(self._quarter-1)*3+1, day=1)

    def end_date(self) -> datetime.date:
        return (self+1).start_date() - datetime.timedelta(days=1)

    @classmethod
    def between(cls, start: "DateQuarter", end: "DateQuarter", include_last: bool = False):
        delta = 1 if start < end else -1

        curr = start
        while curr != end:
            yield curr
            curr += delta

        if include_last:
            yield end
