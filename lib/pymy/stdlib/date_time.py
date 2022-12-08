import math
from calendar import isleap, leapdays, monthrange
from datetime import datetime as BaseDateTime


class DateTime(BaseDateTime):
    HOURS_PER_DAY = 24
    MINUTES_PER_HOUR = 60
    SECONDS_PER_MINUTE = 60
    MILLISECONDS_PER_SECOND = 1000
    MICROSECONDS_PER_MILLISECOND = 1000
    MICROSECONDS_PER_SECOND = 1000000
    FORMAT_DEFAULT_DATETIME = '%Y-%m-%d %H:%M:%S'
    FORMAT_DEFAULT_DATE = '%Y-%m-%d'

    @classmethod
    def convertDate(cls, date_time, date_only: bool = False) -> str:
        format = cls.FORMAT_DEFAULT_DATETIME if date_only is False else cls.FORMAT_DEFAULT_DATE
        date_time = cls.make(date_time)

        return date_time.strftime(format)

    @classmethod
    def make(cls, date_time):

        # match True:
        #     case isinstance(date_time, cls):
        #         date_time = cls.fromtimestamp(date_time.timestamp())
        #     case isinstance(date_time, BaseDateTime):
        #         date_time = cls.fromtimestamp(date_time.timestamp())
        #     case isinstance(date_time, (int, float)):
        #         date_time = cls.fromtimestamp(date_time)
        #     case _:
        #         date_time = cls.fromisoformat(date_time)

        if isinstance(date_time, cls):
            date_time = cls.fromtimestamp(date_time.timestamp())
        elif isinstance(date_time, BaseDateTime):
            date_time = cls.fromtimestamp(date_time.timestamp())
        elif isinstance(date_time, (int, float)):
            date_time = cls.fromtimestamp(date_time)
        else:
            date_time = cls.fromisoformat(date_time)

        return date_time

    def is_leap(self) -> bool:
        return isleap(self.year)

    def leap_days_by(self, y1: int, y2: int):
        return leapdays(y1, y2)

    # Checks add days
    def __check_days_return(self, year: int, month: int, day: int) -> tuple:
        _year = year
        _month = month
        current_day = day
        max_day = self.days_of_month_by(year, month)
        add_month = 0
        if day > max_day:
            while _month <= 12:
                _m = _month
                _month += 1
                _max_day = self.days_of_month_by(_year, _m)
                if _m == 12:
                    _month = 1
                    _year += 1
                if (year, month) == (_year, _m) and day > _max_day:
                    day -= _max_day - current_day
                    add_month += 1
                    continue
                if day >= 1 and day <= _max_day:
                    break
                elif day > _max_day:
                    day -= _max_day
                    add_month += 1
                elif day < 1:
                    day = _max_day + day
                    break

            month += add_month
            add_year = math.floor(month / 12)
            month = month - add_year * 12
            year += add_year

        return (year, month, day)

    def set_year(self, year: int):
        year, month, day = self.__check_days_return(year, self.month, self.day)

        return self.replace(year=year, month=month, day=day)

    def add_year(self, year: int):
        year = self.year + year
        year, month, day = self.__check_days_return(year, self.month, self.day)

        return self.replace(year=year, month=month, day=day)

    def sub_year(self, year: int):
        year = self.year - year
        year, month, day = self.__check_days_return(year, self.month, self.day)

        return self.replace(year=year, month=month, day=day)

    def set_month(self, month: int):
        year, month, day = self.__check_days_return(self.year, month, self.day)

        return self.replace(year=year, month=month, day=day)

    def add_month(self, month: int):
        year = self.year
        month = self.month + month
        add_year = 0
        if month > 12:
            add_year = math.floor(month / 12)
            month = month - add_year * 12
            year += add_year

        year, month, day = self.__check_days_return(year, month, self.day)

        return self.replace(year=year, month=month, day=day)

    def sub_month(self, month: int):
        sub_year = math.floor(month / 12)
        year = self.year - sub_year
        month_remd = month % 12
        month = self.month - month_remd
        if month < 1:
            month = 12 + month
            year -= 1

        year, month, day = self.__check_days_return(year, month, self.day)

        return self.replace(year=year, month=month, day=day)

    def set_day(self, day: int):

        return self.replace(day=day)

    def add_day(self, day: int):
        day = self.day + day
        year = self.year
        month = self.month

        year, month, day = self.__check_days_return(year, month, day)

        return self.replace(year=year, month=month, day=day)

    def sub_day(self, day: int):
        _year = self.year
        _month = self.month
        # max_day = self.days_of_month_by(self.year, self.month)
        sub_month = 0
        while _month >= 1:
            _m = _month
            _month -= 1
            _max_day = self.days_of_month_by(_year, _m)
            if _m == 1:
                _month = 12
                _year -= 1
            if (self.year, self.month) == (_year, _m):
                day -= self.day
                sub_month += 1
                continue
            if day >= 1 and day <= _max_day:
                day = _max_day - day
                if day == 0:
                    _max_day2 = self.days_of_month_by(_year, _month)
                    day = _max_day2
                    sub_month += 1
                break
            elif day > _max_day:
                day -= _max_day
                sub_month += 1
            elif day < 1:
                day = _max_day + day
                break

        sub_year = math.floor(sub_month / 12)
        month_remd = sub_month % 12
        year = self.year - sub_year
        month = self.month - month_remd
        if month < 1:
            month = 12 + month
            year -= 1

        return self.replace(year=year, month=month, day=day)

    def set_hour(self, hour: int):

        return self.replace(hour=hour)

    def add_hour(self, hour: int):
        hour = self.hour + hour
        year = self.year
        month = self.month
        day = self.day
        while hour >= 24:
            hour -= 24
            day += 1
            _max_day = self.days_of_month_by(year, month)
            if day > _max_day:
                day -= _max_day
                month += 1
            if month > 12:
                month -= 12
                year += 1

        return self.replace(year=year, month=month, day=day, hour=hour)

    def sub_hour(self, hour: int):
        year = self.year
        month = self.month
        day = self.day
        current_hour = self.hour
        if hour <= current_hour:
            hour = current_hour - hour
        else:
            hour -= current_hour
            day -= 1
            if day == 0:
                month -= 1
                if month == 0:
                    month = 12
                    year -= 1
                _max_day = self.days_of_month_by(year, month)
                day = _max_day
        while hour >= 24:
            hour -= 24
            day -= 1
            if day == 0:
                month -= 1
                if month == 0:
                    month = 12
                    year -= 1
                _max_day = self.days_of_month_by(year, month)
                day = _max_day
            print(hour)

        return self.replace(year=year, month=month, day=day, hour=hour)

    def set_minute(self, minute: int):

        return self.replace(minute=minute)

    def add_minute(self, minute: int):
        minute = self.minute + minute
        year = self.year
        month = self.month
        day = self.day
        hour = self.hour
        while minute >= 60:
            minute -= 60
            hour += 1
            if hour == 24:
                hour = 0
                day += 1
            _max_day = self.days_of_month_by(year, month)
            if day > _max_day:
                day -= _max_day
                month += 1
            if month > 12:
                month -= 12
                year += 1

        return self.replace(year=year, month=month, day=day, hour=hour, minute=minute)

    def sub_minute(self, minute: int):
        year = self.year
        month = self.month
        day = self.day
        hour = self.hour
        current_minute = self.minute
        if minute <= current_minute:
            minute = current_minute - minute
        else:
            minute -= (current_minute + 1)
            hour -= 1
            if hour == 0:
                day -= 1
            if day == 0:
                month -= 1
                if month == 0:
                    month = 12
                    year -= 1
                _max_day = self.days_of_month_by(year, month)
                day = _max_day
        while minute >= 60:
            minute -= 60
            hour -= 1
            if hour == 0:
                day -= 1
            if day == 0:
                month -= 1
                if month == 0:
                    month = 12
                    year -= 1
                _max_day = self.days_of_month_by(year, month)
                day = _max_day
        else:
            minute = 60 - minute

        return self.replace(year=year, month=month, day=day, hour=hour, minute=minute)

    def set_second(self, second: int):

        return self.replace(second=second)

    def add_second(self, second: int):
        second = self.second + second
        year = self.year
        month = self.month
        day = self.day
        hour = self.hour
        minute = self.minute
        while second >= 60:
            second -= 60
            minute += 1
            if minute == 60:
                minute = 0
                hour += 1
            if hour == 24:
                hour = 0
                day += 1
            _max_day = self.days_of_month_by(year, month)
            if day > _max_day:
                day -= _max_day
                month += 1
            if month > 12:
                month -= 12
                year += 1

        return self.replace(year=year, month=month, day=day, hour=hour, minute=minute, second=second)

    def sub_second(self, second: int):
        year = self.year
        month = self.month
        day = self.day
        hour = self.hour
        minute = self.minute
        current_second = self.second
        if second <= current_second:
            second = current_second - second
        else:
            second -= (current_second + 1)
            minute -= 1
            if minute == -1:
                minute = 60 - 1
                hour -= 1
            if hour == 0:
                day -= 1
            if day == 0:
                month -= 1
                if month == 0:
                    month = 12
                    year -= 1
                _max_day = self.days_of_month_by(year, month)
                day = _max_day
        while second >= 60:
            second -= 60
            minute -= 1
            if minute == -1:
                minute = 60 - 1
                hour -= 1
            if hour == 0:
                day -= 1
            if day == 0:
                month -= 1
                if month == 0:
                    month = 12
                    year -= 1
                _max_day = self.days_of_month_by(year, month)
                day = _max_day
        else:
            second = 60 - second

        return self.replace(year=year, month=month, day=day, hour=hour, minute=minute, second=second)

    def days_of_month_by(self, year: int, month: int):
        month_range = monthrange(year, month)
        days = month_range[1]

        return days

    def days_of_month(self):
        days = self.days_of_month_by(self.year, self.month)

        return days

    def start_of_day(self):
        return self.replace(hour=0, minute=0, second=0, microsecond=0)

    def end_of_day(self):
        return self.replace(
            hour=self.HOURS_PER_DAY - 1,
            minute=self.MINUTES_PER_HOUR - 1,
            second=self.SECONDS_PER_MINUTE - 1,
            microsecond=self.MICROSECONDS_PER_SECOND - 1
        )
