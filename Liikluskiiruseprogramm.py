#max_speedlimit = 30

name = input("Sisesta oma nimi:")
kiirus = int(input("Sisesta lubatud kiirus (km/h):"))
crossed = int(input("Sisesta tegelik kiirus (km/h):"))
trahv = (crossed - kiirus) * 3
trahv = min(190, trahv)

hoiatustrahv = name + ", kiiruse ületamise eest on teie trahv " + str(trahv) + " eurot."

print(hoiatustrahv)
#if input("Sisesta lubatud kiirus (km/h):") < input("Sisesta tegelik kiirus (km/h):"):
    #trahv = crossed - kiirus

#if input("Sisesta lubatud kiirus (km/h):") < input("Sisesta tegelik kiirus (km/h):"):
    #print(name, "Kiiruse ületamise eest on teie trahv " + trahv + " eurot")

#if trahv < 190:
    #print("190")

#name = input('Enter your name:')
#print ('Hello'), name.
#hours = float(input('Enter Hours:'))
#rate = float(input('Enter Rate:'))
#pay = hours * rate.
#print ('Pay ='), pay.
#celsius = float(input('Enter degrees in Celsius:'))