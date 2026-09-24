player_1=input()
player_2=input()

# while player_1== player_2:
#     print("gelijkspel")
#     player_1=input()
#     player_2=input()

if player_1== player_2:
    print("gelijkspel")
    
elif player_1=="Spock" and (player_2=="schaar" or player_2=="steen"):
    print("speler1 wint")
    
elif player_1=="schaar" and (player_2=="blad" or player_2=="hagedis"):
    print("speler1 wint")
    
elif player_1=="blad" and (player_2=="Spock" or player_2=="steen"):
    print("speler1 wint")
    
elif player_1=="steen" and (player_2=="hagedis" or player_2=="schaar"):
    print("speler1 wint")
    
elif player_1=="hagedis" and (player_2=="Spock" or player_2=="blad"):
    print("speler1 wint")
    
else:
    print("speler2 wint")