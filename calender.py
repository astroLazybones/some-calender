import time
import requests
import json
import datetime
import colorama

today = datetime.datetime.now()

year = today.year
tech_month = today.month
month = today.strftime("%B")
weekday = today.day

def lenty(x):
    if x < 12:
        lenty = (datetime.date(year, x, 1) - datetime.date(year, x-1, 1)).days
        return lenty
    else:
        lenty = (datetime.date(year, x, 1) - datetime.date(year, 1, 1)).days
        return lenty

mike = []
josh = 0

for i in range(lenty(tech_month)):
    josh = josh + 1
    mike.append(str(josh))

james = 1
frick = ""
cont = 0

#today.strftime("%A")
jacob = today.isoweekday()
frick = "M  T  W  T  F  S  S\n"

if jacob == 1:
    frick = frick
    cont = 0

if jacob == 2:
    frick = frick + (" " * 4)
    cont += 1

if jacob == 3:
    frick =  frick + (" " * 6)
    cont += 2

if jacob == 4:
    frick = frick + (" " * 8)
    cont += 3

if jacob == 5:
    frick = frick + (" " * 10)
    cont += 4

if jacob == 6:
    frick = frick + (" " * 12)
    cont += 5

if jacob == 7:
    frick = frick + (" " * 14)
    cont += 6

for i in range(lenty(tech_month)-1):
    if len(''.join(mike[james])) == 1:
        if james == weekday:
            frick = frick + f"{colorama.Fore.RED}{james}{colorama.Style.RESET_ALL}  "
        else:
            frick = frick + f"{james}  "
    else:
        if james == weekday:
            frick = frick + f"{colorama.Fore.RED}{james}{colorama.Style.RESET_ALL} "
        else:
            frick = frick + f"{james} "

    james = james + 1
    if cont < 6:
        cont = cont + 1
    else:
        cont = 0
        frick = frick + "\n"


print(f"""
        {year}
        {month}

{frick}
""")