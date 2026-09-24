state_1=input()
state_2=input()
vals=0

if state_1=="links": #4-5-6 vals
    if state_2=="links":
        vals=5
        
    elif state_2=="rechts":
        vals=4
    
    elif state_2=="evenwicht":
        vals=6    
    
elif state_1=="rechts": #1-2-3 vals
    if state_2=="links":
        vals=2
            
    elif state_2=="rechts":
        vals=1
        
    elif state_2=="evenwicht":
        vals=3    

elif state_1=="evenwicht": #7-8-9 vals
    if state_2=="links":
        vals=8
            
    elif state_2=="rechts":
        vals=7
        
    elif state_2=="evenwicht":
        vals=9
    
else:
    print("fout")
    
print(f"muntstuk #{vals} is vervalst")

    
