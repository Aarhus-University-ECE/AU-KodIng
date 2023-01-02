# funktioner til beregninger på kube
# height, width og depth er alle i cm

 WEIGHT_PER_CM3 = 2 # vægt i g

def getSurfaceArea(height, width, depth):
  side1 = width * height
  side2 = width * depth
  side3 = depth * height
  total = (side1 + side1 + side3) * 2
  return total

def getVolume(height, width, depth):
 return width * height * depth

# vægten i kilo returneres
def getWeight(height, width, depth):
 return (getVolume(height, width, depth) * WEIGHT_PER_CM3) / 1000
 
# test af kube funktioner givet en kube på 2cm * 3cm * 4cm
print("expected surface area: 52 cm2, got",getSurfaceArea(2,3,4), "cm2")
print("expected volume: 24 cm3, got",getVolume(2,3,4), "cm3")
print("expected weight: 0,048 kg, got",getWeight(2,3,4),"kg")

# funktioner til beregning på en palle med kuber
BASE_WEIGHT = 6.5  # in kg
BASE_HEIGHT = 15;  # in cm

# vægten af pallen med kuber returneres i kg
def getPalletWeight(bricksInPlane,height):
  numberOfBricks = bricksInPlane * countInHeight
  return getWeight(height, width, depth) * numberOfBricks

#   højden på pallen returneres i cm
def getHeight(height,countInHeight):
  return height % countInHeight + BASE_HEIGHT

# test af palle funktioner givet en palle med 6 lag af 16 kuber på 8*20*12   
bricksInPlane = 16 # antal kuber pr lag
countInHeight = 6 # antal lag på pallen
height = 8 # højde på kube
width = 20 # bredde på kube
depth = 12 # dybde af kube

print("expected weight of new kube: 3.84 kg, got",getWeight(height,width,depth),"kg")
print("expected height of pallet: 63 cm, got", getHeight(height,countInHeight),"cm")
print("expected weight of pallet: 375,14 kg, got", getPalletWeight(bricksInPlane,height),"kg")