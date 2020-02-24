import numpy as np
import csv


def str_column(matrix, i):
    return [row[i] for row in matrix]

def int_column(matrix, i):
    return [int(row[i]) for row in matrix]

def float_column(matrix, i):
    return [float(row[i]) for row in matrix]





grade_master_file = open('C:\\Users\\CSchulz\\Workspace\\HCI\\gradeMaster.csv', 'r')

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
# Data columns created




unique_year = np.unique(year_col)

wd_total = sum(withdraw_col)
enrollment_total = sum(enrollment_col)
instructor_total = len(np.unique(instructor_col))

instructor_top_name = ''
inst_max = 0
unique_instructor = list(np.unique(instructor_col))
instructor_rank = []
for instructor in unique_instructor :
    #print(instructor_col.count(instructor))
    inst_count = instructor_col.count(instructor)
    if  inst_count > inst_max and inst_count != 2218:
        #print(instructor)
        #print(inst_count)
        inst_max = inst_count
        instructor_top_name = instructor
        inst_ins = [instructor_top_name, inst_max]
        instructor_rank.append(inst_ins)

instructor_rank.reverse()
# TODO fix overshadowing problem


# Grade totals
gpa_total = sum(gpa_col)
a_total = sum(a_col)

b_total = sum(b_col)
c_total = sum(c_col)
d_total = sum(d_col)
f_total = sum(f_col)

#grade_sum = a_total + b_total + c_total + d_total + f_total
#print(grade_sum / master_rows)

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

#perc_sum = a_percent + b_percent + c_percent + d_percent + f_percent
#print(perc_sum)

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


#print(unique_year)
#wd_years_unique = np.unique(wd_years)
#print(wd_years_unique)

gpa_avg = gpa_total / master_rows
wd_ratio = wd_total / enrollment_total
wd_percent = wd_ratio * 100
wd_ratio_2009 = wd_total / wd_years_enrollment_total
wd_percent_2009 = wd_ratio_2009 * 100

print("Total enrollment: " + f"{enrollment_total:,d}")
print("Total withdraws: " + f"{wd_total:,d}")
print("Total withdraw percent: " + "%.2f" % wd_percent + "%")
print("Withdraw percent since 2009: " + "%.2f" % wd_percent_2009 + "%")
print("Total GPA Avg.: " + "%.2f" % gpa_avg)
print("Withdraws by year:")
year_string = ''
wd_string = ''
for i in range(len(wd_totals_by_year)) :
    #print("Withdraws in year " + str(unique_year[i] + " : " + str(wd_totals_by_year[i])))
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
print("Amateis     | 2218")
for inst in instructor_rank :
    print("%10s | %4d" %(inst[0], inst[1]))

#print(master[0:3][0])
#print(type(year_col))
