
print("""

Welcome to the Rollercoaster!!!

""")

height = int(input("What's your height in cm?: "))
cost = 0

if height >= 120:
    print("Congrats you can ride the rollercoaster")
    age = int(input("How old are you?: "))
    if age < 12: 
        cost += 5
        print("Childs tickets cost $5")
    elif age <= 18:
        cost += 7
        print("Youth tickets cost $7")
    elif age >= 45 and age <= 55:
        cost = 0
        print("Older people ride for free")
    else:
        cost += 12
        print("Adults tickets costs $12")
        
    pictures = input("Do you want pictures? it costs $3. Y or N: ")
    if pictures == "Y" or pictures == "y":
        cost += 3
        print(f"Your total is {cost}$.")
    else:
        print(f"Your total is {cost}$.")
        
else:
    print("You have to grow taller if you want to ride the rollercoaster")
