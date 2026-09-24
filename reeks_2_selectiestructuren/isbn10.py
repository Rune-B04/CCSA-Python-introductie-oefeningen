som = 0

for number in range(1,11):
    if number<10:
        som+=number*int(input())
    else:
        x10= int(input())
        if x10== som%11:
            print("OK")
        else:
            print("FOUT")