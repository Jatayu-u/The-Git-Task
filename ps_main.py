#Print result after every function to check 
#Read the info in every functions to get the proper understanding of desired output

import json
from multiprocessing.sharedctypes import Value
filepaths='./data.json'

def read_data(filepaths):
    with open(filepaths) as json_file:
        data = json.load(json_file)
    return data

data = read_data(filepaths)


def get_oldest(data):
    max=0
    c=0
    oldest={}
    for i in data["AVENGERS"]:
        if (data["AVENGERS"][i]['age'] > max):
            max=data["AVENGERS"][i]['age']
            oldest[c]=data["AVENGERS"][i]

    for i in data["DC"]:
        if (data["DC"][i]['age'] >max):
            max=data["DC"][i]['age']
            oldest[c]=data["DC"][i]
            

        if data["DC"][i]['age'] == max:
            c+=1
            oldest[c]=data["DC"][i]
    # Return all info of the oldest superheroes
    # Return all info of the oldest superheroes
    print(oldest)
    return oldest

# # returns info: Thor and Wonder Woman

def get_oldest_avenger(data):
    max=0
    for i in data["AVENGERS"]:
         if (data["AVENGERS"][i]['age'] >max):
            max=data["AVENGERS"][i]['age']
            print(max)
            oldest_avenger=data["AVENGERS"][i]
        # Return all info of the oldest avenger
    print(oldest_avenger)
    return oldest_avenger

# # returns info: Thor 


def get_total_points(data):
    total_points={}
    for i in data["AVENGERS"]:
        key=data["AVENGERS"][i]["name"]
        total_points[key] = 0
        for j in data["AVENGERS"][i]['points']:
            total_points[key]+=data["AVENGERS"][i]['points'][j]
    for i in data["DC"]:
        key=data["DC"][i]["name"]
        total_points[key] = 0
        for j in data["DC"][i]['points']:
            total_points[key]+=data["DC"][i]['points'][j]
    # Return a dictionary
    # Key: superhero name
    # Value: total points
    # print(type(total_points))
    print(total_points)
    return total_points

# # returns info: Dict of superhero name and total points

def get_more_than_average(data):
    more_than_average=[]
    avg_mcu=0
    avg_dc=0
    

    for i in data["AVENGERS"]:
        avg_mcu+=data["AVENGERS"][i]["points"]["stealth"]
    avg_mcu=avg_mcu/len(data["AVENGERS"])
    

    for i in data["AVENGERS"]:
        if(data["AVENGERS"][i]['points']['stealth']>avg_mcu):
            
            more_than_average+=data["AVENGERS"][i]
            

    for i in data["DC"]:
        avg_dc+=data["DC"][i]['points']['strength']
        avg_dc=avg_dc/len(data["DC"])

    for i in data["DC"]:
        if(data["DC"][i]['points']['strength']>avg_dc):
            
            more_than_average+=data["DC"][i]
            
            
    '''
    Return list of superheroes with stealth more than average in MCU 
    and list of superheroes with strength more than average in DCU
    '''
    print(more_than_average)
    return more_than_average

#returns info: Steve Rogers and Superman

def get_names(data):
    names=[]
    for i in data["AVENGERS"]:
        names.insert(-1,data["AVENGERS"][i]["name"])
    for j in data["DC"]:
        names.insert(-1,data["DC"][j]["name"])
    # Return a list of superhero names
    print(names)
    return names

# #returns a list 
