#   ===== Weather Trend Analysis =====

''' import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10
fig_size[1] = 3
#import the data from Excel
def import_data(name):
    x=pd.read_excel(name)
    return x

#calculate the moving average
def moving_Average(dataframe):
    Glob_Moving_Avg=(dataframe.loc[:,'Global Temp']).rolling(window=20).mean()
    Milan_Moving_Avg=(dataframe.loc[:,'Milan temp']).rolling(window=20).mean()
    dataframe['Glob_Moving_Avg']=Glob_Moving_Avg
    dataframe['Milan_Moving_Avg']=Milan_Moving_Avg
    return dataframe
#draw the chart
def chart(datachart):
    chart=plt.plot(datachart.loc[:,'years'], datachart.loc[:,'Glob_Moving_Avg'],
                   datachart.loc[:,'years'],datachart.loc[:,'Milan_Moving_Avg']),
    plt.xticks(np.arange(1750, 2013, 25)),
    plt.yticks(np.arange(6, 10, 1)),
    plt.ylabel('Avg_temp (deg)',color='red'),
    plt.xlabel('period (years)',color='red'),
    plt.title('Annual_Temp (Milan VS Global)',color='red')
    return chart
#main function
def main():
     x=import_data('Table.xlsx')
     x=moving_Average(x)
     print(chart(x))
 '''

#   ===== Web Crawler ====

''' import requests
import time
from bs4 import BeautifulSoup

def continue_crawl(search_history,target_url,max_steps=25):
	if (search_history[-1]==target_url):
		print("We found the target page")
		print(search_history)
		return False, "Target Found"
	elif (len(search_history)>len(set(search_history))):
		print("We entered a loop")
		print(search_history)
		return False, "Infinite loop"
	elif (len(search_history)>max_steps):
		print("we exceeded n")
		print(search_history)
		return False, "Too much navigation"
	else:
		print("We're good to go")
		return True, "Still Processing"


def find_first_link(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text,'html.parser')
	content_div = soup.find(id="mw-content-text").find(class_='mw-parser-output')
	anchor = {}
	for tag in content_div.find_all("p",recursive=False):
		if tag.a:
			anchor = tag.find('a',recursive=False)
			break
	if (not(anchor == None)):
		anchor = anchor.get('href')
	print(anchor)
	if (anchor.find('en.wikipedia')>0):
		new_link = anchor
	else:
		new_link = "https://en.wikipedia.org" + anchor
	print(new_link)
	return new_link

def iniator():
	starting_link = ""
	while starting_link=="":
		response = requests.get("https://en.wikipedia.org/wiki/Special:Random")
		starting_link = response.url
	return starting_link

def main():
	target_url = "https://en.wikipedia.org/wiki/Philosophy"
	sample_size = eval(input("Please Enter Sample Size: "))
	boring_rate = eval(input("Please Enter Boring Limit: "))
	results = {}
	for i in range(sample_size):
		search_history = []
		search_history.append(iniator())
		print(search_history)
		flag, outcome = continue_crawl(search_history,target_url,boring_rate)
		while flag:
			first_link = find_first_link(search_history[-1])
			if (first_link == None):
				continue
			search_history.append(first_link)
			time.sleep(2)
			flag, outcome = continue_crawl(search_history,target_url,boring_rate)
		if (outcome in results):
			results[outcome]=results[outcome]+1
		else:
			results[outcome]=1
	total = 0
	for state in results:
		total+=results[state]
	for state in results:
		print(state,"=",(results[state]*100/total),"%")

main()
 '''
