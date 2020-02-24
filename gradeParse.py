import numpy as np
import csv


def str_column(matrix, i):
    return [str(row[i]) for row in matrix]

def int_column(matrix, i):
    return [int(row[i]) for row in matrix]

def float_column(matrix, i):
    return [float(row[i]) for row in matrix]





grade_master_file = open('C:\\Users\\CSchulz\\Workspace\\HCI\\gradeMaster.csv', 'r')
# Get labels for the columns
labels = grade_master_file.readline().split(',')
labels[15] = 'Credits'
#print(labels)
# Convert CSV into 2D matrix
grade_master_csv = csv.reader(grade_master_file, delimiter=',')
master = []
for row in grade_master_csv :
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



# Get column totals
unique_year = np.unique(year_col)
wd_total = sum(withdraw_col)
enrollment_total = sum(enrollment_col)
instructor_total = len(np.unique(instructor_col))



# Get sorted list of instructors by class taught
unique_instructor = list(np.unique(instructor_col))
instructor_rank = { i : 0 for i in unique_instructor}
for instructor in instructor_col :
    instructor_rank[instructor] += 1
instructor_rank_sorted = {k: v for k, v in sorted(instructor_rank.items(), key=lambda item: item[1], reverse=True)}



# Grade totals
gpa_total = sum(gpa_col)
a_total = sum(a_col)

b_total = sum(b_col)
c_total = sum(c_col)
d_total = sum(d_col)
f_total = sum(f_col)

a_ratio = a_total / master_rows
b_ratio = b_total / master_rows
c_ratio = c_total / master_rows
d_ratio = d_total / master_rows
f_ratio = f_total / master_rows

a_percent = a_ratio
b_percent = b_ratio
c_percent = c_ratio
d_percent = d_ratio
f_percent = f_ratio



# Withdraw totals
wd_years_index = []
wd_index = 0
for wd in withdraw_col :
    if wd != 0 :
        wd_years_index.append(wd_index)
    wd_index += 1
    
wd_years = []
wd_years_enrollment_total = 0
for index in wd_years_index :
    wd_years.append(year_col[index])
    wd_years_enrollment_total += enrollment_col[index]

wd_totals_by_year = []
for year in unique_year :
    indexes_by_year = []
    index_by_year = 0
    for element in year_col :
        if element == year :
            indexes_by_year.append(index_by_year)
        index_by_year += 1
    year_wd_total = 0
    for i in indexes_by_year :
        year_wd_total += withdraw_col[i]
    wd_totals_by_year.append(year_wd_total)



# Get ratios
gpa_avg = gpa_total / master_rows
wd_ratio = wd_total / enrollment_total
wd_percent = wd_ratio * 100
wd_ratio_2009 = wd_total / wd_years_enrollment_total
wd_percent_2009 = wd_ratio_2009 * 100



# Print information
print("Total enrollment: " + f"{enrollment_total:,d}")
print("Total withdraws: " + f"{wd_total:,d}")
print("Total withdraw percent: " + "%.2f" % wd_percent + "%")
print("Withdraw percent since 2009: " + "%.2f" % wd_percent_2009 + "%")
print("Total GPA Avg.: " + "%.2f" % gpa_avg)
print("Withdraws by year:")
year_string = ''
wd_string = ''
for i in range(len(wd_totals_by_year)) :
    year_string = year_string + "   " + str(unique_year[i])
    if i > 7 :
        wd_string = wd_string + "      " + str(wd_totals_by_year[i])
    else : 
        wd_string = wd_string + "         " + str(wd_totals_by_year[i])
    
print(year_string)
print(wd_string)
print("\nTotal Grade %'s:       A       B       C       D       F")
print("                   %.2f   %.2f   %.2f    %.2f    %.2f" %(a_percent, b_percent, c_percent, d_percent, f_percent))
print("\nTotal unique instructors: " + str(instructor_total))
print("Top instructors by classes taught:")


for element in list(instructor_rank_sorted.items())[:20] :
    print("%12s | %4d" %(element[0], element[1]))


