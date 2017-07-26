import re
a='1 - 2 * ( (60-30 +(-40*5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
mch = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', a)
while True:
    if not mch:
        break
    con=re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', a).group()
    print(con)
    if len(con.split('*')) > 1:
        n1,n2=con.split("*")
        value=float(n1) * float(n2)
    if len(con.split('/')) > 1:
        n1, n2 = con.split('/')
        value = float(n1) / float(n2)

    value= str(value)
    new_a = re.sub(con, value, a)
    print(new_a)
    before, nothing, after = re.split('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', new_a, 1)
    print(before,nothing,after)
    break