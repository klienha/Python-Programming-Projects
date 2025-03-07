print("Sage's Wedding Cake Price Calculator")
people = int(input("Total People Attending: "))
print("----------------------------------------")
print("Cake A")
costA = (15*15) + (1*12.50) 
laborA = costA/30 #calculating cost per person based on a cake that feeds 30 people
laborTotal = laborA * people
print("Labor Cost:     \t$" + str(round(laborTotal, 2)))
costA += 35
make = costA/30
makeTotal = make * people
print("Cost to Make:   \t$" + str(round(makeTotal, 2)))
costA += (costA * .1)
costA = costA/30
totalA = costA * people
print("Charge Customer: \t$" + str(round(totalA, 2)))
print("----------------------------------------")
print("Cake B")
costB = (14*15) + (2*12.50) 
laborB = costB/30
laborTotal = laborB * people
print("Labor Cost:     \t$" + str(round(laborTotal, 2)))
costB += 30
make = costB/30
makeTotal = make * people
print("Cost to Make:   \t$" + str(round(makeTotal, 2)))
costB += (costB * .1)
costB = costB/30
totalB = costB * people
print("Charge Customer: \t$" + str(round(totalB, 2)))
print("----------------------------------------")
print("Cake C")
costC = (16*15) + (1.5*12.50) 
laborC = costC/30
laborTotal = laborC * people
print("Labor Cost:     \t$" + str(round(laborTotal, 2)))
costC += 40
make = costC/30
makeTotal = make * people
print("Cost to Make:   \t$" + str(round(makeTotal, 2)))
costC += (costC * .1)
costC = costC/30
totalC = costC * people
print("Charge Customer: \t$" + str(round(totalC, 2)))
