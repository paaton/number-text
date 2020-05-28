bigger = "dvacet"
lower = "jedna"
values_bigger = ["dvacet", "třicet", "čtyřicet", "padesát","šedesát", "sedmdesát", "osmdesát", "devadesát" ]
values_lower = ["jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
problematics = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
f = open("C:/Users/motherfucker/Source/Repos/git/number-text/output.txt", "w")


for y in range(9):
    f.write(values_lower[y] + "\n")
for a in range(10):
    f.write(problematics[a] + "\n")
for i in range(8):
    f.write(values_bigger[i] + "\n")
    for x in range(9):
        f.write(values_bigger[i] + values_lower[x] + "\n")
f.write("sto")
print("done")