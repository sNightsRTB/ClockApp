#!/usr/bin/env python3
from tkinter import *
from time import strftime, sleep
import calendar, datetime

bgcolour = "#0f0f0f"
fgcolour = "#AA1515"

window = Tk()
window.geometry("600x300")
window.title("Clock App")
window.config(bg = bgcolour)
window.resizable(False, False)

current_date = datetime.datetime.now()
currentyr = current_date.year
month = current_date.month
currentdy = current_date.day
weekdayimp = calendar.weekday(currentyr, month, currentdy)

outputFrame = Frame(window, bg = bgcolour)
outputFrame.place(relx = 0.5, rely = 0.5, anchor = "center")

### 500 if statements cuz I can xD ###
if weekdayimp == 0:
    weekday = "Monday"
    weekdaysh = "Mon"
elif weekdayimp == 1:
    weekday = "Tuesday"
    weekdaysh = "Tue"
elif weekdayimp == 2:
    weekday = "Wednesday"
    weekdaysh = "Wed"
elif weekdayimp == 3:
    weekday = "Thursday"
    weekdaysh = "Thu"
elif weekdayimp == 4:
    weekday = "Friday"
    weekdaysh = "Fri"
elif weekdayimp == 5:
    weekday = "Saturday"
    weekdaysh = "Sat"
else:
    weekday = "Sunday"
    weekdaysh = "Sun"

if month == 1:
    currentmh = "January"
elif month == 2:
    currentmh = "February"
elif month == 3:
    currentmh = "March"
elif month == 4:
    currentmh = "April"
elif month == 5:
    currentmh = "May"
elif month == 6:
    currentmh = "June"
elif month == 7:
    currentmh = "July"
elif month == 8:
    currentmh = "August"
elif month == 9:
    currentmh = "September"
elif month == 10:
    currentmh = "October"
elif month == 11:
    currentmh = "November"
else:
    currentmh = "December"

if currentdy == 22 and month == 6:
    bgcolour = "#DB7093"
else:
    bgcolour = "#0f0f0f"

def updatetime():
    timestr = strftime("%I:%M:%S %p")
    timelbl.config(text = timestr)
    window.after(1000, updatetime)

def updateday():
    datelbl.config(text = f"Date: {currentdy} {currentmh} {currentyr}\n Day: {weekday}")

def update():
    updateday()
    updatetime()

timelbl = Label(outputFrame, font = ("Caskaydia Mono", 60, "bold"), bg = bgcolour, fg = fgcolour)
timelbl.pack(anchor = "center")

datelbl = Label(outputFrame, font = ("Caskaydia Mono", 20, "bold"), bg = bgcolour, fg = fgcolour)
datelbl.pack(anchor = "center")

update()

window.mainloop()
