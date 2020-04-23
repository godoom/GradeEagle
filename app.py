# coding: utf-8
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly
import plotly.express as px
import pandas as pd

import plotly.graph_objects as go
import numpy as np
from operator import truediv
import csv

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data = pd.read_csv('gradeMaster.csv')
grade_master_file = open('gradeMaster.csv', 'r')


def str_column(matrix, i):
    return [str(row[i]) for row in matrix]


def int_column(matrix, i):
    return [int(row[i]) for row in matrix]


def float_column(matrix, i):
    return [float(row[i]) for row in matrix]


# Get labels for the columns
labels = grade_master_file.readline().split(',')
labels[15] = 'Credits'

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

courseNameandNum = []
courseListFinal = []
gpa_list = []

n = len(coursenum_col)

Dictionary = {}
returnList = []

for i in range(n):
    courseNameandNum.append(subject_col[i] + "-" + coursenum_col[i])
    gpa_list.append(gpa_col[i])

    key = courseNameandNum[i]
    value = gpa_list[i]
    Dictionary[key] = value
    returnList.append([key, value])


for elem in courseNameandNum:
    if elem not in courseListFinal:
        courseListFinal.append(elem)

sorted(courseListFinal)

listSorted = sorted(returnList)
courseNumList = []


freqList = gpa_list
# freqList = {x:coursenum_col.count(x) for x in coursenum_col}

freqListSorted = []

totals = []
keyNums = []


courseAndAvgGPA = list(zip(courseNameandNum, gpa_list))


def to_key(listA, listB):
    d = {}
    for a, b in zip(listA, listB):
        d.setdefault(a, []).append(b)
    avg = []
    for keys in d:
        avg.append(sum(d[keys])/len(d[keys]))

    return list(d.keys())


def gpa_avg(listA, listB):
    d = {}
    for a, b in zip(listA, listB):
        d.setdefault(a, []).append(b)
    avg = []
    for keys in d:
        avg.append(sum(d[keys])/len(d[keys]))

    return avg


courseAvgs = gpa_avg(courseNameandNum, gpa_list)
courseListFinal = to_key(courseNameandNum, gpa_list)

courseNamesAndAvgs = list(zip(courseListFinal, courseAvgs))

y = []
test_list = []

for i in range(0, len(courseNumList)):
    test_list[i] = int(courseNumList[i])

results = list(map(int, courseNumList))

# # bubble chart plot
fig2 = go.Figure(data=[go.Scatter(
    x=courseListFinal, y=courseAvgs,
    mode="markers",
    marker=dict(
        color=courseAvgs,
        colorscale='rdylgn',
        size=20
    )
)])

fig2.update_layout(title='Fall 2018 Semester Averages')


# # Violin plot
fig3 = go.Figure(data=go.Violin(y=courseAvgs, box_visible=True, line_color='black',
                                meanline_visible=True, fillcolor='indigo', opacity=0.6,
                                x0='Virginia Tech Grade Distributions Spread'))


fig3.update_layout(yaxis_zeroline=False)


# # Get user input values for query
# sub = input("What subject would you like to check: ")

# course = input("What course would you like to check: ")

# # have to enter year as XXXX-XX, ie 2018-19, because it covers fall into spring
# year = input("What year (enter as 20xx-xx): ")

# # we can narrow down the query by term if we want, too.
# term = input("Which term (Spring, Summer, Fall, Winter): ")

sub = "CS"
course = "1114"
year = "2018-19"
term = "Spring"

# query
quer2 = 'Subject == "' + sub + '" and CourseNo == "' + course + '"'

# splits data by session
first1 = data.query(quer2)
first1['Session'] = first1["Year"].astype(str) + ' ' + first1["Term"]

fig4 = px.scatter(first1.sort_values(by=['Session']), x="Session", y="GPA",
                  size="Enrollment", color="Withdraws", hover_name="Instructor", width=1800, height=800)


