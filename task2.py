"""
def f21(a):
    if a[4] == 2002:
        if a[3] == 1998:
            if a[0] == 'nu':
                if a[1] == 'nim':
                    return 0
                elif a[1] == 'qmake':
                    return 1
            elif a[0] == 'lean':
                if a[2] == 'roff':
                    return 2
                elif a[2] == 'kicad':
                    return 3
        elif a[3] == 1978:
            return 4
    elif a[4] == 1965:
        return 5
    elif a[4] == 1992:
        if a[2] == 'roff':
            if a[0] == 'nu':
                if a[3] == 1998:
                    return 6
                elif a[3] == 1978:
                    return 7
            elif a[0] == 'lean':
                if a[3] == 1998:
                    return 8
                elif a[3] == 1978:
                    return 9
        elif a[2] == 'kicad':
            return 10

print(f21(['lean', 'qmake', 'roff', 1998, 2002]))
print(f21(['nu', 'qmake', 'roff', 1978, 1992]))
"""
import datetime as DT

test = '18/02/2002'

date = DT.datetime.strptime(test, '%d/%m/%Y').date()
print(date)
print(str(date))
print(date.strftime('%Y.%m.%d'))

def f23(table):

    return 0