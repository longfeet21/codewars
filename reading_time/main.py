'''
4 kyu

Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
'''

# * For seconds = 62, your function should return
#     "1 minute and 2 seconds"
# * For seconds = 3662, your function should return
#     "1 hour, 1 minute and 2 seconds"

minute = 60
hour = minute * 60
day = hour * 24
year = day * 365


def format_duration(seconds):
    ryear, res = check_year(seconds)
    rday, res = check_day(seconds)
    rhour, res = check_hour(seconds)
    rminute, res = check_minute(seconds)
    result = ""
    if ryear:
        result += ", %s %s" % (ryear, check_plural(ryear, "year"))
    if rday:
        result += ", %s %s" % (rday, check_plural(rday, "day"))
    if rhour:
        result += ", %s %s" % (rhour, check_plural(rhour, "hour"))
    if rminute:
        result += ", %s %s" % (
            rminute, check_plural(rminute, "minute"))
    if res:
        result += ", %s %s" % (res, check_plural(res, "second"))

    if result.startswith(","):
        result = result[2:]
        result = " and ".join(result.rsplit(", ", 1))
    else:
        result = "now"
    return result


def check_plural(time, stamp):
    if time > 1:
        return stamp+"s"
    return stamp


def check_year(seconds):
    a = int(seconds/year)
    b = seconds % year
    return (a, b)


def check_day(seconds):
    a = int(seconds % year / day)
    b = seconds % day
    return (a, b)


def check_hour(seconds):
    a = int(seconds % day / hour)
    b = seconds % hour
    return (a, b)


def check_minute(seconds):
    a = int(seconds % hour / minute)
    b = seconds % minute
    return (a, b)


print(format_duration((year*4)+(68*day)+(3*hour)+(4*minute)))
print(format_duration((107*day)+(16*hour)+50))
print(format_duration((14*day)+(17*hour)+(41*minute)))
print(format_duration(day+123))
print(format_duration(minute+123))
