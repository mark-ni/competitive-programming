from sys import stdin
from collections import deque, defaultdict
input=stdin.readline

D,I,S,V,F=map(int,input().split())

#setup intersections
intersections = [deque() for i in range(I)]
currLights = [0]*I      #For each intersection, the street # of the current
                        #light that is green
Cycles=[0]*I

iIns=[deque()]*I        #The list of streets going into an intersection
iOuts=[deque()]*I       #The list of streets going out of an intersection

#setup streets
#streetsStart = [-1]*S   #A list of intersections where each street starts
streetsEnd = [-1]*S     #A list of intersections where each street ends
streetTimes = [0]*S     #A list of required time to cross each street
streetNames = {}
carsOnStreet= [deque() for i in range(S)] #List of cars stopped at current street end
filledStreets=[False]*S #Whether a car has driven down this street at time t already

for i in range(S):
    B,E,name,L=list(input().rstrip().split())
    B,E,L=int(B),int(E),int(L)

    #streetsStart[i] = B
    streetsEnd[i] = E
    iIns[E].append(i)
    iOuts[B].append(i)
    streetTimes[i] = L
    streetNames[name] = i

#setup cars
carPaths=[0]*V      #List of streets the car must drive down
carPathLen=[0]*V    #length of the car's path
carPos=[0]*V        #current stop along the path
timeQueue=[deque() for i in range(2*D+5)]

for i in range(V):
    path=list(input().rstrip().split())
    carPathLen[i]=int(path[0])
    carPaths[i] = [streetNames[j] for j in path[1:]]
    carsOnStreet[carPaths[i][0]].append(i)
    carPos[i] = 0
    timeQueue[0].append(i)

#################################################################
#################################################################
#################################################################
#################################################################

#SETUP CYCLES - MODIFY THIS TO TEST OUTPUTS

#################################################################
#################################################################
#################################################################
#################################################################

for i in range(I):
    Cycles[i] = list(iIns[i])
    # For example, 0 -> [0,0,1,1,1,1,2], 1->[1,2,3] etc.

#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################


#main loop
tot = 0
for t in range(D):
    filledStreets=[False]*S
    for i in range(I):
        currLights[i] = Cycles[i][t % len(Cycles[i])]
    while len(timeQueue[t]) > 0:
        car=timeQueue[t].popleft()
        street=carPaths[car][carPos[car]]
        print(street)
        #Car does not move

        #Car is not at front of line
        if carsOnStreet[street][0] != car:
            timeQueue[t+1].append(car)
        #Light is red
        if not currLights[streetsEnd[street]] == street:
            timeQueue[t+1].append(car)
        #Street ahead is being driven down
        elif filledStreets[carPaths[car][carPos[car] + 1]]:
            timeQueue[t+1].append(car)
        #Car moves forward to next intersection
        else:
            carsOnStreet[street].popleft()
            carPos[car] += 1
            if carPos[car] == carPathLen[car] - 1:
                if t + streetTimes[carPos[car]] <= D:
                    tot += F + D - t
            else:
                street = carPaths[car][carPos[car]]
                carsOnStreet[street].append(car)
                timeQueue[t + streetTimes[street]].append(car)
print(tot)
            
        
    

