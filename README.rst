This is simple cron module for python.

Creating a new job, the user should specify the executable, the list of arguments,
the account to run it as.

Module has method for creating hourly, daily, weekly and monthly jobs.
The arguments(minute, hour, day of week, day of month) are optional.
Threre is a generic add job method that takes raw cron string in module.
