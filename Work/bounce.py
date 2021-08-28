# bounce.py
#
# Exercise 1.5
num = 1
distance =  100.0
while num <= 10:
    distance *= 0.6
    print(num, round(distance,4))
    num += 1
