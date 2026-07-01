# Link: https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true
import calendar

if __name__ == "__main__":
    m, d, y = map(int, input().split(" "))

    day = calendar.weekday(y, m, d)
    print(calendar.day_name[day].upper())
