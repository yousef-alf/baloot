import math
def Combinations(total,hands):
    all_posibilities = float(math.factorial(total) / (math.factorial(hands) * math.factorial(total - hands)))
    return all_posibilities

def Probability(frequency):
    posibilities = combinations(32,8)
    return (frequency / posibilities)

    
totalHands = Combinations(32, 8)
print (totalHands)
fourHundred = (4/32) * (3/31) * (2/30) * (1/29) 
print(fourHundred)
#oneHundredPhotosSun =
#oneHundredNumbersSun =
#oneHundredSun = 
#oneHundredPhotosHokom =
#oneHundredNumbersHokom =
#oneHundredSun = 
fifty = ((Combinations(5, 1) * Combinations(4,1))/ (total) )
fifty1= Combinations(5,1) * Combinations(4,1)
print(fifty1)
print(fifty) 
sira = ((Combinations(3, 1) * Combinations(4,1))/ (total) )
sira1= Combinations(3,1) * Combinations(4,1)
print(sira1)
print(sira)  
#baloot = 
