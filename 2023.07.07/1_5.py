mile = input("введи целую милю: ")
ml = input("введи дробную милю: ")
kmMl = round(int(ml)/10)
print(f"{mile}.{ml} ml = {round((int(mile))/0.6214)+kmMl}.{round(int(ml)/0.6214)} km")