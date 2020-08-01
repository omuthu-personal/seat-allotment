#!/usr/bin/python
import numpy as np
import pandas as pd

passengersCount=30
seats=[]
seatMap=[ [3,2], [4,3], [2,3], [3,4] ]
aisleSeats=[]
windowSeats=[]
centerSeats=[]
firstColumn=0
firstBay=0
lastBay=len(seatMap)-1
printSeats=[]

def allocateSeats():

    seatCount = len(aisleSeats) + len(windowSeats) + len(centerSeats)
    for p in range(passengersCount):
        if p < seatCount:
            seat = seats[p]
            print ('seat :', seat)
            bay = seat[0]
            row = seat[1]
            col = seat[2]
            printSeats[bay][row][col] = p+1
        else:
            break
        
def printToHtml():
	tableStyle="""
	<style>
	table {
	  float: left;
	  margin-right:10px;
	}
	</style>
	"""
	finalHtml = tableStyle
	for bay in printSeats:
	    num = np.array(bay)
	    df = pd.DataFrame(num)
	    html = df.to_html(index=False, header=False)
	    finalHtml += html
	
	f = open("output.html", "w")
	f.write(finalHtml)
	f.close()
    
for idx, bay in enumerate(seatMap, start=0):
  cols=bay[0]
  rows=bay[1]
  printSeats.insert(idx, []) #Create each bay for printing
  for row in range(0, rows):
    printSeats[idx].insert(row, []) #Create row in each bay for printing
    for col in range(0, cols):
        printSeats[idx][row].insert(col, None)
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


#Row wise sorting
seats.extend((sorted(aisleSeats,key=lambda x: (x[1]))))
seats.extend((sorted(windowSeats,key=lambda x: (x[1]))))
seats.extend((sorted(centerSeats,key=lambda x: (x[1]))))

print(seats)
print(printSeats)
allocateSeats()
printToHtml()
