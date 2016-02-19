# Max Wagner

class CarEvaluation:
    carCount = 0

    def __init__(self, brand, price, safetyRating):
        self.brand = brand
        self.price = price
        self.safetyRating = safetyRating
        CarEvaluation.carCount += 1

    def __repr__(self):
        return self.brand

    def showEvaluation(self):
        print "The %s has a %s price and its safety is rated a %d." % (self.brand, self.price, self.safetyRating)

    def priceSort(self):
        if self.price == "Low":
            return 0
        elif self.price == "Med":
            return 1
        elif self.price == "High":
            return 2

def sortbyprice(L, order = 'des'):
    if order == 'asc':
        return sorted(L, key=CarEvaluation.priceSort)
    elif order == 'des':
        return sorted(L, key=CarEvaluation.priceSort, reverse=True)

def searchforsafety(L, rating):
    for car in L:
        if car.safetyRating == rating:
            return True
    return False

# This is the main of the program.  Expected outputs are in comments after the function calls.
if __name__ == "__main__":
    eval1 = CarEvaluation("Ford", "High", 2)
    eval2 = CarEvaluation("GMC", "Med", 4)
    eval3 = CarEvaluation("Toyota", "Low", 3)

    print "Car Count = %d" % CarEvaluation.carCount # Car Count = 3

    eval1.showEvaluation() #The Ford has a High price and it's safety is rated a 2
    eval2.showEvaluation() #The GMC has a Med price and it's safety is rated a 4
    eval3.showEvaluation() #The Toyota has a Low price and it's safety is rated a 3

    L = [eval1, eval2, eval3]

    print sortbyprice(L, "asc"); #[Toyota, GMC, Ford]
    print sortbyprice(L, "des"); #[Ford, GMC, Toyota]
    print searchforsafety(L, 2); #true
    print searchforsafety(L, 1); #false