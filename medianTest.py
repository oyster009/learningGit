# medianTest.py

my_list = [0,1,2,3,4,5]

def median(input):
  length = len(input)
  oddTest = length%2
  if oddTest == 1:
    medLoc = (length // 2) + 1
    median = input[medLoc]
  elif oddTest == 0:
    medLoc1 = (length // 2)-1
    medLoc2 = length//2
    med1 = input[medLoc1]
    med2 = input[medLoc2]
    median = (med1 + med2)/2
  return median


for i in range(len(my_list)):
    print(my_list[i])

print("median of the list:")
print(median(my_list))