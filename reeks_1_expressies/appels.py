crate_size=20
pallet_size=35

apples=int(input())

crates=apples//crate_size
pallets=crates//pallet_size

apples_rem=apples%crate_size
crates_rem=crates%pallet_size

print(f"{pallets}\n{crates_rem}\n{apples_rem}")

