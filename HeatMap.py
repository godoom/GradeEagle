import csv
import pandas as pd
from operator import truediv
import plotly


def str_column(matrix, i):
    return [str(row[i]) for row in matrix]


def int_column(matrix, i):
    return [int(row[i]) for row in matrix]


def float_column(matrix, i):
    return [float(row[i]) for row in matrix]

grade_master_file = open('/Users/user/Documents/4784/HeatMapMKTG.csv', 'r')
# Get labels for the columns
labels = grade_master_file.readline().split(',')
labels[15] = 'Credits'
# print(labels)
# Convert CSV into 2D matrix
grade_master_csv = csv.reader(grade_master_file, delimiter=',')
master = []
for row in grade_master_csv:
    master.append(row)
master_rows = len(master)
# Conversion finished
# Create data columns
year_col = str_column(master, 0)
term_col = str_column(master, 1)
subject_col = str_column(master, 2)
coursenum_col = str_column(master, 3)
coursetitle_col = str_column(master, 4)
instructor_col = str_column(master, 5)
gpa_col = float_column(master, 6)
a_col = float_column(master, 7)
b_col = float_column(master, 8)
c_col = float_column(master, 9)
d_col = float_column(master, 10)
f_col = float_column(master, 11)
withdraw_col = int_column(master, 12)
enrollment_col = int_column(master, 13)
crn_col = str_column(master, 14)
credits_col = int_column(master, 15)

n = len(coursenum_col)

Dictionary = {}
returnList = []

for i in range(n):
    key = coursenum_col[i]
    value = gpa_col[i]
    Dictionary[key] = value
    returnList.append([key, value])

listSorted = sorted(returnList)

# print(listSorted)
courseNumList = []

# for pairs in listSorted:
#     print(pairs)

freqList = {x:coursenum_col.count(x) for x in coursenum_col}
freqListSorted = []
# print("D = ", freqList)
for key in sorted(freqList):
    freqListSorted.append(freqList[key])
    # print ("%s: %s" % (key, freqList[key]))

print("Frequencies = ", freqListSorted)
print("length =", len(freqListSorted))
totals = {}
keyNums = []
for key, value in listSorted:
    totals[key] = totals.get(key, 0) + value

print("Totals = ", (list(totals.values())))
print("length =", len(list(totals.values())))
print("CourseNums = ", (list(totals.keys())))
#print(totals)

Avgs = list(map(truediv, list(totals.values()), freqListSorted))
print("avgs = ", Avgs)

courseAndAvgGPA = {k: v for k, v in zip(list(totals.keys()), Avgs)}
print("CourseNumAndGPA = ", courseAndAvgGPA)
y = []

import plotly.graph_objects as go

for i in range(0, len(courseNumList)):
    test_list[i] = int(courseNumList[i])

results = list(map(int, courseNumList))
# print(gpa_col)

# fig = go.Figure(data=go.Heatmap(
#         z=a_col,
#         x=coursenum_col,
#         y=gpa_col,
#         colorscale=[(0, "blue"), (1, "red")]))
#
# fig.update_layout(
#     title='Class Avgs',
#     xaxis_nticks=33)
#
# fig.show()

fig = go.Figure()

fig.add_trace(go.Bar(
    x=courseNumList,
    y=Avgs
))

my_new_list = [i ** 1.1 for i in freqListSorted]

fig = go.Figure(data=[go.Scatter(
    x=list(totals.keys()), y=Avgs,
    mode="markers",
    marker=dict(
        color=Avgs,
        colorscale='rdylgn',
        size=25,#freqListSorted,
    )
)])
fig.update_layout(title='College of Business: MKTG')
fig.show()

fig = go.Figure(go.Bar(
            x=list(totals.keys()),
            y=Avgs,
            width=150,
            orientation='v'))

fig.show()




# ['aggrnyl', 'agsunset', 'algae', 'amp', 'armyrose', 'balance',
#              'blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 'brbg',
#              'brwnyl', 'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'curl',
#              'darkmint', 'deep', 'delta', 'dense', 'earth', 'edge', 'electric',
#              'emrld', 'fall', 'geyser', 'gnbu', 'gray', 'greens', 'greys',
#              'haline', 'hot', 'hsv', 'ice', 'icefire', 'inferno', 'jet',
#              'magenta', 'magma', 'matter', 'mint', 'mrybm', 'mygbm', 'oranges',
#              'orrd', 'oryel', 'peach', 'phase', 'picnic', 'pinkyl', 'piyg',
#              'plasma', 'plotly3', 'portland', 'prgn', 'pubu', 'pubugn', 'puor',
#              'purd', 'purp', 'purples', 'purpor', 'rainbow', 'rdbu', 'rdgy',
#              'rdpu', 'rdylbu', 'rdylgn', 'redor', 'reds', 'solar', 'spectral',
#              'speed', 'sunset', 'sunsetdark', 'teal', 'tealgrn', 'tealrose',
#              'tempo', 'temps', 'thermal', 'tropic', 'turbid', 'twilight',
#              'viridis', 'ylgn', 'ylgnbu', 'ylorbr', 'ylorrd'].