import numpy as np
import csv
import plotly.express as px
import pandas as pd



data = pd.read_csv('.\\data\\gradeMasterDateFormatted.csv')


sub = "CS"
quer = 'Subject == "' + sub +'" and CourseNo == "3114"'

first = data.query(quer)

fig = px.scatter(first, x="Year", y="GPA", size="Enrollment")

fig.show()

#print(data)
# retrieving row by loc method
#first = data.loc[5][0]
# second = data.loc["2016-17"]
#first = data["Term"]
#first = data.iloc[0]

#print(quer)
#first = data.query('Subject == {sub} and CourseNo == "3114"'.format(**locals()))
#second = data.loc[0]
second = first.query('Year == "2012"')


#print(first)
print(second.iloc[0])

# TODO how to split by year?
# TODO how to make modular /wrt/ input?
# TODO consider shoving everything into fig func?


# iteritems(), iterrows(), itertuples() .

#print(first, "\n\n\n", second)

#for i, j in data.iteritems():
#    print(i, j)
#    print()

#fig = px.line(master, x=formatted_unique_years, y=avg_gpa_by_year)
#fig = px.line(first, x="Year", y="GPA")







