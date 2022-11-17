results = ["Yes", "Yes", "No", "No", "Maybe", "Maybe", "Yes", "No", "Maybe", "Yes"]

yes = 0
no = 0
maybe = 0

for i in results:
    if i == "Yes":
        yes += 1
    elif i == "No":
        no += 1
    else:
        maybe += 1

print("Yes =", yes)
print("No =", no)
print("Maybe =", maybe)

ages = [1, 5, 20, 70, 16, 18, 25, 0.5, 40]

over_18 = 0
below_18 = 0

for i in ages:
    if i < 18:
        below_18 += 1
    else: 
      over_18 += 1

print("\nNumber of people who are or is over 18 =", over_18)
print("Number of people below 18 =", below_18)

prices = [1, 20, 37, 4.59, 69, 42, 54, 37, 53, 7.27]
below_20 = 0
from_20_49 = 0
above_or_50 = 0
for i in prices:
    if i < 20:
        below_20 += 1
    elif i >= 20 and i <= 49:
         from_20_49 += 1
    elif i >= 50:
         above_or_50 += 1

print("\n",prices)
print("\nBelow 20 dollars =", below_20, "from 20-49 =", from_20_49, "Items above 50 =", above_or_50)

prices_B = prices
for i in range(len(prices)):
    prices_B[i] = prices[i] + 2

print("\n", prices_B)

prices_C = prices
for i in range(len(prices)):
    prices_C[i] = prices[i] * 1.05
print(prices_C)

prices_D = prices
for i in range(len(prices)):
    prices_D[i] = prices[i] * 0.80

print(prices_D)







