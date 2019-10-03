    lines += line.strip()

print (lines)
runfile('C:/Users/joema/.spyder-py3/untitled0.py', wdir='C:/Users/joema/.spyder-py3')
runfile('C:/Users/joema/.spyder-py3/lab05.py', wdir='C:/Users/joema/.spyder-py3')
line
runfile('C:/Users/joema/.spyder-py3/lab05.py', wdir='C:/Users/joema/.spyder-py3')
ch
ch[12:18]
runfile('C:/Users/joema/.spyder-py3/lab05.py', wdir='C:/Users/joema/.spyder-py3')
ch[12:17]
runfile('C:/Users/joema/.spyder-py3/lab05.py', wdir='C:/Users/joema/.spyder-py3')
i
runfile('C:/Users/joema/.spyder-py3/lab05.py', wdir='C:/Users/joema/.spyder-py3')
i
ch
ch[12:16]
runfile('C:/Users/joema/.spyder-py3/lab05.py', wdir='C:/Users/joema/.spyder-py3')
d = 1.30
d = "1.30"
float (d)
ch[12:16]
float (ch[12:16])
h
ch
runfile('C:/Users/joema/.spyder-py3/lab05.py', wdir='C:/Users/joema/.spyder-py3')
ch
ch[12:16]
ch[20:25]
ch[25:30]
ch[25:29]
ch[:4]
ch[:6]
runfile('C:/Users/joema/.spyder-py3/lab05.py', wdir='C:/Users/joema/.spyder-py3')
names
name1 = names + "average" + "Max"
name1
name1 = names + "average" + "" + "Max"
name1
name2 = names + "average" + "" + "Max"
name2
name2 = names + "average" + " " + "Max"
name
name2
i
runfile('C:/Users/joema/.spyder-py3/lab05.py', wdir='C:/Users/joema/.spyder-py3')
i
runfile('C:/Users/joema/.spyder-py3/lab05.py', wdir='C:/Users/joema/.spyder-py3')

## ---(Wed Oct  2 17:08:51 2019)---
runfile('C:/Users/joema/.spyder-py3/lab05.py', wdir='C:/Users/joema/.spyder-py3')
ch
ch[25:29]
ch[24:29]
runfile('C:/Users/joema/.spyder-py3/lab05.py', wdir='C:/Users/joema/.spyder-py3')
i
runfile('C:/Users/joema/.spyder-py3/lab05.py', wdir='C:/Users/joema/.spyder-py3')
runfile('C:/Users/joema/.spyder-py3/untitled1.py', wdir='C:/Users/joema/.spyder-py3')
data_o = open("data.txt", "r")
x = 0
y = 0
minimum = 10e10
maximum= 0
BM = 0
print ("{:<12s}{:<12s}{:<12s}{:<12s}".format("Name", "Height (m)", "Weight(kg)", "BMI")) 
for i,ch in enumerate (data_o):
    if i == 0 :
        continue
    else:
        names = ch[:6]
        height = float (ch[12:16])
        x += height
        if height < minimum:
            minimum_h = height
        if height > maximum :
            maximum_h = height
        weight = float (ch[24:29])
        y += weight
        if weight < minimum:
            minimum_w = weight
        if weight > maximum:
            maximum_w = weight
        BMI = weight / height ** 2
        BM += BMI
        if BMI < minimum:
            minb = BMI
        if BMI > maximum:
            maxb = BMI
        print ("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(names, height, weight, BMI))       
        if i == 8:
            avgbmi = BM / i
            avg_weight = y / i       
            avg_height = x/i
            print ("\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Average", avg_height, avg_weight, avgbmi))
            print ("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Max", maximum_h, maximum_w, maxb))
            print ("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Min", minimum_h, minimum_w, minb))

data_o.close()
runfile('C:/Users/joema/.spyder-py3/untitled1.py', wdir='C:/Users/joema/.spyder-py3')
runfile('C:/Users/joema/.spyder-py3/lab05.py', wdir='C:/Users/joema/.spyder-py3')
runfile('C:/Users/joema/.spyder-py3/untitled1.py', wdir='C:/Users/joema/.spyder-py3')

## ---(Thu Oct  3 10:36:30 2019)---
runfile('C:/Users/joema/.spyder-py3/lab05a.py', wdir='C:/Users/joema/.spyder-py3')
miminum
maximum
minimum
BMI
?
%clear
runfile('C:/Users/joema/.spyder-py3/lab05a.py', wdir='C:/Users/joema/.spyder-py3')
runfile('C:/Users/joema/.spyder-py3/lab05b.py', wdir='C:/Users/joema/.spyder-py3')