#!/usr/bin/python
import numpy as np
import pandas as pd

seats=[]
aisleSeats=[]
windowSeats=[]
centerSeats=[]
freeSeats=[]

### Functions for test cases ###

def getAisleSeats(seatMap):
    
    return aisleSeats

def getWindowSeats(seatMap):
    
    return windowSeats

def getCenterSeats(seatMap):
    
    return centerSeats

################################

def allocateSeats(passengersCount):

    seatCount = len(aisleSeats) + len(windowSeats) + len(centerSeats)
    for p in range(passengersCount):
        if p < seatCount:
            seat = seats[p]
            bay = seat[0]
            row = seat[1]
            col = seat[2]
            freeSeats[bay][row][col] = p+1
        else:
            break
        
def printToHtml(fileName):
    tableStyle="""
    <style>
    table {
      float: left;
      margin-right:10px;
    }
    </style>
    """
    finalHtml = tableStyle
    for bay in freeSeats:
        num = np.array(bay)
        df = pd.DataFrame(num)
        html = df.to_html(index=False, header=False)
        finalHtml += html
    
    f = open(fileName, "w")
    f.write(finalHtml)
    f.close()

def classifySeats(seatMap):
    global seats, aisleSeats, windowSeats, centerSeats, freeSeats
    seats=[]
    aisleSeats=[]
    windowSeats=[]
    centerSeats=[]
    freeSeats=[]
    firstColumn = 0
    firstBay = 0
    lastBay = len(seatMap) - 1
    for idx, bay in enumerate(seatMap, start=0):
      cols=bay[0]
      rows=bay[1]
      freeSeats.insert(idx, []) #Create each bay
      for row in range(0, rows):
        freeSeats[idx].insert(row, []) #Create row in each bay
        for col in range(0, cols):
            freeSeats[idx][row].insert(col, None)
            if col == firstColumn: # First column in bay
                if idx == firstBay:
                    windowSeats.insert(row, [idx, row, col])
                elif idx == lastBay:
                    if col == (cols-1): # Single seater last bay
                        windowSeats.append([idx, row, col])
                    else:
                        aisleSeats.append([idx, row, col])
                else: 
                    aisleSeats.append([idx, row, col])
            else: # Not first column
                if col == (cols-1): #Last column in bay
                    if idx == lastBay:
                        windowSeats.append([idx, row, col])
                    else: 
                        aisleSeats.append([idx, row, col])
                else: #This is Middle seat, first seat is handled in previous if condition
                    centerSeats.append([idx, row, col])


    #Row wise sorting of each type seats to meet row wise filling requirement and append sorted data to seats
    seats.extend((sorted(aisleSeats,key=lambda x: (x[1])))) # First Aisle has to be filled
    seats.extend((sorted(windowSeats,key=lambda x: (x[1])))) # Second, window seats
    seats.extend((sorted(centerSeats,key=lambda x: (x[1])))) # Third center seats

######################### Main #########################

if __name__ == "__main__":
    passengersCount=30
    seatMap=[ [3,2], [4,3], [2,3], [3,4] ]
    
    classifySeats(seatMap)
    allocateSeats(passengersCount)
    printToHtml("output.html")
    
