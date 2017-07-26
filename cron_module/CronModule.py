
class CronModule():
    def __init__(self, user, executable, minute=0, hour=0):
        self.user = user
        self.user = user
        self.executable = executable
        self.minute = minute
        self.hour = hour
        self.DOM = "*"  # day of month
        self.MON = "*"  # Month field
        self.DOW = "*"  # day of week

    @staticmethod
    def check_for_minute(minute):
        if minute > 59:
            raise ValueError("Interval in minutes must not exceed 60!")

    @staticmethod
    def check_for_hour(hour):
        if hour > 24:
            raise ValueError("Interval in hours must not exceed 24!")

    @staticmethod
    def check_for_dow(day_of_week):
        if day_of_week > 7:
            raise ValueError("Interval in week must not exceed 7!")

    @staticmethod
    def check_for_dom(day_of_month):
        if day_of_month > 31:
            raise ValueError("Interval in month must not exceed 31!")

    def add_raw(self, raw_string):
        crontab_string = "{raw_string} {user} {executable}".format(
            raw_string=raw_string,
            user=self.user,
            executable=self.executable
        )
        return crontab_string

    def hourly(self, minute=0):
        self.check_for_minute(minute)
        self.minute = minute
        self.hour = "*"

    def daily(self, minute=0, hour=0):
        self.check_for_minute(minute)
        self.check_for_hour(hour)
        self.minute = minute
        self.hour = hour

    def weekly(self, minute=0, hour=0, day_of_week=1):
        self.check_for_minute(minute)
        self.check_for_hour(hour)
        self.check_for_dow(day_of_week)
        self.minute = minute
        self.hour = hour
        self.DOW = day_of_week

    def monthly(self, minute=0, hour=0, day_of_month=1):
        self.check_for_minute(minute)
        self.check_for_hour(hour)
        self.check_for_dom(day_of_month)
        self.minute = minute
        self.hour = hour
        self.DOM = day_of_month

    def create_cron(self):
        crontab_string = "{minute} {hour} {day_of_month} {month} {day_of_week} {user} {executable}".format(
            minute=self.minute,
            hour=self.hour,
            day_of_month=self.DOM,
            month=self.MON,
            day_of_week=self.DOW,
            user=self.user,
            executable=self.executable
        )
        return crontab_string


if __name__ == "__main__":
    new2 = CronModule(user="tania", executable="python writeDate.py")
    new2.add_raw("* * * * *")

    new3 = CronModule(user="tania", executable="executable.py arg1")
    new3.monthly(day_of_month=24)
    new3.create_cron()