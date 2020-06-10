rotation = int(input('please enter rotation:'))
longitude = float(input('please enter longitude:'))
timeDifference = (rotation * longitude) / 360
hours = int(timeDifference)
minutes = int((((timeDifference * 100) % 100) * 60) / 100)
hourAngle = hours * 30.0
minutesAngle = minutes * 6.0
displacement = minutes * 0.5
hourAngle = hourAngle + displacement
if(hourAngle>minutesAngle):
    resultangle = hourAngle - minutesAngle
else:
    resultangle =minutesAngle-hourAngle
tempAngle=360-resultangle
if resultangle<tempAngle:
    print(resultangle)
else:
    print(tempAngle)
