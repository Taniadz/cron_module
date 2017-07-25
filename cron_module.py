
class Cron():

    def __init__(self, user, executable, minute=0, hour=0):
        self.user = user
        self.user = user
        self.executable = executable
        self.minute = minute
        self.hour = hour
        self.DOM = "*"  # day of month
        self.MON = "*"  # Month field
        self.DOW = "*"  # day of week

    def add_raw(self, raw_string):
        crontab_string = "{raw_string} {user} {executable}".format(
            raw_string=raw_string,
            user=self.user,
            executable=self.executable
        )
        return crontab_string

    def hourly(self, minute=0):
        self.minute = minute
        if self.minute > 59:
            raise ValueError("Interval in minutes must not exceed 60!")
        self.hour = "*"

    def daily(self, minute=0, hour=0):
        self.minute = minute
        if self.minute > 59:
            raise ValueError("Interval in minutes must not exceed 60!")
        self.hour = hour
        if self.hour > 24:
            raise ValueError("Interval in hours must not exceed 24!")

    def weekly(self, minute=0, hour=0, day_of_week = 1):
        self.minute = minute
        if self.minute > 59:
            raise ValueError("Interval in minutes must not exceed 60!")
        self.hour = hour
        if self.hour > 24:
            raise ValueError("Interval in hours must not exceed 24!")
        self.DOW = day_of_week
        if self.DOW > 7:
            raise ValueError("Interval in week must not exceed 7!")

    def monthly(self, minute=0, hour=0, day_of_month=1):
        self.minute = minute
        if self.minute > 59:
            raise ValueError("Interval in minutes must not exceed 60!")
        self.hour = hour
        if self.hour > 24:
            raise ValueError("Interval in hours must not exceed 24!")
        self.DOM = day_of_month
        if self.DOM > 31:
            raise ValueError("Interval in month must not exceed 31!")

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
    new1 = Cron(user="tania", executable="executable.py")
    new1.monthly(minute=30, hour=3, day_of_month=3)
    new1.create_cron()


    new2 = Cron(user="tania", executable="python writeDate.py")
    new2.add_raw("* * * * *")

    new3 = Cron(user="tania", executable="executable.py arg1")
    new3.hourly()
    new3.create_cron()