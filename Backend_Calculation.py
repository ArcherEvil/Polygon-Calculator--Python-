# File where the program calculate.
from math import *


def triangle_area(values):
    # converting the strings to floats
    converted = ["Area"]

    for n in values:
        if n == '':
            converted.append(n)
            continue
        try:
            converted.append(float(n))
        except:
            return False
    
    if converted[3] == "":
        # discovering Hipoteneuse
        side = sqrt((converted[1])**2 + (converted[2])**2)
        converted[3] = round(side, 4)

    if converted[1] == "":
        # discovering the side
        side = sqrt((converted[3])**2 - (converted[2])**2)
        converted[1] = round(side, 4)

    if converted[2] == "":
        # discovering the side
        side = sqrt((converted[3])**2 - (converted[1])**2)
        converted[2] = round(side, 4)

    # Calculating Area
    area = (converted[1] * converted[2])/2
    converted.append(round(area, 4))
    return converted
        
def triangle_perimeter(values):
    # converting the strings to floats
    converted = ["Perimeter"]

    for n in values:
        if n == '':
            converted.append(n)
            continue
        try:
            converted.append(float(n))
        except:
            return False
    
    
    if converted[3] == "":
        # discovering Hipoteneuse
        side = sqrt((converted[1])**2 + (converted[2])**2)
        converted[3] = round(side, 4)

    if converted[1] == "":
        # discovering the side
        side = sqrt((converted[3])**2 - (converted[2])**2)
        converted[1] = round(side, 4)

    if converted[2] == "":
        # discovering the side
        side = sqrt((converted[3])**2 - (converted[1])**2)
        converted[2] = round(side, 4)

    # Calculating Perimeter
    area = converted[1] + converted[2] + converted[3]
    converted.append(round(area,4))
    print(converted)
    return converted
        

def square_area(values):
    # converting the strings to floats
    converted = ["Area"]

    for n in values:
        if n == '':
            converted.append(n)
            continue
        try:
            converted.append(float(n))
        except:
            return False
    
    if converted[3] == "":
        # discovering diagonal
        side = sqrt((converted[1])**2 + (converted[2])**2)
        converted[3] = round(side, 4)

    if converted[1] == "":
        # discovering the side
        side = sqrt((converted[3])**2 - (converted[2])**2)
        converted[1] = round(side, 4)

    if converted[2] == "":
        # discovering the side
        side = sqrt((converted[3])**2 - (converted[1])**2)
        converted[2] = round(side, 4)

    # Calculating Area
    area = converted[1] * converted[2]
    converted.append(round(area, 4))
    return converted
        
def square_perimeter(values):
    # converting the strings to floats
    converted = ["Perimeter"]

    for n in values:
        if n == '':
            converted.append(n)
            continue
        try:
            converted.append(float(n))
        except:
            return False
    
    
    if converted[3] == "":
        # discovering Hipoteneuse
        side = sqrt((converted[1])**2 + (converted[2])**2)
        converted[3] = round(side, 4)

    if converted[1] == "":
        # discovering the side
        side = sqrt((converted[3])**2 - (converted[2])**2)
        converted[1] = round(side, 4)

    if converted[2] == "":
        # discovering the side
        side = sqrt((converted[3])**2 - (converted[1])**2)
        converted[2] = round(side, 4)

    # Calculating Perimeter
    area = (converted[1] + converted[2]) * 2
    converted.append(round(area,4))
    print(converted)
    return converted
        
def pentagon(types, values):
    converted = [types, values]

    # calculate apotema

    apotema = values / (2 * tan(radians(36)))
    converted.append(round(apotema, 4))

    # diagonal

    diagonal = values * (1 + sqrt(5)) / 2
    converted.append(round(diagonal, 4))

    if types == "Area":
        area = 5 * values**2 * sqrt((5 + sqrt(5))/2)
        converted.append(round(area, 4))
    elif types == "Perimeter":
        perimeter = 5 * values
        converted.append(round(perimeter, 4))
    
    return converted

        
def hexagon(types, values):
    converted = [types, values]

    # calculate apotema

    apotema = (values * sqrt(3))/2 
    converted.append(round(apotema, 4))

    # diagonal

    diagonal = (values * sin(radians(120))) / sin(radians(30))
    converted.append(round(diagonal, 4))

    if types == "Area":
        area = (3 * (values**2)*sqrt(3))/2
        converted.append(round(area, 4))
    elif types == "Perimeter":
        perimeter = 6 * values
        converted.append(round(perimeter, 4))
    
    return converted

