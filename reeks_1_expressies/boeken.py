total_price=0
unit_price=24.95
discount=0.4
sending_cost_init=3
sending_cost_multi=0.75

# aantal boeken is 60
amount=60

total_price= amount*unit_price*(1-discount)+(sending_cost_init+sending_cost_multi*(amount-1))
print(round(total_price,2))
