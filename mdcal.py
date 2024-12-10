"""Markdown Calendar Generator"""

import calendar
from datetime import datetime
import sys

############################################################
START_FROM_SUN = True  # If True, start the week from Sunday
WITH_ISOWEEK = False  # If True, display the week number
ONLY_THIS_MONTH = True  # If True, only display days within the month
ENGLISH = "en"
JAPANESE = "ja"
CHINESE = "cht"
LANG = ENGLISH  # Language of the column names: en, ja, cht
############################################################


def create_calendar(year, month):
    firstweekday = 6 if START_FROM_SUN else 0

    cal = calendar.Calendar(firstweekday=firstweekday)

    mdstr = ""
    dic = get_dict()

    colnames = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    if START_FROM_SUN:
        colnames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    if WITH_ISOWEEK:
        colnames.insert(0, "Week")
    colnames = [dic[col] for col in colnames]

    mdstr += "|" + "|".join(colnames) + "|" + "\n"
    mdstr += "|" + "|".join([":-:" for _ in range(len(colnames))]) + "|" + "\n"

    for days in cal.monthdatescalendar(year, month):
        daystr = []
        for day in days:
            if ONLY_THIS_MONTH and day.month != month:
                daystr.append(" ")
            else:
                daystr.append(str(day.day))

        if WITH_ISOWEEK:
            isoweek = days[0].isocalendar()[1]
            mdstr += (
                "|"
                + str(isoweek)
                + "|"
                + "|".join(daystr)
                + "|"
                + "\n"
            )
        else:
            mdstr += "|" + "|".join(daystr) + "|" + "\n"

    return mdstr


def print_calendar(year, month):
    print("{}/{}\n".format(year, month))
    print(create_calendar(year, month))


def get_dict():
    colnames = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    colnames_ja = ["月", "火", "水", "木", "金", "土", "日"]
    colnames_cht = ["一", "二", "三", "四", "五", "六", "日"]
    if WITH_ISOWEEK:
        colnames.insert(0, "Week")
        colnames_ja.insert(0, "週")
        colnames_cht.insert(0, "週")
    if LANG == "ja":
        dic = dict(zip(colnames, colnames_ja))
    elif LANG == "cht":
        dic = dict(zip(colnames, colnames_cht))
    else:
        dic = {col: col for col in colnames}
    return dic


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) == 1:
        today = datetime.now()
        print_calendar(today.year, today.month)
    elif len(argv) == 2:
        year = int(argv[1])
        for month in range(1, 13):
            print_calendar(year, month)
    elif len(argv) == 3:
        if argv[1].isdigit() and argv[2].isdigit():
            year, month = [int(a) for a in argv[1:3]] 
            if month < 1 or month > 12:
                print("Invalid month. Please enter a valid month.")
            else:
                print_calendar(year, month)
        else:
            print("Usage: python mdcal.py [year] [month]")
    else:
        print("Usage: python mdcal.py [year] [month]")
