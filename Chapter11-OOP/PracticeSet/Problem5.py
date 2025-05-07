# Write a class Train which has methods to book a ticket,get status(no of seats) and get fare information of train running under Indian Railways.

from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
    
    def getstatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(334, 7474)}")

t = Train(8965)
t.book("Puri", "Amritsar")
t.getstatus()
t.getFare("Puri", "Amritsar")
