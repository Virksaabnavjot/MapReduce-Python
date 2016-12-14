#!/usr/bin/env python
import sys

# Reducer to return overall top N records
# Data source: https://www.kaggle.com/c/titanic/data
# Data header: "PassengerId" "Survived"	"Pclass" "Name"	"Sex" "Age" "SibSp" "Parch" "Ticket" "Fare" "Cabin" "Embarked"

myList = []
n = 10  # Number of top N records

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split data values into list
    data = line.split(",")

    # convert weight (currently a string) to int
    try:
        age = int(data[6])
    except ValueError:
        # ignore/discard this line
        continue

    # add (age, record) touple to list
    myList.append((age, line))
    # sort list in reverse order
    myList.sort(reverse=True)

    # keep only first N records
    if len(myList) > n:
        myList = myList[:n]

# Print top N records
for (k, v) in myList:
    print(v)