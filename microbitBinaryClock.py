import microbit, time

def decToBin(n):
    return int(bin(n)[2:])

hour1 = 1
hour2 = 8
minute1 = 4
minute2 = 0

'''while not microbit.button_b.was_pressed:
    if microbit.button_a.is_pressed:
        minute2 += 1

    if minute2 > 9:
        minute2 = 0
        minute1 += 1

    if minute1 > 5:
        hour2 +=1

    if hour2 > 9:
        hour2 = 0
        #hour1 += 1

    if hour1 > 1 and hour2 > 3:
        hour1 = 0
        hour2 = 0

    hourBin1 = str(decToBin(int(hour1)))
    hourBin2 = str(decToBin(int(hour2)))

    minuteBin1 = str(decToBin(int(minute1)))
    minuteBin2 = str(decToBin(int(minute1)))
    
    while len(hourBin1) < 5:
        hourBin1 = '0' + hourBin1

    while len(hourBin2) < 5:
        hourBin2 = '0' + hourBin2

    while len(minuteBin1) < 5:
        minuteBin1 = '0' + minuteBin1

    while len(minuteBin2) < 5:
        minuteBin2 = '0' + minuteBin2

    timeImage = hourBin1 + ':' + hourBin2 + ':00000:' + minuteBin1 + ':' + minuteBin2
    timeImage = microbit.Image(timeImage)
    microbit.display.show(timeImage)'''

while True:

    hourBin1 = str(decToBin(int(hour1)))
    hourBin2 = str(decToBin(int(hour2)))
        
    minuteBin1 = str(decToBin(int(minute1)))
    minuteBin2 = str(decToBin(int(minute2)))
        
    while len(hourBin1) < 5:
        hourBin1 = '0' + hourBin1
        
    while len(hourBin2) < 5:
        hourBin2 = '0' + hourBin2
        
    while len(minuteBin1) < 5:
        minuteBin1 = '0' + minuteBin1
        
    while len(minuteBin2) < 5:
        minuteBin2 = '0' + minuteBin2

    timeImage = hourBin1 + ':' + hourBin2 + ':00000:' + minuteBin1 + ':' + minuteBin2
    timeImage = microbit.Image(timeImage)
    microbit.display.show(timeImage)
    
    minute2 += 1
    
    if minute1 > 5:
        hour2 +=1

    if minute2 > 9:
        minute2 = 0
        minute1 += 1

    if hour1 > 1 and hour2 > 3:
        hour1 = 0
        hour2 = 0

    if hour2 > 9:
        hour2 = 0
        hour1 += 1

    time.sleep(60)