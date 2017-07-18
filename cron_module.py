
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


    def add_raw(self, raw_string, config):
        crontab_string = "{raw_string} {user} {executable}".format(
            raw_string=raw_string,
            user=self.user,
            executable=self.executable
        )
        with open(config, "a") as output_config:
            output_config.write(crontab_string + '\n')

    def hourly(self, minute=0):
        self.minute = minute
        self.hour = "*"

    def daily(self, minute=0, hour=0):
        self.minute = minute
        self.hour = hour

    def weekly(self, minute=0, hour=0, day_of_week = 1):
        self.minute = minute
        self.hour = hour
        self.DOW = day_of_week

    def monthly(self, minute=0, hour=0, day_of_month=1):
        self.minute = minute
        self.hour = hour
        self.DOM = day_of_month

    def create_cron(self, config):
        if self.minute > 59:
            raise ValueError("Interval in minutes must not exceed 60!")
        if self.hour != "*" and self.hour > 24:
            raise ValueError("Interval in hours must not exceed 24!")

        if self.DOM != "*" and self.DOM > 31:
            raise ValueError("Interval in month must not exceed 31!")

        if self.DOW != "*" and self.DOW > 7:
            raise ValueError("Interval in week must not exceed 7!")
        crontab_string = "{minute} {hour} {day_of_month} {month} {day_of_week} {user} {executable}".format(
            minute=self.minute,
            hour=self.hour,
            day_of_month=self.DOM,
            month=self.MON,
            day_of_week=self.DOW,
            user=self.user,
            executable=self.executable
        )
        with open(config, "a") as output_config:
            output_config.write(crontab_string + '\n')
        return crontab_string


if __name__ == "__main__":
    new1 = Cron(user="tania", executable="executable.py")
    new1.monthly(minute=30, hour=3, day_of_month=3)
    new1.create_cron("config.py")


    new2 = Cron(user="tania", executable="python writeDate.py")
    new2.add_raw("* * * * *", config="config.py")

    new3 = Cron(user="tania", executable="executable.py arg1")
    new3.weekly()
    new3.create_cron("config.py")