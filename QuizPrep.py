import random
# 1
month_list = ["January", "June", "July"]

print(month_list)
# 2

joy_list = []
for i in range(700):
  joy_list.append("joy")
print(joy_list)

 
# 3
num_list = []
for i in range (0, 500):
  x = 7
  num_list.append(x)
print(num_list)

# 4
decimal_list = []
for i in range(0, 5000):
    x = random.randrange(0, 100)
    decimal_list.append(x)
print(decimal_list)

# 5
integer_list = []
for i in range(0, 300):
  integer_list.append(random.randrange(0, 40))
print(integer_list)
# 5(2)
integer_list = []
for i in range(0, 300):
  x = random.randrange(0, 40)
  integer_list.append(x)
print(integer_list)

# 6
multiple_list = []

for i in range(20, 801, 4):
  multiple_list.append(i)
print(multiple_list)

# 7
even_list = []
for i in range(100, 9, -2):
    even_list.append(i)
print(even_list)

# 7 (Alternative)
even_list = []
for i in range(10, 101, 2):
    even_list.append(i)
    reverse_list = even_list[::-1]
print(reverse_list)

# 8
color_list = "red,orange,yellow,green,blue,indigo,violet"
color = color_list.split(",")
print("\n",color)

# 9
city_list = "Edmonton;Calgary;Vancouver;Saskatoon;Winnipeg"
city = city_list.split(";")
print("\n",city)


# 10 App and more polished to use version
loop = True
name_list = []
while loop:
  # Add Name
  print("\n Add Name Menu")
  print("1: Add Name To List")
  print("2: Exit The Loop")

  selection = input("Enter Selection (1-2): ")

  if selection == "1":
     add_name = input("\nAdd a name to the list: ")
     name_list.append(add_name.capitalize())
     print(name_list)
  elif selection == "2":
    exit = input("Type done to exit: ")
  if exit == "done": 
     loop = False

# 10 Alternative
#loop = True
#name_list = []
#while loop:
#   selection = input("Enter a name to add the array and type 'done' to exit program: ")
#   if selection.capitalize() == "Done":
#        loop = False
#        print(name_list)
#    else:
#        name_list.append(selection.capitalize())