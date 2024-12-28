from urllib import request
import sys


def fetch_if_needed(day):
    if day < 5:
        return
    try:
        with open(f"../input/day_{day}.txt", "r") as f:
            pass
    except:
        print(f"Fetching day {day}", end="\r")
        url = f"https://adventofcode.com/2024/day/{day}/input"
        with open(f".env", "r") as f:
            cookie = f.read().strip()
        headers = {
            "cookie": "session=" + cookie
        }
        req = request.Request(url, headers=headers)
        with request.urlopen(req) as response:
            data = response.read().decode("utf-8")
            with open(f"../input/day_{day}.txt", "w") as f:
                f.write(data)
        print(f"Fetched day {day}                                   ")


def run_day(day):
    print(f"Running day {day}")
    fetch_if_needed(day)
    match day:
        case num if num < 5:
            print("Not solved in python, try the Haskell solultions")
        case 5:
            from day_5 import solve
            return solve()
        case 6:
            from day_6 import solve
            return solve()
        case 7:
            from day_7 import solve
            return solve()
        case 8:
            from day_8 import solve
            return solve()
        case 9:
            from day_9 import solve
            return solve()
        case 10:
            from day_10 import solve
            return solve()
        case 11:
            from day_11 import solve
            return solve()
        case 12:
            from day_12 import solve
            return solve()


args = sys.argv

day = args[1] if len(args) > 1 else "all"
test = args[2] == "test" if len(args) > 2 else False
clean = args[1] == "clean" if len(args) > 1 else False

if clean:
    import os
    for i in range(5, 26):
        try:
            os.remove(f"../input/day_{i}.txt")
        except:
            pass
elif day == "all":
    for i in range(5, 13):
        run_day(i)
        print()
else:
    day = "".join(filter(str.isdigit, list(day)))
    run_day(int(day))
