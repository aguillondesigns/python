ages = {'Leo':15, 'Livier':19, 'Bolis':10}
highScore = max(ages.values())
highUser = max(ages, key=ages.get)
print(str(highUser) + ":" + str(highScore))