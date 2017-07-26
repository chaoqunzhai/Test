age_old=56
conn = 0
while conn < 3:
    gee=input("age>>:")
    if gee.isdigit():
        gee = int(gee)
    else:
        continue
    if gee==age_old:
        print("good")
        break
    elif gee > age_old:
        print("big")
    else:
        print("xiao")
        conn += 1