#   ====== CVRPTW =====
''' import random
from random import shuffle
import math
def main ():
    
    file=open("r101.txt","r")

    d=[]
    for line in file:
        x = line.split()
        d.append(x)
    dipo=customer(int(d[9][0]),int(d[9][1]),int(d[9][2]),int(d[9][3]),int(d[9][4]),int(d[9][5]),int(d[9][6]))
    d=d[10:]
    
    mylist=[]
    for i in (d):
        mylist.append(customer(int(i[0]),int(i[1]),int(i[2]),int(i[3]),int(i[4]),int(i[5]),int(i[6])))
    solutions=[]
    solution_id=0
    oldlist=[]
    for l in mylist:
        oldlist.append(l)
    for k in range(10):
        
        triplists=[]
        random.shuffle(mylist)
        listofnodes=[]
        nodes=[]              
        Dem=0
        trips=[]
        h=0
        for j in mylist :

            if Dem+j.Getdemand() > 200:
                h=h+dis
                trips.append(trip)     #(h,nodes)
                #trip.nodes=nodes
                Dem=j.Getdemand()
                listofnodes.append(nodes)
                nodes=[]
                nodes.append(j)
                dis=math.sqrt((35-j.Getx())**2+(35-j.Gety())**2)
                x=j.Getx()
                y=j.Gety()
                
            else :
                 if Dem < 1 :
                     dis=math.sqrt((35-j.Getx())**2+(35-j.Gety())**2)
                     x=j.Getx()
                     y=j.Gety()
                 else :
                     dis=dis+math.sqrt((x-j.Getx())**2+(y-j.Gety())**2)
                 nodes.append(j)
                 Dem=Dem+j.Getdemand()
             
        listofnodes.append(nodes)
        solution_id=solution_id+1
        solutions.append(solution(solution_id,listofnodes,len(listofnodes),h))
        
    random.shuffle(solutions)
    for s in range (1):
        q=solutions[s].gettrips()
        t=solutions[s+1].gettrips()
        q[0],t[0]=t[0],q[0]
        counter=0
        adding=[]
        w=[]
        for c in q :
            for v in c :
                w.append(v)
                
    for z in oldlist:
       if w.count(z)==0:
           adding.append(z)

    for o in range(0, len(adding)):
      for u in range(o+1, len(adding)):
        if adding[u].Getdemand() > adding[o].Getdemand():
            adding[u], adding[o] = adding[o], adding[u]
    
    
    for m in oldlist:
        for c in q:
            if m in c :
                counter=counter+1
            if counter>1 :
                c.remove(m)
                counter=1
                o=0
                Dema=0
                for v in c:    
                    Dema=Dema+v.Getdemand()
                    
        counter=0            
    #print(q)
    
    
class customer:
        name=0
        X=0
        Y=0
        Demand=0
        readytime=0
        duedate=0
        servicetime=0
        def __init__(self,name,x,y,Demand,readytime,duedate,servicetime):
            self.name=name
            self.x=x
            self.y=y
            self.Demand=Demand
            self.readytime=readytime
            self.duedate=duedate
            self.servicetime=servicetime
        def Getx(self):
            return (self.x)
        def Gety(self):
            return(self.y)
        def Getname(self):
            return(self.name)
        def Getdemand(self):
            return(self.Demand)
        def Getreadytime(self):
            return(self.readytime)
        def Getduedate(self):
            return(self.duedate)
        def Getservicetime(self):
            return(self.servicetime)
        def getDistance(self,dx,dy):
            dist = math.sqrt(((self.getx()-dx)**2) + ((self.gety()-dy)**2))
            return (dist)
        
class truck:
    truck_id=0
    capacity=200
    currentload=0
    tripdistance=0
    def __init__(self,truck_id,capacity,currentload,tripdistance):
        self.truck_id=truck_id
        self.capacity=capacity
        self.currentload=currentload
        self.tripdistance=tripdistance

class trip:
    trip_distance=0
    nodes=[]
    def __init__(self,trip_distance,nodes):
        self.trip_distance=trip_distance
        self.nodes=nodes
    
                
class solution:
    no_of_trips=0
    trips=0
    total_dis=0
    def __init__(self,solution_id,trips,no_of_trips,total_dis):
        self.trips=trips
        self.no_of_trips=no_of_trips
        self.total_dis=total_dis
        self.solution_id=solution_id
    def getsolution_id(self):
        return(self.solution_id)
    def gettrips(self):
        return(self.trips)
    def gettotal_dis(self):
        return(self.total_dis)
main()
 '''