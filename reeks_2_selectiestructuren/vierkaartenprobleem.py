face=input()
value=input()
turn=input()
even=False
rood=False

if face=="kleur":
    rood=value=="rood"
    if not rood:
        if turn=="ja":
            print(f"Juist: kaarten met {face} {value} moeten gedraaid worden.")
        elif turn=="nee":
            print(f"Fout: kaarten met {face} {value} moeten gedraaid worden.")
                    
    elif rood:
        if turn=="ja":
            print(f"Fout: kaarten met {face} {value} moeten niet gedraaid worden.")

        elif turn=="nee":
            print(f"Juist: kaarten met {face} {value} moeten niet gedraaid worden.")
            
elif face=="waarde":
    even=int(value)%2==0
    if even:
        if turn=="ja":
            print(f"Juist: kaarten met {face} {value} moeten gedraaid worden.")     
        elif turn=="nee":
            print(f"Fout: kaarten met {face} {value} moeten gedraaid worden.")
            
    elif not even:
        if turn=="ja":
            print(f"Fout: kaarten met {face} {value} moeten niet gedraaid worden.")
        elif turn=="nee":
            print(f"Juist: kaarten met {face} {value} moeten niet gedraaid worden.")
            
else:
    print("fout")