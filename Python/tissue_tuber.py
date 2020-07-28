import docx
import datetime
from docx.enum.text import WD_ALIGN_PARAGRAPH
#load in the template document
document = docx.Document("/Users/burkej24/Desktop/tc_labels_tuber.docx")
# configure the default syle: all font is bold, left aligned
style = document.styles["Normal"]
font = style.font.bold=True
form = style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
# get table object from the template
table = document.tables[0]
# recieve the input in a comma separated list and create replicates
atlantic_evol = int(input("Input number of atlantic for tuber evolution: "))
atlantic_nsf = int(input ("Input number of atlantic for nsf: "))
m6 = int(input ("input number of M6: "))
hjt =  int(input("input number of HJT: "))
# get the current date in mm/dd/year format
date = datetime.datetime.now()
date = date.strftime("%x")
# remove all empty elements in the lists

length = atlantic_evol + atlantic_nsf + m6 + hjt
# get the number of full rows
rows = int(length / 4)
# get the number of leftover cells
extra_cells = length % 4
# add the rows and extra cells
for i in range(rows):
    table.add_row()
if extra_cells != 0:
    table.add_row()
#counters
row_num = 0
col_num = 0
# main loops for populating table
for element in range(atlantic_evol):
    if col_num % 2 != 0:
        continue
    elif (col_num / 6 == 1):
        table.cell(row_num, col_num).text = "Atlantic" + "\n" + "JB" + "\t" + date
        row_num += 1
        col_num = 0
    else:
        table.cell(row_num, col_num).text = "Atlantic" + "\n" + "JB" + "\t" + date
        col_num += 2
for element in range(atlantic_nsf):
    if col_num % 2 != 0:
        continue
    elif (col_num / 6 == 1):
        table.cell(row_num, col_num).text = "Atlantic" + "\n" + "JB" + "\t" + date
        row_num += 1
        col_num = 0
    else:
        table.cell(row_num, col_num).text = "Atlantic" + "\n" + "JB" + "\t" + date
        col_num += 2
for element in range(m6):
    if col_num % 2 != 0:
        continue
    elif (col_num / 6 == 1):
        table.cell(row_num, col_num).text = "M6" + "\n" + "JB" + "\t" + date
        row_num += 1
        col_num = 0
    else:
        table.cell(row_num, col_num).text = "M6" + "\n" + "JB" + "\t" + date
        col_num += 2

for element in range(hjt):
    if col_num % 2 != 0:
        continue
    elif (col_num / 6 == 1):
        table.cell(row_num, col_num).text = "HJT 1366" + "\n" + "JB" + "\t" + date
        row_num += 1
        col_num = 0
    else:
        table.cell(row_num, col_num).text = "HJT 1366" + "\n" + "JB" + "\t" + date
        col_num += 2
date = date.replace("/", "_")
document.save("/Users/burkej24/Desktop/" + date + "_tc_tuber.docx")