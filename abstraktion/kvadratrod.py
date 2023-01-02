def intSquareroot(x):
  root = 0
  while (root*root) <= x:
    root = root + 1
  #root er det mindste tal større end heltalskvadratroden af x
  return (root - 1)

print(intSquareroot(0))

print(intSquareroot(4))

print(intSquareroot(3.5))