heights = [154,177,203,164,172,169,166,164,166,188,192,201,163, 187,200,154]
for i in range(0,len(heights)):
  lowest = i
  for j in range(i+1,len(heights)):
    if heights[lowest] > heights[j]:
      lowest = j
  temp = heights[i]
  heights[i] = heights[lowest]
  heights[lowest] = temp

print(heights)

def max(list):
  maximum = 0
  for i in range (1,len(list)):
    if list[i] > list[maximum]:
      maximum = i
  return maximum

def swap(list, element1, element2):
  temp = list[element1]
  list[element1] = list[element2]
  list[element2] = temp

heights = [154,177,203,164,172,169,166,164,166,188,192,201,163, 187,200,154]
for i in range(0,len(heights)):
  tallest = max(heights[i:len(heights)])
  swap(heights, i, tallest+i)

print(heights)