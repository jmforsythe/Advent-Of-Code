import requests
import os
import datetime
import time

CURRENT_TIME = datetime.datetime.utcnow() + datetime.timedelta(hours=-5)
EARLIEST_YEAR = 2015

# Time in seconds to wait between requests to avoid spamming servers
TIME_BETWEEN_REQUESTS = 5

def get_input(year, day):
    res = s.get(f"https://adventofcode.com/{year}/day/{day}/input")
    return res

def get_folders(path="."):
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return dirs

def get_prev_years():
    return [i for i in range(EARLIEST_YEAR, CURRENT_TIME.year)]

def get_whole_year(year):
    if not os.path.isdir(str(year)):
        os.makedirs(str(year))
    for day in range(1, 25+1):
        get_day(year, day)

def get_day(year, day):
    year_day_path = os.path.join(str(year), str(day).zfill(2))
    if not os.path.isdir(year_day_path):
        os.makedirs(year_day_path)

    input_path = os.path.join(year_day_path, "input.txt")
    if os.path.isfile(input_path):
        return

    with open(input_path, "w") as f:
        print(f"Downloading {input_path}")
        time.sleep(5)
        res = get_input(year, day)
        if res.ok:
            f.write(res.content.decode())

if __name__ == "__main__":
    s = requests.session()
    sc_filename = "sessioncookie.txt"

    if not os.path.isfile(sc_filename):
        print(f"Please supply session cookie in {sc_filename}")
        exit()

    with open(sc_filename) as f:
        s.cookies.set("session", f.read())

    for year in get_prev_years():
        get_whole_year(year)

    if CURRENT_TIME.month == 12:
        if not os.path.isdir(str(year)):
            os.makedirs(str(year))
        for day in range(1, min(25, CURRENT_TIME.day)+1):
            get_day(CURRENT_TIME.year, day)
