a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

#7al
g = int(input("Enter the value of g: "))
j = int(input("Enter the value of j: "))

print(f"{a}x + {b}y = {c}")
y = a  #k
x = -b  #k

s = f"{-b}k"  #x
d = f"{a}k"  #y

print(f"{a}x + {b}y - {a}*{g} - {b}*{j} = 0")
print(f"{a}(x - {g}) + {b}(y - {j}) = 0")

if g > 0 and j > 0:
  xf = f"{s}+{g}"
  yf = f"{d}+{j}"
elif g < 0 and j < 0:
  xf = f"{s} {g}"
  yf = f"{d} {j}"
elif g > 0 and j < 0:
  xf = f"{s}+{g}"
  yf = f"{d} {j}"
elif g < 0 and j > 0:
  xf = f"{s} {g}"
  yf = f"{d}+{j}"
elif g == 0 and j > 0:
  xf = f"{s}"
  yf = f"{d}+{j}"
elif g == 0 and j < 0:
  xf = f"{s}"
  yf = f"{d} {j}"
elif g > 0 and j == 0:
  xf = f"{s}+{g}"
  yf = f"{d}"
elif g < 0 and j == 0:
  xf = f"{s} {g}"
  yf = f"{d}"
elif g == 0 and j == 0:
  xf = f"{s}"
  yf = f"{d}"
else:
  # Additional conditions can be added based on specific requirements
  pass
print(f"x = {xf}")
print(f"y = {yf}")
