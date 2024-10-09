import pandas as pd
import matplotlib.pyplot as plt

ud = pd.read_csv("unlabelled_data.csv")
ud.columns = ud.columns.str.replace("-1.885907518189583", "x").str.replace("-1.997407599218205", "y")

y = [-4, 4]
x = [-6, 6]   
plt.plot(x, y, marker = 'o')
fy = [1 for x in range(-4, 4)]
fx = [1 for x in range(-6, 6)]

kvärde = sum(fy)/ sum(fx) 

ud["0 or 1"] = ud["x"]

for x, y in zip(ud["x"], ud["y"]):
    km = kvärde * x + 0
    if y < km:
        ud["0 or 1"] = ud["0 or 1"].replace(x, 0)
    else:
        ud["0 or 1"] = ud["0 or 1"].replace(x, 1)

noll = ud[ud["0 or 1"] == 0]
ett = ud[ud["0 or 1"] == 1]

#Skapa en ny fil, lägg inte in nya rader
ud.to_csv("labelled_data.csv", index = False)


plt.scatter(noll["x"], noll["y"], color = "blue", label = "1")
plt.scatter(ett["x"], ett["y"], color = "green", label = "0")

# Add labels and legend
plt.xlabel("X-axel")
plt.ylabel("Y-axel")
plt.title("Punkter")
plt.legend()
plt.grid()

# Show the plot
plt.show()
