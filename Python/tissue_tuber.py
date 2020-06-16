import docx
import datetime
from docx.enum.text import WD_ALIGN_PARAGRAPH
#load in the template document
document = docx.Document("/Users/burkej24/Desktop/tc_labels.docx")
# configure the default syle: all font is bold, left aligned
style = document.styles["Normal"]
font = style.font.bold=True
form = style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
# get table object from the template
table = document.tables[0]
# recieve the input in a comma separated list and create replicates
atlantic_evol = input("Input number of atlantic for tuber evolution: ").split(",")
atlantic_nsf = input ("Input number of atlantic for nsf ").split(",")
m6 = input ("input all M6 ").split(",")
hjt =  input("input all HJT")
# get the current date in mm/dd/year format
date = datetime.datetime.now()
date = date.strftime("%x")
# remove all empty elements in the lists
s = [i for i in s if i]
gwh = [i for i in gwh if i]
other = [i for i in other if i]
# sort them
s.sort()
gwh.sort()
other.sort()
# get the length
length = len(s) + len(gwh) + len(other)
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
for element in s:
    if col_num % 2 != 0:
        continue
    elif (col_num / 6 == 1):
        table.cell(row_num, col_num).text = "SUP19xM6" + "\t" + "# " + element + "\n" + "S" + "\t" + date
        row_num += 1
        col_num = 0
    else:
        table.cell(row_num, col_num).text = "SUP19xM6" + "\t" + "# " + element + "\n" + "S" + "\t" +  date
        col_num += 2
for element in gwh:
    if col_num % 2 != 0:
        continue
    elif (col_num / 6 == 1):
        table.cell(row_num, col_num).text = "SUP19xM6" + "\t" + "# " + element + "\n" + "GMH" + "\t" + date
        row_num += 1
        col_num = 0
    else:
        table.cell(row_num, col_num).text = "SUP19xM6" + "\t" + "# " + element + "\n" + "GMH" + "\t" + date
        col_num += 2
form = style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
for element in other:
    if col_num % 2 != 0:
        continue
    elif (col_num / 6 == 1):
        table.cell(row_num, col_num).text = element + "\t" + "\n" + date + "\t"
        row_num += 1
        col_num = 0
    else:
        table.cell(row_num, col_num).text = element + "\t" + "\n" + date + "\t"
        col_num += 2
date = date.replace("/", "_")
document.save("/Users/burkej24/Desktop/" + date + "_tc.docx")