suv = int(input("Jumlah SUV adalah: "))
category = ""

if suv < 20 and suv > 0:
    category = "Demo"
elif suv >= 20 and suv <= 80:
    category = "Non Exclusive"
elif suv > 80:
    category = "Exclusive"
else:
    print("Invalid input")
    exit()

print("Kategori GoScreen adalah " + category)
