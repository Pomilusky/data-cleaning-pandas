from operator import index
from unittest import case
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re
import random
from pycountry_convert import country_alpha2_to_continent_code, country_name_to_country_alpha2

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
            return int(c[0][:4])+5
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
    string = Not_BC(string)
    string = digits_digits(string)
    string = earlies_lates(string)
    string = four_digits(string) # Here we made sure all the column values are either a 4 digit number or 0, now we make all 0s NaNs.
    if int(string) == 0: return np.nan
    else: return string


# This next function is going to be able to replace the year, in the cases where the data isnt found in it for the data in the other columns,
def year_replacement(df):
    """This function recives a data frame and iterates through the values of the rows, acceding to some of the 
    values in them, and picking the one that it needs. It returns a Serie."""
    resultat = dict()
    for i, row in df.iterrows():
        if row['year'] != 0.0 and row['year'] is not np.nan:
            resultat[i] = row['year']
        elif row['date']:
            #print(row['date'])
            resultat[i] = row['date']
        elif row['case_number'] and int(row['case_number']) > 1000:
            resultat[i] = row['case_number']
        else:
            resultat[i] = np.nan
    #print(resultat)
    return pd.Series(resultat)

# Functions to achieve the third point,
def clean_names(string):
    """This function takes a string and returns a name, it also checks if the string may cotain something other than a name, if it does it returns 
    a np.nan."""
    string = str(string)
    if re.findall('(?i)girl|(?i)male|(?i)man|(?i)woman|(?i)boy|^\d|.+boat.+', string.strip()) == []: # if we don't find anything that may indicate that what is writen isn't a name.
        return list(re.findall('(?i)[a-z]', string.strip()))[0].lower()
    else: return np.nan

#Function to clean the sex coulumn,
def clean_sex(string):
    if re.findall('M', str(string).strip()) != []:
        return 0   
    elif re.findall('F', str(string).strip()) != []:
        return 1
    elif re.findall('M|F', str(string).strip()) == []:
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

# function to clean the country column,
def country_clean(column):
    continents = {
        'NA': 'North America',
        'SA': 'South America', 
        'AS': 'Asia',
        'OC': 'Australia',
        'AF': 'Africa',
        'EU': 'Europe'
    }

    countries = list()
    for i in column:
        if type(i) != str:
            countries.append('np.nan')
        else: 
            countries.append(i.replace('_',' ').title().replace('&','and'))
    result = []
    result_countries = []
    errors = []
    for country in countries:
        if '?' in country: country = country[:len(country)-1]
        if country == 'Usa' or country == 'Columbia' or 'New Britain' in country: country = 'United States'
        elif 'England' == country or 'British' in country or country == 'Scotland': country = 'United Kingdom'
        elif 'Ceylon' in country: country = 'Sri Lanka'
        elif 'Anda' in country: country = 'India'
        elif 'Red Sea' in country: country = 'Egypt'
        elif 'Reunion' in country: country = 'Madagascar' # It is the closest country to the islands, even though they are a French colony (Won't put it as French territory, colonies should be part of the past, also wouldn't a good indicator)
        elif 'Okinawa' == country: country = 'Japan'
        elif 'Arab Emirates' in country or 'Persian Gulf' in country or 'Arabian' in country: country = 'United Arab Emirates'
        elif 'Antigua' == country: country = 'Antigua and Barbuda'
        elif 'Johnston Island' == country or 'Pacific' in country or 'Pacifc' in country: country = 'Pacific Ocean'
        elif 'Azores' == country or 'Atlantic' in country or 'Caribbean' in country: country = 'Atlantic ocean'
        elif 'New Guinea' == country or 'Admiralty Islands' == country: country='Papua New Guinea'
        elif country in ['Java', 'Indian Ocean', 'Inida','Bay Of Bengal','Andaman Islands']: country = 'India'
        elif 'Federated States Of Micronesia' == country: country = 'Federated States of Micronesia'
        elif 'Burma' == country: country= 'Myanmar'
        elif '/' in country: country = country.split('/')[0].strip()
        elif country == 'Gulf Of Aden': country = 'Egypt'
        elif 'Maldi' in country: country = 'Maldives'
        elif country in ['St. Maartin','Curacao', 'Nevis','Roatan','San Domingo','Netherlands Antilles']:
            country = 'Atlantic ocean'
        elif 'Tobago' == country: country = 'Trinidad and Tobago'
        elif 'Crete' == country or 'Mediterranean Sea' == country: country = 'Greece'
        elif 'Bahrein' == country: country = 'Bahrain'
        elif 'Palestin' in country: country = 'Palestine'
        elif 'China' in country: country = 'China'
        elif 'North Sea' in country: country = 'Sweden'
        elif 'West Indies' == country: country = 'Mexico'
        elif 'Tasman Sea' == country: country = 'Australia'
        elif 'Western Samoa' == country: country = 'Samoa'
        elif 'The Balkans' == country: country = 'Albania'
        elif 'Korea' == country: country = 'South Korea'
        elif 'Cayman' in country: country = 'Cayman Islands'
        elif 'np.nan' == country: country = np.nan
        result_countries.append(country)

        try:
            result.append(continents[country_alpha2_to_continent_code(country_name_to_country_alpha2(country))])
        except KeyError:
            if country in ['Atlantic ocean','Pacific Ocean', 'Asia'] or 'Africa' in country:
                if 'Af' in country:
                    result.append('Africa')
                else: result.append(country)
            else:
                errors.append(country)
                result.append(np.nan)
        except TypeError:
            errors.append(country)
            result.append(np.nan)
    return result_countries, result, errors

def append_world(column):
    if column == 'Oceania':
        return 1862
    elif column == 'North America':
        return 2654
    elif column == 'Europe':
        return 265
    elif column == 'Africa':
        return 837
    elif column == 'Asia':
        return 372
    elif column == 'South America':
        return 151
    else:
        return 0

def append_world_country(column, Serie):
    countries = Serie.index.values.tolist()
    #print(countries)
    if column in countries:
        return Serie[column]
        
    else:
        return 0
    