import pandas as pd
import matplotlib.pyplot as plt

ud = pd.read_csv("unlabelled_data.csv")
ud.columns = ud.columns.str.replace("-1.885907518189583", "x").str.replace("-1.997407599218205", "y")   #Ta bort första raden helt för att skapa nya kolumnnamn

y = [-4, 4]
x = [-6, 6]   
plt.plot(x, y, marker = 'o')   #Plotta y och x, linjens ändar ska sluta med ett o

fy = [1 for x in range(-4, 4)]   #Beräkna avstånd från -4 till 4 och -6 till 6
fx = [1 for x in range(-6, 6)]   

kvärde = sum(fy)/ sum(fx)   #Dela summan av avstånden och spara i ny variabel

ud["0_or_1"] = ud["x"]   #Skapa ny spalt och kopiera in gamla x-spalten

for x, y in zip(ud["x"], ud["y"]):   #Slå ihop och loopa igenom x och y
    km = kvärde * x + 0    #
    if y < km:
        ud["0_or_1"] = ud["0_or_1"].replace(x, 0)   #Om y < km ändra elementet till 0, annars till 1
    else:
        ud["0_or_1"] = ud["0_or_1"].replace(x, 1)

#Skapa variablar för alla rader med värdet 0 och 1
noll = ud[ud["0_or_1"] == 0]   
ett = ud[ud["0_or_1"] == 1]   

ud.to_csv("labelled_data.csv", index = False)   #Skapa en ny fil men lägg inte till nya rader i filen

plt.scatter(noll["x"], noll["y"], color = "blue", label = "1")
plt.scatter(ett["x"], ett["y"], color = "green", label = "0")

plt.xlabel("X-axel")
plt.ylabel("Y-axel")
plt.title("Punkter")
plt.legend()   #
plt.grid()   #Lägg till rutnät 

plt.show()
