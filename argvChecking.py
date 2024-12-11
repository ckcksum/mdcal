import mdcal

USAGE = "Usage: python mdcal.py [year] [month]<Start with Sunday><Display week number><Only this month><language>"
INVALID = "Invalid argument."

"""
Sanity check for the arguments
"""
# Helper methods
def check_start_from_sun(argv):
    if argv.lower() in ["true", "t", "1", "sun", "sunday", "s", "yes", "y"]:
        mdcal.START_FROM_SUN = True
        return True
    elif argv.lower() in ["false",  "f", "0", "mon", "monday", "m", "no", "n"]:
        mdcal.START_FROM_SUN = False
        return True
    else:
        return False

def check_true_false(argv):
    if argv.lower() in ["true", "t", "1", "yes", "y"]:
        return True
    elif argv.lower() in ["false",  "f", "0", "no", "n"]:
        return False
    else:
        return None
    
def check_language(argv):
    if argv.lower() in ["en", "english", "eng", "e"]:
        mdcal.LANG = mdcal.ENGLISH
    elif argv.lower() in ["ja", "japanese", "jp", "j"]:
        mdcal.LANG = mdcal.JAPANESE
    elif argv.lower() in ["cht", "chinese", "cn", "c", "zh", "ch"]:
        mdcal.LANG = mdcal.CHINESE
    else:
        return False
    return True


# ############################################# #
# argv2 = y 
def check_argv_2(argv):
    if argv[1].isdigit():
        year = int(argv[1])
        if year < 2:
            print(INVALID)
        else: 
            for month in range(1, 13):
                mdcal.print_calendar(year, month)
    else:
        print(USAGE)

# argv3 = y, m
def check_argv_3(argv):
    if argv[1].isdigit() and argv[2].isdigit():
        year, month = [int(a) for a in argv[1:3]] 
        if month < 1 or month > 12 or year < 2:
            print(INVALID+USAGE)
        else: 
            mdcal.print_calendar(year, month)
    else:
        print(USAGE)


# argv4 = y, m, sun
def check_argv_4(argv):
    if argv[1].isdigit() and argv[2].isdigit():
        year, month = [int(a) for a in argv[1:3]] 
        if month < 1 or month > 12 or year < 2:
            print(INVALID+USAGE)
        else: 
            if check_start_from_sun(argv[3]):
                mdcal.print_calendar(year, month)
            else:
                print(INVALID+USAGE)
    else:
        print(USAGE)



# argv5 = y, m, sun, iso
def check_argv_5(argv):
    if argv[1].isdigit() and argv[2].isdigit():
        year, month = [int(a) for a in argv[1:3]] 
        if month < 1 or month > 12 or year < 2:
            print(INVALID+USAGE)
        else: 
            if check_start_from_sun(argv[3]) and check_true_false(argv[4]) != None:
                mdcal.WITH_ISOWEEK = check_true_false(argv[4])
                mdcal.print_calendar(year, month)
            else:
                print(INVALID+USAGE)
    else:
        print(USAGE)



# argv6 = y, m, sun, iso, only
def check_argv_6(argv):
    if argv[1].isdigit() and argv[2].isdigit():
        year, month = [int(a) for a in argv[1:3]] 
        if month < 1 or month > 12 or year < 2:
            print(INVALID+USAGE)
        else: 
            if check_start_from_sun(argv[3]) and check_true_false(argv[4]) != None and check_true_false(argv[5]) != None:
                mdcal.WITH_ISOWEEK = check_true_false(argv[4])
                mdcal.ONLY_THIS_MONTH = check_true_false(argv[5])
                mdcal.print_calendar(year, month)
            else:
                print(INVALID+USAGE)
    else:
        print(USAGE)


# argv7 = y, m, sun, iso, only, lang
def check_argv_7(argv):
    if argv[1].isdigit() and argv[2].isdigit():
        year, month = [int(a) for a in argv[1:3]] 
        if month < 1 or month > 12 or year < 2:
            print(INVALID+USAGE)
        else: 
            if check_start_from_sun(argv[3]) and check_true_false(argv[4]) != None and check_true_false(argv[5]) != None and check_language(argv[6]):
                mdcal.WITH_ISOWEEK = check_true_false(argv[4])
                mdcal.ONLY_THIS_MONTH = check_true_false(argv[5])
                mdcal.print_calendar(year, month)
            else:
                print(INVALID+USAGE)
    else:
        print(USAGE)
