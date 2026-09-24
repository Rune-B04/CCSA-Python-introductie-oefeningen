x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

x3 = int(input())
y3 = int(input())
x4 = int(input())
y4 = int(input())

# Grenzen van rechthoek 1
if x1 < x2:
    links1 = x1
    rechts1 = x2
else:
    links1 = x2
    rechts1 = x1

if y1 < y2:
    onder1 = y1
    boven1 = y2
else:
    onder1 = y2
    boven1 = y1

# Grenzen van rechthoek 2
if x3 < x4:
    links2 = x3
    rechts2 = x4
else:
    links2 = x4
    rechts2 = x3

if y3 < y4:
    onder2 = y3
    boven2 = y4
else:
    onder2 = y4
    boven2 = y3

# Controle op botsing
if rechts1 <= links2 or rechts2 <= links1 or boven1 <= onder2 or boven2 <= onder1:
    print("geen botsing")
else:
    print("botsing")