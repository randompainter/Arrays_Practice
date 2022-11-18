#Python Functions Assignment

#Global Variables
test = [2, 4, 6, 8, 10]

# Contains
def contains(list, i):
  for el in list:
    if el == i:
      # Return index of desired item
      return True

  # Return if item not found
  return False
    
    

if contains(test, 4):
    print("\n4 is in the list")
else:
    print("4 is not found in the list")

#IndexOf

def indexOf(list, i):
  # Loop through list and search for the first occurrence of the item
  for index in range(len(list)):
    if list[index] == i:
      # Return index of desired item
      return index

  # Return if item not found
  return -1

idx = indexOf(test, 8)

if idx != -1:
  print("\n8 was found at index", str(idx))
else:
  print("\n8 was not found in the list")
  
#Reverse
def reverse(list):
    x = []
    for i in range(len(list)-1, -1, -1):
      x.append(list[i])
    return x

    
reversed = reverse(test)
print("\nOriginal List", test)
print("Reversed List", reversed)

#def reverse2(x):
#  return x[::-1]

#reversed = reverse2(test)
#print("\nOriginal list: ", test)
#print("\nReversed list: ", reversed)
  
#Swap
def swapPos(lis, pos1, pos2):
  lis[pos1], lis[pos2] = lis[pos2], lis[pos1]

print("\n2 and 10 shall be swapped", test)
swapped = test
swapPos(swapped, 0, 4)
print("2 and 10 have been swapped", swapped)

#IndexOfMin
def indexOfMin(list):
    x = len(list)
    min_value = list[0]
    min_index = 0
 
    for i in range(1, x):
      if list[i] < min_value:
        min_value = list[i]
        min_index = i

    return min_index
 #   return min_value
     

tested = indexOfMin(test)
print("\nCurrent List", test)
print("The Index of the smallest value in the list is at", tested)