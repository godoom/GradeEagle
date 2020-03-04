import numpy as np
import csv
import plotly.express as px

def str_column(matrix, i):
    return [str(row[i]) for row in matrix]

def int_column(matrix, i):
    return [int(row[i]) for row in matrix]

def float_column(matrix, i):
    return [float(row[i]) for row in matrix]

grade_master_file = open('.\\data\\gradeMasterDateFormatted.csv', 'r')
# Get labels for the columns
labels = grade_master_file.readline().split(',')
labels[15] = 'Credits'
#print(labels)
# Convert CSV into 2D matrix
grade_master_csv = csv.reader(grade_master_file, delimiter=',')
master = []
for row in grade_master_csv :
    master.append(row)

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

unique_years = np.unique(year_col)




def gpa_over_time(course_subject, course_number) :
    course_subject = course_subject.upper()
    course_number_indexes = []
    course_number_index = 0
    master_column = str_column(master, 3)
    for number_row in master_column :
        #print(number_row)
        #print(course_number)
        #print("-")
        if number_row == course_number :
            #print(coursetitle_col[course_number_index])
            course_number_indexes.append(course_number_index)
        course_number_index += 1
    course_indexes = []
    course_subject_index = 0
    #print("Course indexes" + str(course_number_indexes))
    #print(len(course_number_indexes))
    for number_index in course_number_indexes :
        #print(subject_col[number_index])
        #print(course_subject)
        #print("-")
        if subject_col[number_index] == course_subject :
            #print("%s %s" % (subject_col[number_index], coursenum_col[number_index]))
            course_indexes.append(number_index)
        course_subject_index += 1
    year_indexes = []
    #print(course_indexes)
    for year in unique_years :
        specific_year_indexes = []
        for course_index in course_indexes :
            #print(year_col[course_index])
            #print(coursetitle_col[course_index])
            #print(year)
            #print("-")
            if year_col[course_index] == year :
                #print(coursetitle_col[course_index])
                specific_year_indexes.append(course_index)
        year_indexes.append(specific_year_indexes)
    # We now have indexes by year
    #print(year_indexes)
    average_gpa_by_year = []
    num_year = 1
    for column in year_indexes :
        #print("20%02d # classes: %d" %(num_year, len(column)))
        num_year += 1
        year_sum = 0
        for row in column :
            year_sum += gpa_col[row]
            #print(coursetitle_col[row])
        if (len(column) != 0 ) :
            average_gpa_by_year.append(year_sum / len(column)) 
        else :
            average_gpa_by_year.append(0)
    return average_gpa_by_year 
        
    
    











"""
year_indexes = []
formatted_unique_years=[]
# Iterate along all unique years
for year in unique_years :
    formatted_unique_years.append(year[:4])
    year_index = []
    year_row_index = 0
    # For every year in the year column
    for year_row in year_col :
        # If the year row matches our unique year
        if year_row == year :
            # Add the row index to year_index
            year_index.append(year_row_index)
        year_row_index += 1
    # After iterating across all rows
    year_indexes.append(year_index)
# Year indexes now has the indexes for each year
classes_per_year = []
avg_gpa_by_year = []
for year in year_indexes :
    classes_per_year.append(len(year))
    year_gpa_sum = 0
    #print(len(gpa_col))
    for element in year :
        #print(element)
        year_gpa_sum += gpa_col[element]
        #avg_gpa_by_year.append((sum(gpa_col[element] for element in year) / len(year)))
    avg_gpa_by_year.append(year_gpa_sum / len(year))
"""

# print(formatted_unique_years)

        







# Use directly Columns as argument. You can use tab completion for this!
# fig = px.scatter(master, x=year_col, y=gpa_col)
# fig = px.scatter(df, x=df.year, y=df.GPA, color=df.species, size=df.petal_length)



#fig = px.line(master, x=formatted_unique_years, y=classes_per_year)
#fig = px.line(master, x=formatted_unique_years, y=avg_gpa_by_year)


class_gpa = gpa_over_time("cs", "1054")
fig = px.line(master, x=unique_years, y=class_gpa)



fig.update_layout(
    title="Avg. Class GPA per Year",
    xaxis_title="Year",
    yaxis_title="GPA",
    font=dict(
        family="Courier New, monospace",
        size=18,
        #color="#7f7f7f"
        color="black"
    )
)

fig.show()

"""

df = px.data.gapminder().query("continent=='Oceania'")
print(type(df))
print(df)
fig = px.line(df, x="year", y="lifeExp", color='country')
fig.show()
"""