start_hour = int(input())
start_minute = int(input())
stop_hour = int(input())
stop_minute = int(input())

start = start_hour * 60 + start_minute
stop = stop_hour * 60 + stop_minute

if stop_hour == 0 and stop_minute == 0:
    stop = 24 * 60

if start < 18 * 60 or stop > 24 * 60 or stop <= start:
    print("ongeldige invoer")

else:
    if start < 21 * 60 + 30:
        if stop <= 21 * 60 + 30:
            bedrag = (stop - start) / 60 * 2

        else:
            bedrag = ((21 * 60 + 30) - start) / 60 * 2
            bedrag = bedrag + (stop - (21 * 60 + 30)) / 60 * 4

    else:
        bedrag = (stop - start) / 60 * 4

    print(bedrag)