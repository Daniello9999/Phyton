x = int(input(podaj pozycję gracza x:))
y = int(input(podaj pozycję gracza y:))

if x > 100 or y > 100 or x < 0 or y < 0:
    print("poza planszą")
elif x > 90 and y > 90:
    print ("prawy górny róg")
elif x > 90 and y < 10:
    print ("prawy dolny róg")
elif x < 10 and y < 10:
    print ("lewy dolny róg")
elif x < 10 and y > 90:
    print("lewy górny róg")
