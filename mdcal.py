"""Markdown Calendar Generator"""

import calendar
from datetime import datetime
import sys
import argvChecking as ac

############################################################
START_FROM_SUN = False  # If True, start the week from Sunday
WITH_ISOWEEK = False  # If True, display the week number
ONLY_THIS_MONTH = False  # If True, only display days within the month
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
                "|" + str(isoweek) + "|" + "|".join(daystr) + "|" + "\n" )
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

# year, month, start day, iso week, only this month, lang
if __name__ == "__main__":
    argv = sys.argv
    if len(argv) == 1: 
        today = datetime.now()
        print_calendar(today.year, today.month)
    elif len(argv) == 2:  ## y
        ac.check_argv_2(argv)
    elif len(argv) == 3: ## y, m
        ac.check_argv_3(argv)
    elif len(argv) == 4: ## y, m, sun
        ac.check_argv_4(argv)
    elif len(argv) == 5: ## y, m, sun, iso
        ac.check_argv_5(argv)
    elif len(argv) == 6: ## y, m, sun, iso, only
        ac.check_argv_6(argv)
    elif len(argv) == 7: ## y, m, sun, iso, only, lang
        ac.check_argv_7(argv)
    else:
        print("Usage: python mdcal.py [year] [month]")
