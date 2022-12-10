elfs = {}   # Setup dictionary to keep track of the
elfId = 1   # Keep track of elf id's

def GetTopTotals(numElfs):
    total = 0   # total to keep track of the combined values
    sortedElfs = sorted(elfs.items(), key=lambda item: item[1], reverse=True)
    x = 0
    while x < numElfs:
        elfId, elfTotal = sortedElfs[x]
        #print(elfId, elfTotal)
        total += elfTotal
        x += 1
    return total


with open("day1.data", 'r') as f:
    lines = len(f.readlines())
    f.seek(0,0)
    line = 0
    emptyLines = 0
    numberLines = 0
    currentTotal = 0
    while line < lines:
        data = f.readline().strip()
        # If we are dealing with a number
        if data.isdigit():
            currentTotal += int(data)
        
        # if we have an empty string, store the data, reset the counter
        if data == '':
            elfs[elfId] = currentTotal  # store this elf
            currentTotal = 0    # reset our total
            elfId += 1  # prepare the next elf id

        line += 1

highestElf = max(elfs.values())
numberElves = 3
topXTotal = GetTopTotals(numberElves)

print("The elf carry the most is carrying", highestElf, "calories!")
print("The combined value of the top (", numberElves, ") is", topXTotal)