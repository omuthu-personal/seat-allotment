#!/usr/bin/python
import seat_allotment as sa
import unittest

class TestSeatAllotment(unittest.TestCase):

    def setUp(self):
        pass

    def testAisleSeats(self):
        print("Testing Aisle Seats...")
        seatMap=[ [3,2], [4,3], [2,3], [3,4] ]
        sa.classifySeats(seatMap)
        aisleSeats = [[0, 0, 2], [0, 1, 2], [1, 0, 0], [1, 0, 3], [1, 1, 0], [1, 1, 3], [1, 2, 0], [1, 2, 3], [2, 0, 0], [2, 0, 1], [2, 1, 0], [2, 1, 1], [2, 2, 0], [2, 2, 1], [3, 0, 0], [3, 1, 0], [3, 2, 0], [3, 3, 0]]

        self.assertEqual(sa.getAisleSeats(seatMap),aisleSeats,"Incorrect AisleSeats")
        print("Identified Aisle seats correctly...")

    def testWindowSeats(self):
        print("Testing Window Seats...")
        seatMap=[ [3,2], [4,3], [2,3], [3,4] ]
        sa.classifySeats(seatMap)
        windowSeats = [[0, 0, 0], [0, 1, 0], [3, 0, 2], [3, 1, 2], [3, 2, 2], [3, 3, 2]]

        self.assertEqual(sa.getWindowSeats(seatMap),windowSeats,"Incorrect WindowSeats")
        print("Identified Window seats correctly...")

    def testCenterSeats(self):
        print("Testing Center Seats...")
        seatMap=[ [3,2], [4,3], [2,3], [3,4] ]
        sa.classifySeats(seatMap)
        centerSeats = [[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 2, 2], [3, 0, 1], [3, 1, 1], [3, 2, 1], [3, 3, 1]]

        self.assertEqual(sa.getCenterSeats(seatMap),centerSeats,"Incorrect CenterSeats")
        print("Identified Center seats correctly...")

    def testSeatPosition(self):
        print("Testing Seat Position...")
        seatMap=[ [3,2], [4,3], [2,3], [3,4] ]
        passengerCount = 30
        passengerId = 25
        seatPosition = [0, 0 , 1]
        sa.classifySeats(seatMap)
        sa.allocateSeats(passengersCount)

        self.assertEqual(sa.getSeatPosition(passengerId),seatPosition,"Incorrect Seat Allocated")
        print("Seat position correctly allocated for passenger :", passengerId)

if __name__ == "__main__":
    passengersCount=30

    unittest.main()
