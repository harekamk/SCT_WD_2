#a bus travels in a circular path, fare is calculated between input source and destination stop. if d=1000m, fare=5 INR, the fare should be rounded off
#path=[800,600,750,900,1400,1200,1100,1500]
#THANERAILWAYSTN=TH
#GAONDEVI=G
#ICEFACTROY=IC
#HARINIWASCIRCLE=HA
#NITINCOMPANYJUNCTION=NI
#CADBURRYJUNCTION=CA
#LUISWADI=LU
#TEENHATHNAKA=TE
#BusStops=["TH","GA","IC","HA","NI","CA","LU","TE"]

import math

def getFare(source,destination):
    route=[["TH","GA","IC","HA","NI","CA","LU","TE"],[800,600,750,900,1400,1200,1100,1500]]

    fare=0.0

    if not(source in route[0] and destination in route[0]):
        print("Invalid input")
    if route[0].index(source)<route[0].index(destination):
        for i in range(route[0].index(source)<route[0].index(destination)):
            fare+=route[1][i]

    elif route[0].index(destination)<route[0].index(source):
        for i in range(route[0].index(source)+1,len(route[0])):
            fare+=route[1][i]
        for i in range(0,route[0].index(destination)+1):
            fare+=route[1][i]

    return float(math.ceil(fare*0.005))

source=input("Enter source station:")
destination=input("Enter destination station:")
fare=getFare(source,destination)
if fare==0:
    print("Invalid input")
else:
    print(fare)

        
    
    
        