from unittest import case
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re
import random

########################################################################################################################################

def Not_BC(string):
    """ This function evaluates an string, if it finds B.C or b.c it return 0, else it returns
    the same string."""
    try:
        a = re.findall('(?i)B\.C',str(string))
        if a == []:
            return string
        else:
            return np.nan
    except IndexError:
        return string
# Way to apply it: df['date'] = df.date.apply(Not_BC)

def digits_digits(string):
    """ This function evaluates a string, if it finds 2 numbers made of four digits separated by something that is not a number
    then it calculates de average and returns the average as a float. If it doesn't find any coincidence it returns the same string.
    """
    try:
        b = re.findall('^\d{4}-\d{4}$', str(string))
        if b != []:
            #return int((int(a[0][:4])+int(a[0][5:]))//2)
            return string #.
        else:
            return string
    except IndexError:
        return string
    except ValueError:
        return string
# Way to apply it: df['date'] = df.date.apply(digits_digits)

def earlies_lates(string):
    """ This function evaluates a string, if it finds a four digint number finished with an s or an 's it returns
    the same number plus 5 as an integer. If it doesn't find any coincidence it returns the same string.
    """
    try:
        c = re.findall("\d{4}'s|\d{4}s", str(string))
        if c != None:
            return int(a[0][:4])+5
    except IndexError:
        return string
# Way to apply it: df['date'] = df.date.apply(earlies_lates)

def four_digits(string):
    """This digit looks for any 4 digits it can find in the string and returns them as an integer, if it doesn't find 
    any number it returns a 0."""
    try:
        a = re.findall("\d{4}", str(string))
        if a != None:
            return a[0]
        else:
            return 0
    except IndexError:
        return 0

# Way to apply it: df['date'] = df.date.apply(four_digits)

# This last function evaluates the data in a column of the set, using the functions created above in the proper order,
def clean_column(string):
    """This function apply the functions: Not_BC, digits_digits, earlies_lates, four_digits. In that order. 
    It also gives all the 0s and NaNs only as NaNs."""
    print('entra a aqui')
    string = Not_BC(string)
    string = digits_digits(string)
    string = earlies_lates(string)
    string = four_digits(string) # Here we made sure all the column values are either a 4 digit number or 0, now we make all 0s NaNs.
    if int(string) == 0: return np.nan
    else: return string


# This next function is going to be able to replace the year, in the cases where the data isnt found in it for the data in the other columns,
def year_replacement(array):
    """We need to input an array with the following order: [year, date, case_num, case_num1, case_num2]
    it will return the year when the attack happened"""
    year, date, case_num, case_num1, case_num2 = array
    if year != 0.0 and year is not np.nan:
        return int(year)
    elif not date.isnan():
        return int(date)
    elif not case_num.isnan():
        return case_num
    elif not case_num1.isnan():
        return case_num1
    elif not case_num2.isnan():
        return case_num2
    else: return np.nan

# Functions to achieve the third point,
def clean_names(string):
    """This function takes a string and returns a name, it also checks if the string may cotain something other than a name, if it does it returns 
    a np.nan."""
    if re.findall('(?i)girl|(?i)male|(?i)man|(?i)woman|(?i)boy|^\d|.+boat.+', string.strip()) == []: # if we don't find anything that may indicate that what is writen isn't a name.
        return string.strip()[0]
    else: return np.nan

#Function to clean the sex coulumn,
def clean_sex(string):

    if re.findall('M', str(string).strip()):
        return 0   
    elif re.findall('F', str(string).strip()):
        return 1
    else:
        return np.nan

def clean_age(string):
    string= str(string)
    if re.findall('^\d', string.strip()): # first we make sure it starts with a digit to avoid all the text (such as: 'adult')
        if re.findall('^\d{2}$', string.strip()):
            return int(list(re.findall('^\d{2}$', string.strip()))[0]) # here we extract most of the data, all the 2 digit cases
        elif re.findall('^\d{1}$', string.strip()):
            return int(list(re.findall('^\d{1}$', string.strip()))[0]) # for numbers under 10
        elif re.findall('(?i)month', string.strip()): # if there is a child under 1, we are going to considerd it 1 year old, it is precise enough
            return 1
        elif re.findall('\d{2}', string.strip()):
            av = 0
            for age in list(re.findall('\d{2}', string.strip())): # we calculate the average of the age of the people that were attacked
                av += int(age)
            return int(av/len(list(re.findall('\d{2}', string.strip()))))

        elif re.findall('½', string.strip()):
            return string[0]
        elif re.findall('^\d{1} or', string.strip()):
            return (int(string[0])+int(string[len(string)-1]))//2
        elif re.findall('\d{1}', string.strip()):
            av = 0
            for age in list(re.findall('\d{1}', string.strip())): # we calculate the average of the age of the people that were attacked
                av += int(age)
            #return int(av/len(list(re.findall('\d{2}', string.strip()))))
        
    elif re.findall('(?i)teen', string.strip()):
        return random.choice(range(10,20))
    else: return np.nan