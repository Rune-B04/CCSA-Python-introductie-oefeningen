amount_products=int(input())
unit_price=float(input())
amount_barcodes_req=int(input())
miles_per_coupon=int(input())

money_spent=float(amount_products*unit_price)
amount_coupons=amount_products//amount_barcodes_req
total_miles=int(miles_per_coupon*amount_coupons)

print(f"Phillips spendeerde ${money_spent} voor {total_miles} frequent flyer mijlen. ")

