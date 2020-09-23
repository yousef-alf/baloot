import math

totalhands = 10518300
def combinations(n,r):
    all_posibilities = float(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))
    return all_posibilities

def baloot_m():
    
    sira_frequency = combinations(4,1) * combinations(6,1) * combinations(29,5)
    sira = (sira_frequency / totalhands ) * 100
    print(sira)
    
    fifty_frequency = combinations(4,1) * combinations(5,1) * combinations(28,4)
    fifty = (fifty_frequency / totalhands ) * 100
    print(fifty)
    
    baloot_frequency = combinations(30, 6)
    baloot = (baloot_frequency / totalhands ) * 100
    print(baloot)
    
    one_hundred_series_frequency = combinations(4,1) * combinations(4,1) * combinations(27,3)
    one_hundred_series = (one_hundred_series_frequency / totalhands ) * 100
    print(one_hundred_series)
    
    one_hundred_photos_sun_frequency = combinations(4,1) * combinations(28,4)
    one_hundred_photos_sun = (one_hundred_photos_sun_frequency / totalhands ) * 100
    print(one_hundred_photos_sun)
    
    one_hundred_photos_hokom_frequency = combinations(5,1) * combinations(28,4)
    one_hundred_photos_hokom = (one_hundred_photos_hokom_frequency / totalhands ) * 100
    print(one_hundred_photos_hokom)
    
    one_hundred_sun = one_hundred_series + one_hundred_photos_sun
    print(one_hundred_sun)
    one_hundred_hokom = one_hundred_series + one_hundred_photos_hokom
    print(one_hundred_hokom)
    
    fourHundred = (4/32) * (3/31) * (2/30) * (1/29) * 100
    print(fourHundred)

baloot_m()
