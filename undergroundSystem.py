class UndergroundSystem:

    def __init__(self):
        self.checkI = {}
        self.route = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkI[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        rout = (self.checkI[id][0], stationName)
        if rout in self.route:
            self.route[rout][0] += t-self.checkI[id][1]
            self.route[rout][1] += 1
        else:
            self.route[rout] = [t-self.checkI[id][1], 1]
        del self.checkI[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        print(self.route[(startStation, endStation)][0] /
              self.route[(startStation, endStation)][1])


# Your UndergroundSystem object will be instantiated and called as such:
obj = UndergroundSystem()
obj.checkIn(22, "a", 3)
obj.checkOut(22, "b", 37)
obj.checkIn(27, "a", 5)
obj.checkOut(27, "b", 22)
obj.getAverageTime("a", "b")

# param_3 = obj.getAverageTime(startStation,endStation)
