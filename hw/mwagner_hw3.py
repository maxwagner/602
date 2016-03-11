# Max Wagner

from Tkinter import Tk
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfile
import csv
import sys
import re


def getfile():
    Tk().withdraw()
    csvfile = askopenfilename()
    return csvfile


def readfile(filename):
    if filename is None or filename == "":
        print "You need to select a file first, exiting"
        sys.exit()
    else:
        _file = open(filename, "rb")
        reader = csv.reader(_file)
        carlist = list(reader)

        for car in carlist:
            if not validate(car):
                print "The car above does not have correct data, exiting"
                sys.exit()
        return carlist


def writefile(carlist):
    f = asksaveasfile(mode="w")
    if f is None or f == "":
        print "Something went wrong."
    writer = csv.writer(f)
    writer.writerows(carlist)


def validate(carlist):
    price = ["vhigh", "high", "med", "low"]
    maint = ["vhigh", "high", "med", "low"]
    doors = ["2", "3", "4", "5more"]
    persons = ["2", "4", "more"]
    lug = ["small", "med", "big"]
    safety = ["high", "med", "low"]
    condition = ["unacc", "acc", "good", "vgood"]
    return carlist[0] in price and carlist[1] in maint and carlist[2] in doors and carlist[3] in persons \
           and carlist[4] in lug and carlist[5] in safety and carlist[6] in condition


def sort(carlist, attribute, order="desc"):
    if attribute == "maint":
        index = 1
    elif attribute == "doors":
        index = 2
    elif attribute == "safety":
        index = 5
    else:
        print "The program only sorts by maint, doors, and safety, exiting"
        sys.exit()

    rating = {"low":1, "med":2, "high":3, "vhigh":4, "1":1, "2":2, "3":3, "4":4, "5more":5}

    if order == "asc":
        return sorted(carlist, key=lambda x: rating[x[index]])
    elif order == "desc":
        return sorted(carlist, key=lambda x: rating[x[index]], reverse=True)
    else:
        print "Order must be asc or desc, exiting."
        sys.exit()


def search_a(carlist):
    cars = []
    pattern = "v?high"
    for car in carlist:
        if re.search(pattern, car[0]) and re.search(pattern, car[1]) and re.search(pattern, car[5]):
            cars.append(car)
    return sort(cars, "doors", "asc")


def search_b(carlist):
    cars = []
    for car in carlist:
        if car[0] == "vhigh" and car[1] == "med" and car[2] == "4" and car[3] in ("4", "more"):
            cars.append(car)
    return cars


if __name__ == "__main__":
    filename = getfile()
    carlist = readfile(filename)
    print sort(carlist, "safety", "desc")[:10] # 2a
    print "\n"
    print sort(carlist, "maint", "asc")[-15:] # 2b
    print "\n"
    print search_a(carlist) # 2c
    writefile(search_b(carlist)) #2d