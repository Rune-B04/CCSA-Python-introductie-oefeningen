import math
a=float(input())
b=float(input())
c=float(input())

det=(b**2)-4*a*c

if det<0:
    print("geen wortels")
    
elif det==0:
    print("een wortel")
    root=-b/(2*a)
    print((root))
elif det>0:
    print("twee wortels")
    root1,root2= (-b-math.sqrt(det))/(2*a),(-b+math.sqrt(det))/(2*a)
    if root1>root2:
        print(f"{(root2)}\n{(root1)}")
    else:
        print(f"{(root1)}\n{(root2)}")
        
        
# GEEN ROUND GEBRUIKEN