# query the csv
if year == "" and term == "":
    quer = 'Subject == "' + sub + '" and CourseNo =="' + course + '"'

if year != "" and term == "":
    quer = 'Subject == "' + sub + '" and CourseNo =="' + course + \
        '" and Year == "' + year + '"'  # + 'and Term == "' + term + '"'

if year != "" and term != "":
    quer = 'Subject == "' + sub + '" and CourseNo =="' + course + \
        '" and Year == "' + year + '"' + 'and Term == "' + term + '"'

first = data.query(quer)

# Make array holding instructor names based on query results
instructors = ["" for x in range(len(first.values))]
for x in range(0, len(first.values), 1):
    instructors[x] = first.values[x][5]

# fill in A, B, C, D, F, and withdraw spread
aDist = np.empty(len(first.values), dtype=int)
bDist = np.empty(len(first.values), dtype=int)
cDist = np.empty(len(first.values), dtype=int)
dDist = np.empty(len(first.values), dtype=int)
fDist = np.empty(len(first.values), dtype=int)
wdDist = np.empty(len(first.values), dtype=int)

for x in range(0, len(first.values), 1):
    aDist[x] = first.values[x][7]

for x in range(0, len(first.values), 1):
    bDist[x] = first.values[x][8]

for x in range(0, len(first.values), 1):
    cDist[x] = first.values[x][9]

for x in range(0, len(first.values), 1):
    dDist[x] = first.values[x][10]

for x in range(0, len(first.values), 1):
    fDist[x] = first.values[x][11]

for x in range(0, len(first.values), 1):
    wdDist[x] = first.values[x][12]

# selected_value = dropdown_properties['value']

# make the graph and add bars for every instructor
fig = go.Figure(go.Bar(x=instructors, y=wdDist,
                       name='Withdraw', marker_color='#A0A0A0'))
fig.add_trace(go.Bar(x=instructors, y=fDist,
                     name='F', marker_color='#DA3636'))
fig.add_trace(go.Bar(x=instructors, y=dDist,
                     name='D', marker_color='#F3C871'))
fig.add_trace(go.Bar(x=instructors, y=cDist,
                     name='C', marker_color='#D9F371'))
fig.add_trace(go.Bar(x=instructors, y=bDist, name='B',
                     marker_color='#71F37A'))  # 3376CD
fig.add_trace(go.Bar(x=instructors, y=aDist, name='A',
                     marker_color='#71A5F3'))  # 41C74F

# formatting the graph and rest of the page.
figTitle = 'Grade Distribution for ' + sub + \
    ' ' + course + ' for the school year ' + year
fig.update_layout(title=figTitle, xaxis=dict(
    title='Instructors'), yaxis=dict(title='Enrollment'), barmode='stack')


app.layout = html.Div(children=[
    html.H3('Grade Eagle'),


    dcc.Dropdown(
        id='visualizations_dropdown',
        options=[
            {'label': 'See grade distribution breakdown for course',
                'value': 'BAR'},
            {'label': 'See semester averages (broken)', 'value': 'BUBBLE'},
            {'label': 'See grade distributions spread (broken)',
             'value': 'VIOLIN'},
            {'label': 'See GPA Over Time for Course', 'value': 'SCATTER'},
            {'label': 'test', 'value': 'LINE'}

        ],
        value='BAR'
    ),

    dcc.Graph(
        id='showing_graph'
    )
])


@app.callback(
    Output('showing_graph', 'figure'),
    [Input('visualizations_dropdown', 'value')]
)
def update_output_div(dropdown_properties):
    if dropdown_properties == 'BAR':
        return fig
    if dropdown_properties == 'BUBBLE':
        return fig2
    if dropdown_properties == 'VIOLIN':
        return fig3
    if dropdown_properties == 'SCATTER':
        return fig4


if __name__ == '__main__':
    app.run_server(debug=True)
