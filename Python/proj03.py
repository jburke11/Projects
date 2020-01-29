# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# project 03
# ask for input on residency, year , college, major , and credits
# use this information to go through if statements with each possible outcome of input
# print the calculated tuition
# ask the user if they want to make another calculation
#
#
#
#
print ("2019 MSU Undergraduate Tuition Calculator.")
while True :
    resident1 = input ("\nResident (yes/no): ")                         # input on residency
    if resident1.lower() != "yes" :
        resident = "no"
    else: 
        resident = "yes"
    if resident == "no" :
       resident2 = input ("International (yes/no): ")
    level1 = input ("Level—freshman, sophomore, junior, senior: ")
    while level1.lower() not in ["freshman" , "sophomore" , "junior" , "senior"] :           # input on year
        print ("Invalid input. Try again.")
        level1 = input ("Level—freshman, sophomore, junior, senior: ")
    else :
        level = level1.lower()
        if level == "junior" or level == "senior" :                                                         # information bracket for juniors and seniors
            college = input ("Enter college as business, engineering, health, sciences, or none: ")
            cmse = input ("Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ")
            if college == "engineering" :
                engineering = "yes"
            else :
                engineering = "no"
            if cmse != "yes" :
                 cmse = "no"
            madison = None
            if college !=  "business"  and college != "engineering" and college != "health" and college != "sciences" and college != "none" :
                madison = input ("Are you in the James Madison College (yes/no): ")
            else :
                madison = "no"
            if madison != "yes":
                madison = "no"
        elif level == "freshman" or level == "sophomore" :                  # information bracket for freshman and sophomores
            engineering = input ("Are you admitted to the College of Engineering (yes/no): ")
            if engineering != "yes":
                engineering = "no"
            if engineering == "yes" :
                madison = "no"
            if engineering != "yes" :
                madison = input ("Are you in the James Madison College (yes/no): ")
                if madison != "yes":
                    madison = "no"
            college = None
            cmse = "no"
        elif college == "none" :
            madison = input ("Are you in the James Madison College (yes/no): ")
            if madison != "yes":
                madison = "no"
    while True:
        credit1 = input ("Credits: ")                   # credit input
        if "." in credit1:
            print ("Invalid input. Try again.")
            continue
        elif not credit1.isdigit():
            print ("Invalid input. Try again.")
            continue
        elif int (credit1) <= 0 :
            print ("Invalid input. Try again.")
            continue
        else:
            credit = int (credit1)
            break
    if resident == "yes" and level == "freshman" and engineering == "no" and madison == "no" and credit < 6  :      # if else statements for resident buisiness health sciences freshman/sophomore
        tuition = 482 * credit + 21 + 3 
    elif resident == "yes" and level == "freshman" and engineering == "no" and madison == "no" and 6 <= credit <= 11 :
        tuition = 482 * credit + 21 + 3 + 5
    elif resident == "yes" and level == "freshman" and engineering == "no" and madison == "no" and 12 <= credit < 18 :
        tuition = 7230 + 21 + 3 + 5
    elif resident == "yes" and level == "freshman" and engineering == "no" and madison == "no" and 18 <= credit :
        tuition = 7230 + 21 + 3 + 5 + 482 * (credit - 18)
    elif resident == "yes" and level == "sophomore" and engineering == "no" and madison == "no" and credit < 6:
        tuition = 494 * credit + 21 + 3
    elif resident == "yes" and level == "sophomore" and engineering == "no" and madison == "no" and 6 <= credit <= 11 :
        tuition = 494 * credit + 21 + 3 + 5
    elif resident == "yes" and level == "sophomore" and engineering == "no" and madison == "no" and 12 <= credit < 18:
        tuition = 7410 + 21 + 3 + 5
    elif resident == "yes" and level == "sophomore" and engineering == "no" and madison == "no" and 18 <= credit :
        tuition = 7410 + 21 + 3 + 5 + 482 * (credit - 18)
    
    elif resident == "yes" and level == "freshman" and engineering == "no" and madison == "yes" and credit < 6  : # madison freshman-senior
        tuition = 482 * credit + 21 + 3 + 7.5
    elif resident == "yes" and level == "freshman" and engineering == "no" and madison == "yes" and 6 <= credit <= 11 :
        tuition = 482 * credit + 21 + 3 + 5 + 7.5
    elif resident == "yes" and level == "freshman" and engineering == "no" and madison == "yes" and 12 <= credit < 18 :
        tuition = 7230 + 21 + 3 + 5 + 7.5
    elif resident == "yes" and level == "freshman" and engineering == "no" and madison == "yes" and 18 <= credit :
        tuition = 7230 + 21 + 3 + 5 + 482 * (credit - 18) + 7.5
    elif resident == "yes" and level == "sophomore" and engineering == "no" and madison == "yes" and credit < 6 :
        tuition = 494 * credit + 21 + 3 + 7.5
    elif resident == "yes" and level == "sophomore" and engineering == "no" and madison == "yes" and 6 <= credit <= 11 :
        tuition = 494 * credit + 21 + 3 + 5 + 7.5
    elif resident == "yes" and level == "sophomore" and engineering == "no" and madison == "yes" and 12 <= credit < 18 :
        tuition = 7410 + 21 + 3 + 5 + 7.5
    elif resident == "yes" and level == "sophomore" and engineering == "no" and madison == "yes" and 18 <= credit :
        tuition = 7410 + 21 + 3 + 5 + 482 * (credit - 18) + 7.5
    elif resident == "yes" and level == "junior" and engineering == "no" and madison == "yes" and credit <= 4 :
        tuition = 555 * credit + 21 + 3 + 7.5
    elif resident == "yes" and level == "junior" and engineering == "no" and madison == "yes" and credit == 5 :
        tuition = 555 * credit + 21 + 3 + 7.5
    elif resident == "yes" and level == "junior" and engineering == "no" and madison == "yes" and 6 <= credit <= 11 :
        tuition = 555 * credit + 21 + 3 + 5 + 7.5
    elif resident == "yes" and level == "junior" and engineering == "no" and madison == "yes" and 11 < credit <= 18 :
        tuition = 8325 + 21 + 3 + 5 + 7.5
    elif resident == "yes" and level == "junior" and engineering == "no" and madison == "yes" and 18 < credit :
        tuition = 8325 + (credit - 18) * 555 + 21 + 3 + 5 + 7.5
    elif resident == "yes" and level == "senior" and engineering == "no" and madison == "yes" and credit <= 4 :
        tuition = 555 * credit + 21 + 3 + 7.5
    elif resident == "yes" and level == "senior" and engineering == "no" and madison == "yes" and credit == 5 :
        tuition = 555 * credit + 21 + 3 + 7.5
    elif resident == "yes" and level == "senior" and engineering == "no" and madison == "yes" and 6 <= credit <= 11 :
        tuition = 555 * credit + 21 + 3 + 5 + 7.5
    elif resident == "yes" and level == "senior" and engineering == "no" and madison == "yes" and 11 < credit <= 18 :
        tuition = 8325 + 21 + 3 + 5 + 7.5
    elif resident == "yes" and level == "senior" and engineering == "no" and madison == "yes" and 18 < credit :
        tuition = 8325 + (credit - 18) * 555 + 21 + 3 + 5 + 7.5
        
    elif resident == "yes" and level == "junior" and engineering == "no" and madison == "no" and credit <= 4 and college == "business": # buisiness junior
        tuition = 573 * credit + 21 + 3 + 113
    elif resident == "yes" and level == "junior" and engineering == "no" and madison == "no" and credit == 5 and college == "business":
        tuition = 573 * credit + 21 + 3 + 226
    elif resident == "yes" and level == "junior" and engineering == "no" and madison == "no" and 6 <= credit <= 11 and college == "business":
        tuition = 573 * credit + 21 + 3 + 226 + 5
    elif resident == "yes" and level == "junior" and engineering == "no" and madison == "no" and 11 < credit <= 18 and college == "business":
        tuition = 8595 + 21 + 3 + 226 + 5
    elif resident == "yes" and level == "junior" and engineering == "no" and madison == "no" and 18 < credit and college == "business":
        tuition = 8595 + ((credit - 18) * 555) + 21 + 3 + 226 + 5
    
    elif resident == "yes" and level == "senior" and engineering == "no" and madison == "no" and credit <= 4 and college == "business": # buisiness senior
        tuition = 573 * credit + 21 + 3 + 113
    elif resident == "yes" and level == "senior" and engineering == "no" and madison == "no" and credit == 5 and college == "business":
        tuition = 573 * credit + 21 + 3 + 226
    elif resident == "yes" and level == "senior" and engineering == "no" and madison == "no" and 6 < credit <= 11 and college == "business":
        tuition = 573 * credit + 21 + 3 + 226 + 5
    elif resident == "yes" and level == "senior" and engineering == "no" and madison == "no" and 11 < credit <= 18 and college == "business":
        tuition = 8595 + 21 + 3 + 226 + 5
    elif resident == "yes" and level == "senior" and engineering == "no" and madison == "no" and 18 < credit and college == "business":
        tuition = 8595 + ((credit - 18) * 555) + 21 + 3 + 226 + 5
    
    elif resident == "yes" and level == "junior" and engineering == "no" and madison == "no" and credit <= 4 and college == "health" or college == "sciences": # health and sciences junior
        tuition = 555 * credit + 21 + 3 + 50
    elif resident == "yes" and level == "junior" and engineering == "no" and madison == "no" and credit == 5 and college == "health" or college == "sciences":
        tuition = 555 * credit + 21 + 3 + 100
    elif resident == "yes" and level == "junior" and engineering == "no" and madison == "no" and 6 <= credit <= 11 and college == "health" or college == "sciences":
        tuition = 555 * credit + 21 + 3 + 100 + 5
    elif resident == "yes" and level == "junior" and engineering == "no" and madison == "no" and 11 < credit <= 18 and college == "health" or college == "sciences":
        tuition = 8325 + 21 + 3 + 100 + 5
    elif resident == "yes" and level == "junior" and engineering == "no" and madison == "no" and 18 < credit and college == "health" or college == "sciences":
        tuition = 8325 + (credit - 18) * 555 + 21 + 3 + 100 + 5
    
    elif resident == "yes" and level == "senior" and engineering == "no" and madison == "no" and credit <= 4 and college == "health" or college == "sciences": # health and sciences senior
        tuition = 555 * credit + 21 + 3 + 50
    elif resident == "yes" and level == "senior" and engineering == "no" and madison == "no" and credit == 5 and college == "health" or college == "sciences":
        tuition = 555 * credit + 21 + 3 + 100
    elif resident == "yes" and level == "senior" and engineering == "no" and madison == "no" and 6 <= credit <= 11 and college == "health" or college == "sciences":
        tuition = 555 * credit + 21 + 3 + 100 + 5
    elif resident == "yes" and level == "senior" and engineering == "no" and madison == "no" and 11 < credit <= 18 and college == "health" or college == "sciences":
        tuition = 8325 + 21 + 3 + 100
    elif resident == "yes" and level == "senior" and engineering == "no" and madison == "no" and 18 < credit and college == "health" or college == "sciences":
        tuition = 8325 + (credit - 18) * 555 + 21 + 3 + 100 + 5
    
    elif resident == "yes" and level == "junior" and engineering == "no" and madison == "no" and credit <= 4 and cmse == "yes" : # cmse junior
        tuition = 555 * credit + 21 + 3 + 402
    elif resident == "yes" and level == "junior" and engineering == "no" and madison == "no" and credit == 5 and cmse == "yes" :
        tuition = 555 * credit + 21 + 3 + 670
    elif resident == "yes" and level == "junior" and engineering == "no" and madison == "no" and 6 <= credit <= 11 and cmse == "yes":
        tuition = 555 * credit + 21 + 3 + 670 + 5
    elif resident == "yes" and level == "junior" and engineering == "no" and madison == "no" and 11 < credit <= 18 and cmse == "yes":
        tuition = 8325 + 21 + 3 + 670 + 5
    elif resident == "yes" and level == "junior" and engineering == "no" and madison == "no" and 18 < credit and cmse == "yes":
        tuition = 8325 + (credit - 18) * 555 + 21 + 3 + 670 + 5
    
    elif resident == "yes" and level == "senior" and engineering == "no" and madison == "no" and credit <= 4 and cmse == "yes": # cmse senior
        tuition = 555 * credit + 21 + 3 + 402
    elif resident == "yes" and level == "senior" and engineering == "no" and madison == "no" and credit == 5 and cmse == "yes":
        tuition = 555 * credit + 21 + 3 + 670
    elif resident == "yes" and level == "senior" and engineering == "no" and madison == "no" and 6 <= credit <= 11 and cmse == "yes":
        tuition = 555 * credit + 21 + 3 + 670 + 5
    elif resident == "yes" and level == "senior" and engineering == "no" and madison == "no" and 11 < credit <= 18 and cmse == "yes":
        tuition = 8325 + 21 + 3 + 670
    elif resident == "yes" and level == "senior" and engineering == "no" and madison == "no" and 18 < credit and cmse == "yes":
        tuition = 8325 + (credit - 18) * 555 + 21 + 3 + 670 + 5
    
    
    elif resident == "yes" and level == "freshman" and engineering == "yes" and madison == "no" and credit <= 4  :  # college of engineering freshman
        tuition = 482 * credit + 21 + 3 + 402 
    elif resident == "yes" and level == "freshman" and engineering == "yes" and madison == "no" and credit == 5  :
        tuition = 482 * credit + 21 + 3 + 670 
    elif resident == "yes" and level == "freshman" and engineering == "yes" and madison == "no" and 6 <= credit <= 11  :
        tuition = 482 * credit + 21 + 3 + 5 + 670
    elif resident == "yes" and level == "freshman" and engineering == "yes" and madison == "no" and 12 <= credit < 18 :
        tuition = 7230 + 21 + 3 + 5 + 670
    elif resident == "yes" and level == "freshman" and engineering == "yes" and madison == "no" and 18 <= credit :
        tuition = 7230 + 21 + 3 + 5 + 482 * (credit - 18) + 670
    
    elif resident == "yes" and level == "sophomore" and engineering == "yes" and madison == "no" and credit <= 4 : # college of engineering sophomore
        tuition = 494 * credit + 21 + 3 + 402
    elif resident == "yes" and level == "sophomore" and engineering == "yes" and madison == "no" and credit == 5  :
        tuition = 482 * credit + 21 + 3 + 670 
    elif resident == "yes" and level == "sophomore" and engineering == "yes" and madison == "no" and 6 <= credit <= 11 :
        tuition = 494 * credit + 21 + 3 + 5 + 670
    elif resident == "yes" and level == "sophomore" and engineering == "yes" and madison == "no" and 12 <= credit < 18 :
        tuition = 7410 + 21 + 3 + 5 + 670
    elif resident == "yes" and level == "sophomore" and engineering == "yes" and madison == "no" and 18 <= credit :
        tuition = 7410 + 21 + 3 + 5 + 482 * (credit - 18) + 670 
        
    elif resident == "yes" and level == "junior" and college == "engineering" and madison == "no" and credit <= 4  :  # college of engineering junior
        tuition = 573 * credit + 21 + 3 + 402 
    elif resident == "yes" and level == "junior" and college == "engineering" and madison == "no" and credit == 5  :
        tuition = 573 * credit + 21 + 3 + 670 
    elif resident == "yes" and level == "junior" and college == "engineering" and madison == "no" and 6 <= credit <= 11  :
        tuition = 573 * credit + 21 + 3 + 5 + 670
    elif resident == "yes" and level == "junior" and college == "engineering" and madison == "no" and 12 <= credit < 18 :
        tuition = 8595 + 21 + 3 + 5 + 670
    elif resident == "yes" and level == "junior" and college == "engineering" and madison == "no" and 18 <= credit :
        tuition = 8595 + 21 + 3 + 5 + 573 * (credit - 18) + 670
    
    elif resident == "yes" and level == "senior" and college == "engineering" and madison == "no" and credit <= 4 : # college of engineering senior
        tuition = 573 * credit + 21 + 3 + 402
    elif resident == "yes" and level == "senior" and college == "engineering" and madison == "no" and credit == 5  :
        tuition = 573 * credit + 21 + 3 + 670 
    elif resident == "yes" and level == "senior" and college == "engineering" and madison == "no" and 6 <= credit <= 11 :
        tuition = 573 * credit + 21 + 3 + 5 + 670
    elif resident == "yes" and level == "senior" and college == "engineering" and madison == "no" and 12 <= credit < 18 :
        tuition = 8595 + 21 + 3 + 5 + 670
    elif resident == "yes" and level == "senior" and college == "engineering" and madison == "no" and 18 <= credit :
        tuition = 8595 + 21 + 3 + 5 + 482 * (credit - 18) + 670 
        
        # international calculations
        
    elif resident == "no" and level == "freshman" and engineering == "no" and madison == "no" and credit <= 4 :    # non cse or JM freshman/ sophmore
        tuition = 1325.5 * credit + 21 + 3 + 375
    elif resident == "no" and level == "freshman" and engineering == "no" and madison == "no" and credit == 5 :
        tuition = 1325.5 * credit + 21 + 3 + 750
    elif resident == "no" and level == "freshman" and engineering == "no" and madison == "no" and 6 <= credit <= 11 :
        tuition = 1325.5 * credit + 21 + 3 + 5 + 750
    elif resident == "no" and level == "freshman" and engineering == "no" and madison == "no" and 12 <= credit < 18 :
        tuition = 19883 + 21 + 3 + 5 + 750
    elif resident == "no" and level == "freshman" and engineering == "no" and madison == "no" and 18 <= credit :
        tuition = 19883+ 21 + 3 + 5 + 1325.5 * (credit - 18) + 750
    elif resident == "no" and level == "sophomore" and engineering == "no" and madison == "no" and credit <= 4 :
        tuition = 1325.5 * credit + 21 + 3 + 375
    elif resident == "no" and level == "sophomore" and engineering == "no" and madison == "no" and credit == 5 :
        tuition = 132.55 * credit + 21 + 3 + 750
    elif resident == "no" and level == "sophomore" and engineering == "no" and madison == "no" and 6 <= credit <= 11 :
        tuition = 1325.5 * credit + 21 + 3 + 5 + 750
    elif resident == "no" and level == "sophomore" and engineering == "no" and madison == "no" and 12 <= credit < 18 :
        tuition = 19883 + 21 + 3 + 5 + 750
    elif resident == "no" and level == "sophomore" and engineering == "no" and madison == "no" and 18 <= credit :
        tuition = 19883 + 21 + 3 + 5 + 1325.5 * (credit - 18) + 750
    
    elif resident == "no" and level == "freshman" and engineering == "no" and madison == "yes" and credit <= 4  : # madison freshman-senior
        tuition = 1325.5 * credit + 21 + 3 + 7.5 + 375
    elif resident == "no" and level == "freshman" and engineering == "no" and madison == "yes" and credit == 5  : # madison freshman-senior
        tuition = 1325.5 * credit + 21 + 3 + 7.5 + 750
    elif resident == "no" and level == "freshman" and engineering == "no" and madison == "yes" and 6 <= credit <= 11 :
        tuition = 1325.5 * credit + 21 + 3 + 5 + 7.5 + 750
    elif resident == "no" and level == "freshman" and engineering == "no" and madison == "yes" and 12 <= credit < 18 :
        tuition = 19883 + 21 + 3 + 5 + 7.5 + 750
    elif resident == "no" and level == "freshman" and engineering == "no" and madison == "yes" and 18 <= credit :
        tuition = 19883 + 21 + 3 + 5 + 1325 * (credit - 18) + 7.5
    elif resident == "no" and level == "sophomore" and engineering == "no" and madison == "yes" and credit <= 4 :
        tuition = 1325.5 * credit + 21 + 3 + 7.5 + 375
    elif resident == "no" and level == "sophomore" and engineering == "no" and madison == "yes" and credit == 5 :
        tuition = 1325.5 * credit + 21 + 3 + 7.5 + 750
    elif resident == "no" and level == "sophomore" and engineering == "no" and madison == "yes" and 6 <= credit <= 11 :
        tuition = 1325.5 * credit + 21 + 3 + 5 + 7.5 +750
    elif resident == "no" and level == "sophomore" and engineering == "no" and madison == "yes" and 12 <= credit < 18 :
        tuition = 19883 + 21 + 3 + 5 + 7.5 + 750
    elif resident == "no" and level == "sophomore" and engineering == "no" and madison == "yes" and 18 <= credit :
        tuition = 19883 + 21 + 3 + 5 + 1325.5 * (credit - 18) + 7.5 + 750
    elif resident == "no" and level == "junior" and engineering == "no" and madison == "yes" and credit <= 4 :
        tuition = 1366.75 * credit + 21 + 3 + 7.5 + 375
    elif resident == "no" and level == "junior" and engineering == "no" and madison == "yes" and credit == 5 :
        tuition = 1366.75 * credit + 21 + 3 + 7.5 + 750
    elif resident == "no" and level == "junior" and engineering == "no" and madison == "yes" and 6 <= credit <= 11 :
        tuition = 1366.75 * credit + 21 + 3 + 5 + 7.5 +750
    elif resident == "no" and level == "junior" and engineering == "no" and madison == "yes" and 11 < credit <= 18 :
        tuition = 20501 + 21 + 3 + 5 + 7.5 + 750
    elif resident == "no" and level == "junior" and engineering == "no" and madison == "yes" and 18 < credit :
        tuition = 20501 + (credit - 18) * 1366.75 + 21 + 3 + 5 + 7.5 + 750
    elif resident == "no" and level == "senior" and engineering == "no" and madison == "yes" and credit <= 4 :
        tuition = 1366.75 * credit + 21 + 3 + 7.5 + 375
    elif resident == "no" and level == "senior" and engineering == "no" and madison == "yes" and credit == 5 :
        tuition = 1366.75 * credit + 21 + 3 + 7.5 +750
    elif resident == "no" and level == "senior" and engineering == "no" and madison == "yes" and 6 <= credit <= 11 :
        tuition = 1366.75 * credit + 21 + 3 + 5 + 7.5 + 750
    elif resident == "no" and level == "senior" and engineering == "no" and madison == "yes" and 11 < credit <= 18 :
        tuition = 20501 + 21 + 3 + 5 + 7.5 + 750
    elif resident == "no" and level == "senior" and engineering == "no" and madison == "yes" and 18 < credit :
        tuition = 20501 + (credit - 18) * 1366.75 + 21 + 3 + 5 + 7.5 + 750
        
    elif resident == "no" and level == "junior" and engineering == "no" and madison == "no" and credit <= 4 and college == "business": # buisiness junior
        tuition = 1385.75 * credit + 21 + 3 + 113 + 375
    elif resident == "no" and level == "junior" and engineering == "no" and madison == "no" and credit == 5 and college == "business":
        tuition = 1385.75 * credit + 21 + 3 + 226 + 750
    elif resident == "no" and level == "junior" and engineering == "no" and madison == "no" and 6 <= credit <= 11 and college == "business":
        tuition = 1385.75 * credit + 21 + 3 + 226 + 5 + 750
    elif resident == "no" and level == "junior" and engineering == "no" and madison == "no" and 11 < credit <= 18 and college == "business":
        tuition = 20786 + 21 + 3 + 226 + 5 + 750
    elif resident == "no" and level == "junior" and engineering == "no" and madison == "no" and 18 < credit and college == "business":
        tuition = 20786 + ((credit - 18) * 1385.75) + 21 + 3 + 226 + 5 + 750
    
    elif resident == "no" and level == "senior" and engineering == "no" and madison == "no" and credit <= 4 and college == "business": # buisiness senior
        tuition = 1385.75 * credit + 21 + 3 + 113 + 375
    elif resident == "no" and level == "senior" and engineering == "no" and madison == "no" and credit == 5 and college == "business":
        tuition = 1385.75 * credit + 21 + 3 + 226 + 750
    elif resident == "no" and level == "senior" and engineering == "no" and madison == "no" and 6 < credit <= 11 and college == "business":
        tuition = 1385.75 * credit + 21 + 3 + 226 + 5 + 750
    elif resident == "no" and level == "senior" and engineering == "no" and madison == "no" and 11 < credit <= 18 and college == "business":
        tuition = 20786 + 21 + 3 + 226 + 5 + 750
    elif resident == "no" and level == "senior" and engineering == "no" and madison == "no" and 18 < credit and college == "business":
        tuition = 20786 + ((credit - 18) * 1385.75) + 21 + 3 + 226 + 5 + 750
    
    elif resident == "no" and level == "junior" and engineering == "no" and madison == "no" and credit <= 4 and college == "health" or college == "sciences": # health and sciences junior
        tuition = 1366.75 * credit + 21 + 3 + 50 + 375
    elif resident == "no" and level == "junior" and engineering == "no" and madison == "no" and credit == 5 and college == "health" or college == "sciences":
        tuition = 1366.75 * credit + 21 + 3 + 100 + 750
    elif resident == "no" and level == "junior" and engineering == "no" and madison == "no" and 6 <= credit <= 11 and college == "health" or college == "sciences":
        tuition = 1366.75 * credit + 21 + 3 + 100 + 5 + 750
    elif resident == "no" and level == "junior" and engineering == "no" and madison == "no" and 11 < credit <= 18 and college == "health" or college == "sciences":
        tuition = 20501 + 21 + 3 + 100 + 5 + 750
    elif resident == "no" and level == "junior" and engineering == "no" and madison == "no" and 18 < credit and college == "health" or college == "sciences":
        tuition = 20501 + (credit - 18) * 1366.75 + 21 + 3 + 100 + 5 + 750
    
    elif resident == "no" and level == "senior" and engineering == "no" and madison == "no" and credit <= 4 and college == "health" or college == "sciences": # health and sciences senior
        tuition = 1366.75 * credit + 21 + 3 + 50 +375
    elif resident == "no" and level == "senior" and engineering == "no" and madison == "no" and credit == 5 and college == "health" or college == "sciences":
        tuition = 1366.75 * credit + 21 + 3 + 100 + 750
    elif resident == "no" and level == "senior" and engineering == "no" and madison == "no" and 6 <= credit <= 11 and college == "health" or college == "sciences":
        tuition = 1366.75 * credit + 21 + 3 + 100 + 5 +750 
    elif resident == "no" and level == "senior" and engineering == "no" and madison == "no" and 11 < credit <= 18 and college == "health" or college == "sciences":
        tuition = 20501 + 21 + 3 + 100 + 750
    elif resident == "no" and level == "senior" and engineering == "no" and madison == "no" and 18 < credit and college == "health" or college == "sciences":
        tuition = 20501 + (credit - 18) * 1366.75 + 21 + 3 + 100 + 5 + 750
    
    elif resident == "no" and level == "junior" and engineering == "no" and madison == "no" and credit <= 4 and cmse == "yes" : # cmse junior
        tuition = 1366.75 * credit + 21 + 3 + 402 + 375
    elif resident == "no" and level == "junior" and engineering == "no" and madison == "no" and credit == 5 and cmse == "yes" :
        tuition = 1366.75 * credit + 21 + 3 + 670 + 750
    elif resident == "no" and level == "junior" and engineering == "no" and madison == "no" and 6 <= credit <= 11 and cmse == "yes":
        tuition = 1366.75 * credit + 21 + 3 + 670 + 5 + 750
    elif resident == "no" and level == "junior" and engineering == "no" and madison == "no" and 11 < credit <= 18 and cmse == "yes":
        tuition = 20501 + 21 + 3 + 670 + 5 + 750
    elif resident == "no" and level == "junior" and engineering == "no" and madison == "no" and 18 < credit and cmse == "yes":
        tuition = 20501 + (credit - 18) * 1366.75 + 21 + 3 + 670 + 5 + 750
    
    elif resident == "no" and level == "senior" and engineering == "no" and madison == "no" and credit <= 4 and cmse == "yes": # cmse senior
        tuition = 1366.75 * credit + 21 + 3 + 402 + 375
    elif resident == "no" and level == "senior" and engineering == "no" and madison == "no" and credit == 5 and cmse == "yes":
        tuition = 1366.75 * credit + 21 + 3 + 670 + 750
    elif resident == "no" and level == "senior" and engineering == "no" and madison == "no" and 6 <= credit <= 11 and cmse == "yes":
        tuition = 1366.75 * credit + 21 + 3 + 670 + 5 + 750
    elif resident == "no" and level == "senior" and engineering == "no" and madison == "no" and 11 < credit <= 18 and cmse == "yes":
        tuition = 20501 + 21 + 3 + 670 + 750
    elif resident == "no" and level == "senior" and engineering == "no" and madison == "no" and 18 < credit and cmse == "yes":
        tuition = 20501 + (credit - 18) * 1366.75 + 21 + 3 + 670 + 5 + 750
    
    
    elif resident == "no" and level == "freshman" and engineering == "yes" and madison == "no" and credit <= 4  :  # college of engineering freshman
        tuition = 1325.5 * credit + 21 + 3 + 402 + 375
    elif resident == "no" and level == "freshman" and engineering == "yes" and madison == "no" and credit == 5  :
        tuition = 1325.5 * credit + 21 + 3 + 670 + 750
    elif resident == "no" and level == "freshman" and engineering == "yes" and madison == "no" and 6 <= credit <= 11  :
        tuition = 1325.5 * credit + 21 + 3 + 5 + 670 + 750
    elif resident == "no" and level == "freshman" and engineering == "yes" and madison == "no" and 12 <= credit < 18 :
        tuition = 19883 + 21 + 3 + 5 + 670 + 750
    elif resident == "no" and level == "freshman" and engineering == "yes" and madison == "no" and 18 <= credit :
        tuition = 19883 + 21 + 3 + 5 + 1325.5 * (credit - 18) + 670 + 750
    
    elif resident == "no" and level == "sophomore" and engineering == "yes" and madison == "no" and credit <= 4 : # college of engineering sophomore
        tuition = 1325.5 * credit + 21 + 3 + 402 + 375
    elif resident == "no" and level == "sophomore" and engineering == "yes" and madison == "no" and credit == 5  :
        tuition = 1325.5 * credit + 21 + 3 + 670 + 750
    elif resident == "no" and level == "sophomore" and engineering == "yes" and madison == "no" and 6 <= credit <= 11 :
        tuition = 1325.5 * credit + 21 + 3 + 5 + 670 + 750
    elif resident == "no" and level == "sophomore" and engineering == "yes" and madison == "no" and 12 <= credit < 18 :
        tuition = 19883 + 21 + 3 + 5 + 670 + 750
    elif resident == "no" and level == "sophomore" and engineering == "yes" and madison == "no" and 18 <= credit :
        tuition = 19883 + 21 + 3 + 5 + 1325.5 * (credit - 18) + 670 + 750        
    
    elif resident == "no" and level == "junior" and college == "engineering" and madison == "no" and credit <= 4  :  # college of engineering junior
        tuition = 1385.75 * credit + 21 + 3 + 402 + 375
    elif resident == "no" and level == "junior" and college == "engineering" and madison == "no" and credit == 5  :
        tuition = 1385.75 * credit + 21 + 3 + 670 +750
    elif resident == "no" and level == "junior" and college == "engineering" and madison == "no" and 6 <= credit <= 11  :
        tuition = 1385.75 * credit + 21 + 3 + 5 + 670 + 750
    elif resident == "no" and level == "junior" and college == "engineering" and madison == "no" and 12 <= credit < 18 :
        tuition = 20786 + 21 + 3 + 5 + 670 + 750
    elif resident == "no" and level == "junior" and college == "engineering" and madison == "no" and 18 <= credit :
        tuition = 20786 + 21 + 3 + 5 + 1385.75 * (credit - 18) + 670 + 750
    
    elif resident == "no" and level == "senior" and college == "engineering" and madison == "no" and credit <= 4 : # college of engineering senior
        tuition =  1385.75 * credit + 21 + 3 + 402 + 375
    elif resident == "no" and level == "senior" and college == "engineering" and madison == "no" and credit == 5  :
        tuition = 1385.75 * credit + 21 + 3 + 670 + 750
    elif resident == "no" and level == "senior" and college == "engineering" and madison == "no" and 6 <= credit <= 11 :
        tuition = 1385.75 * credit + 21 + 3 + 5 + 670 + 750
    elif resident == "no" and level == "senior" and college == "engineering" and madison == "no" and 12 <= credit < 18 :
        tuition = 20786 + 21 + 3 + 5 + 670 + 750
    elif resident == "no" and level == "senior" and college == "engineering" and madison == "no" and 18 <= credit :
        tuition = 20786 + 21 + 3 + 5 + 1385.75 * (credit - 18) + 670 + 750
    else :
        continue 
    tuition = float (tuition)                                                     # print tuition and ask to calculate again or to stop
    print ("Tuition is ${:,.2f}.".format(tuition))
    c = input ("Do you want to do another calculation (yes/no):")
    if c.lower() == "yes":
        continue 
    else :
        break
    
    
    
    
    
    
    
        
        
                        
        
                
    
            